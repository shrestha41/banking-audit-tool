"""
Unit tests for the Digital Banking Audit Tool.
Run with:  python -m unittest -v test_audit_tool
"""
import ast
import inspect
import unittest

from audit_tool import apply_service_fee, calculate_nested_total, clean_transactions


class TestCleanTransactions(unittest.TestCase):
    def test_removes_non_positive(self):
        self.assertEqual(clean_transactions([-40, 0, 50]), [50])

    def test_removes_below_threshold(self):
        self.assertEqual(clean_transactions([5, 9.99, 12.5]), [12.5])

    def test_threshold_is_inclusive(self):
        self.assertEqual(clean_transactions([10, 10.0, 9.999]), [10, 10.0])

    def test_custom_threshold(self):
        self.assertEqual(clean_transactions([5, 20, 50], min_threshold=25), [50])

    def test_empty_list(self):
        self.assertEqual(clean_transactions([]), [])

    def test_input_is_not_modified(self):
        raw = [250, -40, 5]
        clean_transactions(raw)
        self.assertEqual(raw, [250, -40, 5])


class TestApplyServiceFee(unittest.TestCase):
    def test_default_fee(self):
        self.assertEqual(apply_service_fee([250, 12.5, 100]), [245.0, 12.25, 98.0])

    def test_custom_fee_rate(self):
        self.assertEqual(apply_service_fee([200], fee_rate=0.1), [180.0])

    def test_rounds_to_cents(self):
        self.assertEqual(apply_service_fee([19.99]), [19.59])

    def test_empty_list(self):
        self.assertEqual(apply_service_fee([]), [])


class TestCalculateNestedTotal(unittest.TestCase):
    def test_empty_list_base_case(self):
        self.assertEqual(calculate_nested_total([]), 0.0)

    def test_single_number_base_case(self):
        self.assertEqual(calculate_nested_total(75.5), 75.5)
        self.assertEqual(calculate_nested_total(7), 7)

    def test_assignment_example(self):
        self.assertEqual(calculate_nested_total([100, [50, 25], [[10, 5], 40]]), 230)

    def test_deep_nesting(self):
        self.assertEqual(calculate_nested_total([1, [2, [3, [4, [5]]]]]), 15)

    def test_empty_sublists(self):
        self.assertEqual(calculate_nested_total([[], [[]], 5]), 5)

    def test_string_is_rejected(self):
        with self.assertRaises(TypeError):
            calculate_nested_total(["50"])

    def test_boolean_is_rejected(self):
        with self.assertRaises(TypeError):
            calculate_nested_total([True])

    def test_function_has_no_loops_or_globals(self):
        # Checks the source code against the assignment's forbidden constructs.
        tree = ast.parse(inspect.getsource(calculate_nested_total))
        forbidden = (ast.For, ast.While, ast.AsyncFor, ast.Global)
        self.assertFalse([n for n in ast.walk(tree) if isinstance(n, forbidden)])


if __name__ == "__main__":
    unittest.main(verbosity=2)

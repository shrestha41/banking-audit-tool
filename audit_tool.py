"""
Digital Banking Audit Tool
Lesson 4 Individual Assignment
Uses filter(), map(), lambda expressions, and pure recursion.
"""


def clean_transactions(amounts, min_threshold=10.0):
    """Keep only positive transactions at or above min_threshold."""
    return list(filter(lambda amt: amt > 0 and amt >= min_threshold, amounts))


def apply_service_fee(amounts, fee_rate=0.02):
    """Deduct a percentage service fee from every transaction amount."""
    return list(map(lambda amt: round(amt * (1 - fee_rate), 2), amounts))


def calculate_nested_total(data):
    """
    Recursively total a number or an arbitrarily nested list of numbers.

    Base cases:
        [] -> 0.0
        int/float -> the value itself
    Recursive step:
        non-empty list -> total(head) + total(tail)
    """
    if isinstance(data, list):
        if data == []:
            return 0.0
        head = data[0]
        tail = data[1:]
        return calculate_nested_total(head) + calculate_nested_total(tail)
    if isinstance(data, (int, float)) and not isinstance(data, bool):
        return data
    raise TypeError(f"Unsupported type in batch: {type(data).__name__}")


def main():
    raw = [250, -40, 5, 0, 12.5, 100, 9.99]
    print("Raw batch:        ", raw)

    cleaned = clean_transactions(raw)
    print("Cleaned (>=10.0): ", cleaned)

    processed = apply_service_fee(cleaned)
    print("After 2% fee:     ", processed)

    nested = [100, [50, 25], [[10, 5], 40]]
    print("Nested batch:     ", nested)
    print("Nested total:     ", calculate_nested_total(nested))

    print("Single value:     ", calculate_nested_total(75.5))
    print("Empty list:       ", calculate_nested_total([]))
    print("Deep nesting:     ", calculate_nested_total([1, [2, [3, [4, [5]]]]]))


if __name__ == "__main__":
    main()

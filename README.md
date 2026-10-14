# Digital Banking Audit Tool

Lesson 4 Individual Assignment. A Python audit tool for batch banking transactions.

## Features
- `clean_transactions(amounts, min_threshold=10.0)` removes non-positive and below-threshold amounts using `filter()` and a lambda.
- `apply_service_fee(amounts, fee_rate=0.02)` deducts a percentage fee using `map()` and a lambda.
- `calculate_nested_total(data)` totals arbitrarily nested lists with pure recursion (no loops, no globals).

## Files
- `audit_tool.ipynb` is the Jupyter notebook with code, explanations and outputs.
- `audit_tool.py` is the same code as a runnable script (main demo only).

The notebook also includes an extra cell of edge-case tests (empty input, boundaries, invalid types, recursion limit).

- `test_audit_tool.py` contains 18 unit tests (`unittest`).

## Run
```
python audit_tool.py
python -m unittest -v test_audit_tool
```

## Example output
```
Nested total:      230.0
Deep nesting:      15.0
```

Author: [Your Name]

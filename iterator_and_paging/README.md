# Description
Example of building a custom iterable that pages over data. Each `Page` yields its items and stops at a sentinel (`END_OF_PAGE`). `PagedResult` wraps multiple pages and iterates over them as a single stream.

# Usage
```python page_example.py```

Outputs:
```
1
2
3
4
5
6
7
8
```

# Test
pytest page_example.py

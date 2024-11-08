### How to run
`python -m pytest [--tb=no] [-q][-v]`
tb = traceback
q = quiet mode (brief summary)
v = verbose

### How to run tests from specific file
`pytest tests/test_format_file_size.py`

### How to run specific test function
`pytest tests/test_format_file_size.py::test_format_file_size_returns_format_tb`
or using filtering
`pytest -k <search string in function>`

### How to run tests in specific class
`pytest tests/test_file.py::<TestClassName>::<test_method>`

### How to organize test cases using Data classes (preferred)
```
from dataclasses import dataclass, field
import pytest
from src.method import my_function
```

Define class with 3 attributes
`id` is generated by `__post_init__`
```
@dataclass
class FileSizeTestCase:
    size_bytes: int # function input
    expected_result: str
    id: str = field(init=false)

    def __post_init__(self):
        self.id = f"test_format_file_size_{self.size_bytes}_bytes"
```

Define test cases
```
test_cases = [
    FileSizeTestCase(0, "0B"),
    FileSizeTestCase(1, "1.00 B"),
    FileSizeTestCase(1024, "1 KB"),
    FileSizeTestCase(1024**2, "1.00 MB")
]
```

Decorator tells pytest to run `test_format_file_size` multiple times
`test_case` is an instance of `FileSizeTestCase`
`ids` argument means each test case in output is clearly labeled
```
@pytest.mark.parametrize("test_case", test_cases, ids=lambda tc: tc.id)
def test_format_file_size(test_case):
assert format_file_size(test_case.size_bytes) == test_case.expected_result
```

### How to test exception handling
use `pytest.raises()`

Say your function returns a `ValueError`
```
... raise ValueError("Size cannot be negative")
```

Add 2 fields to `FileSizeTestCase` class to indicate if an error is expected and what its message should be
```
expected_error: type[Exception] = None
error_message: str | None = None
```

Add to `test_cases` list values to trigger except block
```
FileSizeTestCase(
    -1, "", ValueError, "Size cannot be negative"
),
```

Add to testing function to check exception type and error message
If no error is expected, use assert statement to check output
```
    if test_case.expected_error:
        with pytest.raises(test_case.expected_error, match=test_case.error_message):
            format_file_size(test_case.size_bytes)
    else:
        assert format_file_size(test_case.size_bytes) == test_case.expected_result
```

Resources
---------
[Betterstack.com: A Beginner's Guide to Unit Testing with Pytest](https://betterstack.com/community/guides/testing/pytest-guide/)
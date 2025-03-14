# Sorter Class and Unit Tests

## Files
- `sorter.py` - Contains the `Sorter` class with the `sort` method and the interactive script to classify packages based on user input.
- `test_sorter.py` - Contains unit tests for the `Sorter` class.

## Running the Tests
To run the unit tests, execute the following command in your terminal:
```sh
python -m unittest test_sorter.py
```

## Running the Sorter Script
To run the interactive sorter script, execute the following command in your terminal:
```sh
python sorter.py
```

## Example Usage
```python
from sorter import Sorter

result = Sorter.sort(99, 100, 100, 10)
print(result)  # Output: STANDARD
```

## Requirements
- Python 3

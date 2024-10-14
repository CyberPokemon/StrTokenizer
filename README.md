
# StrTokenizer

A Python module that mimics the functionality of the Java `StringTokenizer` class. This class splits a given string into tokens based on a specified delimiter and offers methods to iterate over the tokens, count them, and manipulate the tokenizer's state.

## Installation

To install the `StrTokenizer` package globally, you can use `pip`. Here are the steps to install:

1. Ensure you have `pip` installed on your system.
2. Open your command line interface (CLI) and run:

```bash
pip install StrTokenizer
```

If you want to use it locally without installing, simply download or copy the `tokenizer.py` file and import it into your project.

## Usage

### Import the Module

If the module is installed via pip, import the class from your module:

```python
from StrTokenizer import StrTokenizer
```


If the module (tokenizer.py) is downloaded from GitHub, import it like this:

```python
from tokenizer import StrTokenizer
```

### Creating a StrTokenizer Object

To create an instance of `StrTokenizer`, provide the input string, the delimiter (optional, defaults to a space `" "`), and whether to return the delimiters as tokens (optional, defaults to `False`).

```python
# Example with default delimiter (space)
tokenizer = StrTokenizer("This is a test string")

# Example with custom delimiter
tokenizer = StrTokenizer("This,is,a,test,string", ",")

# Example with custom delimiter and returning the delimiter as tokens
tokenizer = StrTokenizer("This,is,a,test,string", ",", return_delims=True)
```

### Methods

#### `countTokens() -> int`

Returns the total number of tokens in the string.

```python
token_count = tokenizer.countTokens()
print("Number of tokens:", token_count)
```

#### `countTokensLeft() -> int`

Returns the number of tokens left to be iterated.

```python
tokens_left = tokenizer.countTokensLeft()
print("Tokens left:", tokens_left)
```

#### `hasMoreTokens() -> bool`

Checks if there are more tokens to iterate over.

```python
if tokenizer.hasMoreTokens():
    print("There are more tokens available.")
```

#### `nextToken() -> str`

Returns the next token. Raises an `IndexError` if no more tokens are available.

```python
while tokenizer.hasMoreTokens():
    print(tokenizer.nextToken())
```

#### `rewind(steps: int = None) -> None`

Resets the tokenizer's index either completely or by a specified number of steps:
- **Without arguments**: Resets the tokenizer back to the first token.
- **With `steps`**: Moves the tokenizer back by the given number of steps.

```python
# Rewind completely
tokenizer.rewind()

# Rewind by 2 tokens
tokenizer.rewind(2)
```

### Example

```python
from tokenizer import StrTokenizer

# Create a tokenizer with a custom delimiter
tokenizer = StrTokenizer("apple,orange,banana,grape", ",")

# Get the number of tokens
print("Number of tokens:", tokenizer.countTokens())

# Iterate over the tokens
while tokenizer.hasMoreTokens():
    print("Token:", tokenizer.nextToken())

# Rewind the tokenizer and iterate again
tokenizer.rewind()
print("After rewinding:")
while tokenizer.hasMoreTokens():
    print("Token:", tokenizer.nextToken())
```

### Output:

```text
Number of tokens: 4
Token: apple
Token: orange
Token: banana
Token: grape
After rewinding:
Token: apple
Token: orange
Token: banana
Token: grape
```

## Methods Overview

- `__init__(self, inputstring: str, delimiter: str = " ", return_delims: bool = False)`:
  - Initializes the `StrTokenizer` with the given string, delimiter, and whether to return delimiters as tokens.
  
- `create_token(self) -> None`:
  - Splits the input string into tokens based on the delimiter.
  
- `countTokens(self) -> int`:
  - Returns the total number of tokens.
  
- `countTokensLeft(self) -> int`:
  - Returns the number of tokens left for iteration.
  
- `hasMoreTokens(self) -> bool`:
  - Checks if there are more tokens to be retrieved.
  
- `nextToken(self) -> str`:
  - Returns the next available token or raises an `IndexError` if no tokens are left.
  
- `rewind(self, steps: int = None) -> None`:
  - Resets the tokenizer's index either completely or by a given number of steps.
 
You can install the `StrTokenizer` package from PyPI:

[Install StrTokenizer from PyPI](https://pypi.org/project/StrTokenizer/1.0.0/)

## Source Code:

[Github Link](https://github.com/CyberPokemon/StrTokenizer)

## License

This project is open-source and available for modification or distribution.

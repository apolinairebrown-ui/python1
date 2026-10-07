# python1: Multifunction Calculator

A menu-driven command-line calculator written in Python. It supports addition,
subtraction, multiplication, and division, handles invalid input without
crashing, and includes a pytest test suite.

## Features

- Four operations: add, subtract, multiply, divide
- Interactive menu that runs until you type `q`
- Invalid input (like `abc`) shows a message instead of crashing
- Dividing by zero shows a clear error message
- Calculator logic is kept separate from user input, so it is easy to test

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
git clone https://github.com/apolinairebrown-ui/python1.git
cd python1
uv sync
```

`uv sync` creates the `.venv` virtual environment and installs everything the
project needs, including pytest.

## Usage

```bash
uv run main.py
```

or use the installed command:

```bash
uv run python1
```

Example session:

```text
=== Calculator ===
1) Add
2) Subtract
3) Multiply
4) Divide
q) Quit

Choose an option: 4
First number: 20
Second number: 4
20.0 / 4.0 = 5.0
```

## Running the tests

```bash
uv run pytest
```

Add `-v` to see each test by name.

## Project structure

```text
python1/
├── src/
│   └── python1/
│       ├── __init__.py
│       ├── calculator.py     # Pure calculator functions
│       └── cli.py            # Interactive menu
├── tests/
│   └── test_calculator.py    # pytest test cases
├── main.py                   # Entry point: runs the menu
├── pyproject.toml            # Project metadata and dependencies
└── uv.lock                   # Exact dependency versions
```

# Test Calculator

## Overview

This project is a simple calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. These tests help ensure that eval can handle a variety of inputs correctly and raise appropriate errors when necessary.

## Features

- Basic Operations: Tests simple arithmetic expressions.
- Large Numbers: Tests for handling large integer calculations.
- Unary Operations: Tests the handling of unary operators.
- Octal: Tests for octal representations.
- Floating Point and Integers: Tests mixed expressions with floats and integers.
- Invalid Expressions: Tests to ensure proper error handling for invalid and malformed expressions.
- Complex Expressions: Tests nested expressions and operator precedence.
- Overflow Simulation:
  - 10**1000: Tests a very large exponentiation to ensure the evaluator can handle large numbers.
  - 10**100 + 10**100: Tests arithmetic operations with large numbers.
  - 2**100000: This expression tests Python's ability to handle extremely large computations. While it won't cause an overflow as in other languages, it can demonstrate performance and resource usage.

## Project Structure
```
test_calc/
├── .idea/
├── .venv/
├── Scripts/
├── site-packages/
├── .gitignore
├── test_calc.iml
├── calculator_eval.py  # Contains code for the expression evaluator
└── test_calculator_eval.py  # Contains unit tests for arithmetic operations
```

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone [repository-url]
   cd test_calc

2. Set up a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   
## Running Tests
To run the unit tests for the arithmetic operations, use one of the following commands in the terminal:
- To run a specific test file:
  ```bash
  python3 -m unittest test_calculator_eval.py
- To discover and run all tests in the project:
  ```bash
  python3 -m unittest discover

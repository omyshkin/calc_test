# Test Calculator

## Overview

This project is a simple calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division. The project includes unit tests to ensure the correctness of these operations.

## Features

- Addition
- Subtraction
- Multiplication
- Division (with error handling for division by zero)

## Project Structure
```
test_calc/
├── .idea/
├── .venv/
├── Scripts/
├── site-packages/
├── .gitignore
├── test_calc.iml
└── test_operations.py  # Contains unit tests for arithmetic operations
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
  python3 -m unittest test_operations.py
- To discover and run all tests in the project:
  ```bash
  python3 -m unittest discover

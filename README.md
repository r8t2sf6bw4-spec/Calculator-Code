# Python CLI Calculator

A robust command-line interface (CLI) calculator built with Python, focusing on modularity and error handling.

## 🚀 Project Overview (SDLC)

Name: ezirim destiny
Matric: 24/14565
Department: computer science 

### 1. Requirements
- Perform basic operations: Addition, Subtraction, Multiplication, Division.
- Guard against "Division by Zero" errors.
- Validate user input to prevent program crashes.

### 2. Design & Architecture
The project follows a **Functional Programming** approach. It uses a dispatch table (dictionary) to map operators to their respective functions, reducing the complexity of conditional logic.

### 3. Implementation
- **Language:** Python 3.x
- **Key Features:** `try-except` blocks for validation, `while` loops for persistence, and modular function definitions.

### 4. Testing Phase
Testing was conducted using the following scenarios:
| Test Case | Input | Expected Result | Status |
|-----------|-------|-----------------|--------|
| Addition  | 5 + 5 | 10.0            | Pass   |
| Error     | 10 / 0| Error Message   | Pass   |
| Validation| 'abc' | "Invalid input" | Pass   |

## 🛠️ How to Run
1. Ensure you have [Python](https://www.python.org/) installed.
2. Clone this repository or download the script.
3. Run the following command in your terminal:
   ```bash
   python calculator.py

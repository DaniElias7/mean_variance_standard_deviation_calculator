# Statistics Calculator for 3x3 Matrices

This project contains a Python function called `calculate()` that uses the NumPy library to compute the **mean**, **variance**, **standard deviation**, **maximum**, **minimum**, and **sum** of a 3x3 matrix. The calculations are performed along the rows, columns, and the flattened matrix, returning the results in a dictionary.

## Purpose

The goal of this project is to provide a simple and efficient tool for analyzing basic statistics of a 3x3 matrix from 
a list of 9 numbers. It is ideal for students, developers, or anyone interested in basic matrix calculations.

## Features

- **Input**: The `calculate()` function accepts a list with exactly 9 numbers.
- **Conversion**: Transforms the list into a 3x3 matrix using NumPy.
- **Calculations**: Computes the following statistics:
  - **Mean**
  - **Variance**
  - **Standard deviation**
  - **Maximum**
  - **Minimum**
  - **Sum**
- **Output**: Returns a dictionary with lists (not NumPy arrays) in the following format:
  ```python
  {
    'mean': [rows_axis, columns_axis, flattened_matrix],
    'variance': [rows_axis, columns_axis, flattened_matrix],
    'standard deviation': [rows_axis, columns_axis, flattened_matrix],
    'max': [rows_axis, columns_axis, flattened_matrix],
    'min': [rows_axis, columns_axis, flattened_matrix],
    'sum': [rows_axis, columns_axis, flattened_matrix]
  }

## Requirements

- **Python** 3.8 or higher
- The following library:
  - `numpy`

## Installation
1. **Clone or download this repository to your local machine**:
    ```bash
    git clone <COLOCAR_URL_MI_REPOSITORIO>

2. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt

## Usage
The main file **mean_var_std.py** contains the **calculate()** function. You can test it by running main.py from the terminal:

1. **Navigate to the src folder:**
    ```bash
    cd src

2. **Run the main script:**
    ```bash
    python main.py

## Project Structure
- mean_var_std.py: Contains the main calculate() function.
- main.py: File to test the function with examples.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
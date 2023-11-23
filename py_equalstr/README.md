# String Comparison Algorithm

This repository contains a Python implementation of a string comparison algorithm. The algorithm compares substrings of a given string `s` and checks if they are equal. The comparison is performed using hash values to efficiently determine substring equality.

## Algorithm Overview

The algorithm employs rolling hash values to efficiently compare substrings. It uses modular arithmetic to handle hash values and is designed for quick and effective string comparison.

## Usage

1. **Input File:**
   - Provide input strings in an input file (e.g., `input.txt`).
     ```
     Example:
     5          # Length of the string 's'
     abcde      # String 's'
     3          # Number of queries
     2 1 3      # Query 1: Length, Starting Index A, Starting Index B
     3 2 4      # Query 2: Length, Starting Index A, Starting Index B
     4 1 2      # Query 3: Length, Starting Index A, Starting Index B
     ```

2. **Run the Algorithm:**
   - Execute the Python script to perform string comparison.
     ```bash
     python string_comparison_algorithm.py
     ```

3. **Output File:**
   - Check the output file (e.g., `output.txt`) for the results of string comparisons.
     ```
     Example:
     yes        # Result of Query 1
     no         # Result of Query 2
     yes        # Result of Query 3
     ```

## Customization

Feel free to customize the algorithm for your specific use case. The Python script `string_comparison_algorithm.py` can be modified to suit different input formats or requirements.

## License

This string comparison algorithm is released under the [MIT License](LICENSE).

Happy coding!

# Radix Sort Algorithm

This repository contains a Python implementation of the Radix Sort algorithm. Radix Sort is a non-comparative sorting algorithm that works by distributing elements into buckets according to their individual digits. It is particularly useful for sorting integers or strings with fixed-length representations.

## Algorithm Overview

The Radix Sort algorithm implemented in this repository follows the LSD (Least Significant Digit) approach. It iteratively sorts the input array based on individual digits, starting from the least significant digit and moving towards the most significant digit.

## Usage

1. **Input File:**
   - Provide input numbers in an input file (e.g., `input.txt`).
  
     ```text
     
     Example:
     5          # Length of the array
     170, 45, 75, 90, 802      # Array to be sorted
     ```

2. **Run the Algorithm:**
   - Execute the Python script to perform Radix Sort.
  
     ```bash
     python radix_sort_algorithm.py
     ```

3. **Output File:**
   - Check the output file (e.g., `output.txt`) for the sorted array and sorting phases.

     ```text
     Example:
     Initial array:
     170, 45, 75, 90, 802

     **********
     Phase 1
     Bucket 0: empty
     Bucket 1: 170, 90
     Bucket 2: empty
     Bucket 3: 45
     Bucket 4: empty
     Bucket 5: 75
     Bucket 6: empty
     Bucket 7: empty
     Bucket 8: 802
     Bucket 9: empty

     **********
     Phase 2
     Bucket 0: 90
     Bucket 1: empty
     Bucket 2: empty
     Bucket 3: 802, 45
     Bucket 4: empty
     Bucket 5: 170, 75
     Bucket 6: empty
     Bucket 7: empty
     Bucket 8: empty
     Bucket 9: empty

     **********
     Sorted array:
     45, 75, 90, 170, 802
     ```

## Customization

Feel free to customize the algorithm or input format in the Python script (`radix_sort_algorithm.py`) to suit different use cases.

## License

This Radix Sort algorithm is released under the [MIT License](LICENSE).

Happy sorting!

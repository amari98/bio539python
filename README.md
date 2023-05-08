# Big Data Python Exam
Marissa Ardovino

## Overview

This project will allow users to enter a string of nucleic acid base characters (A, T, C, and G) of any length to determine the number of possible substrings and observed unique substrings of any given length and determine the associated linguistic complexity of a string based on a comparison between the possible substrings and the observed substrings. In practice, these tests would allow geneticists and biologists to make estimations about genome assembly, genome size, and allow for the identification of bacterial species within a given string.

## File Navigation

#### BigDataPythonExam.py contains 3 functions to complete this task:

**Function 1: numsubstrings** Count the number of theoretically possible substrings of length k within a given string.

**Function 2: observed** Count the number of unique observed substrings of length k within a given string.

**Function 3: ling_complex** Determine linguistic complexity for a given string by summing the unique observed substrings of all possible lengths for a string and dividing that total by the sum of all possible substrings of all lengths k for the string.

Doc strings contain overview information about the use and variable inputs of each function.
Additional information and descriptions are available in individual line comments on the file.

#### test_PythonExam.py contains all of the tests for each function.

Tests show cases where expected and actual outputs are equivalent, and also cases where the expected output will produce an error message that explains why a particular test case was not possible.


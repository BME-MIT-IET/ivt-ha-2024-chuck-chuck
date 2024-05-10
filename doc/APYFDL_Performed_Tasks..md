# This document provides the documentation on the tasks performed by Adilet Sooronbaev | Neptun: APYFDL

# 1) Manual Code Review Documentation

## Overview

This document shows the findings from a manual code review conducted on selected portions of the code. The review aimed to identify common coding errors, ensure adherence to coding standards, and assess the overall quality of the code. The ultimate goal was to enhance the maintainability and reliability of the codebase.

## Methodology

The review was dont on the following files:
- `algorithms/tree/bst/kth_smallest.py`
- `algorithms/compression/huffman_coding.py`
- `algorithms/automata/dfa.py`

A check-list approach was adopted, utilizing a checklist to evaluate aspects such as:
- variable naming conventions
- code complexity
- adherence to the DRY principle,
- efficiency and documentation of the code
- etc.

## Main Results

### kth_smallest.py
- The initial implementation utilizes an in-order traversal with a stack, recognized for its space efficiency. The second version employs a recursive approach, constructing a list of node values with an O(n) space complexity, potentially less efficient for larger trees.
- Recommendations include enhancing the docstring to clearly show the method's functionality and parameters, ensuring a comprehensive understanding and proper usage of the method.

### huffman_coding.py
- The code is organized into well-defined classes (`Node`, `HuffmanReader`, `HuffmanWriter`, `TreeFinder`, `HuffmanCoding`), each responsible for distinct aspects of the Huffman coding process. This modular structure improves readability and maintainability.
- However, the documentation was found to be lacking. Additional comments in complex logic sections could significantly aid future maintenance efforts. Input validation for file paths and file content was recommended to prevent runtime errors.

### dfa.py
- The implementation effectively simulates a DFA, correctly processing input strings based on a given transition table and determining acceptance based on final states.
- It was noted that the function lacks input validation for transitions, start and final states, and input strings. Validating these inputs is crucial for robustness. Maintaining the Time Complexity at O(n) is suitable for DFA operations.

## Lessons Learned

This manual code review process highlighted several key points:
- The importance of regular code reviews to identify issues early and minimize technical debt.
- The significance of clear, descriptive naming conventions and thorough documentation for managing large codebases and facilitating future modifications.
- Common oversights in input validation and error handling were identified, highlighting their critical role in ensuring software reliability and stability.

This exercise showed the value of manual code reviews as an addition to automated testing, offering insights into the practical aspects of software development and maintenance.

<br>
<br>

# 2) BDD Tests Documentation

## Overview

The integration of Behavior-Driven Development (BDD) testing through the "behave" framework into the Python project was undertaken. The aim was to ensure that the functionalities of the project align with user expectations and documented specifications. Features such as Huffman coding, shortest distance calculations, password strength validation, and a Sudoku solver were tested.

## Methodology

Scenarios reflecting real-world usage were crafted for each feature. These scenarios were then translated into test cases written in Gherkin syntax within the `behave` framework. The tests were structured to validate both positive outcomes and handle edge cases or failure modes effectively.

### Key Features and Scenarios

- **Huffman Coding**
  - Scenarios for encoding and decoding files were tested to verify that the encoded files are smaller than the original and that decoding restores the original content.

- **Shortest Distance from All Buildings**
  - Scenarios were designed to calculate the shortest distance from all buildings in a grid layout, with tests to handle grids with and without empty spaces, ensuring correct distance calculations or appropriate error handling.

- **Strong Password Validation**
  - This feature involved testing the strength of passwords given specific criteria, with scenarios outlining the requirements for a password to be considered strong and providing feedback on how to achieve it.

- **Sudoku Solver**
  - The solver was tested on both fully solvable and unsolvable Sudoku boards to ensure it correctly solves or fails to solve the puzzle as expected.

## Main Results

- **Huffman Coding**
  - The tests confirmed that the Huffman coding implementation not only reduces file size upon encoding but also accurately reconstructs the original data from the encoded format.

- **Shortest Distance to All Buildings**
  - The implementation correctly calculated distances in complex grid scenarios, and appropriately returned errors when no valid paths existed.

- **Strong Password Validation**
  - The validation logic was thoroughly tested to ensure it meets modern security standards, correctly identifying weak passwords and suggesting enhancements.

- **Sudoku Solver**
  - The solver was effective in handling solvable boards and correctly identified and reported unsolvable situations, preventing wasted computational efforts on impossible tasks.

## Lessons Learned

- **Complexity in Test Scenarios**
  - Developing test cases for complex algorithms like Huffman coding and Sudoku solving taught the importance of detailed scenario planning to cover as many edge cases as possible.

- **Feedback Loops**
  - Immediate feedback from failing tests, especially in password strength validation, was crucial in quickly refining the logic and enhancing security measures.

- **Efficiency in Algorithms**
  - BDD tests for the shortest distance calculations highlighted the need for efficient algorithm design to handle dense grid configurations effectively.

This BDD testing cycle has proven useful in validating the functional integrity and robustness of key features in the project, while also providing clear insights into areas for future improvement.

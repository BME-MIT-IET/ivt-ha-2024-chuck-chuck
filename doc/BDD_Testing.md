# This document provides the documentation on the tasks performed by Adilet Sooronbaev | Neptun: APYFDL

# BDD Tests Documentation

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

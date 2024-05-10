# Overview

The task is to achieve 100% coverage for ordered_stack and bitonic_sort

## Summary of work performed
- Wrote unit tests following best practices, used error assertion, and rewrote the stack algorithm because of the error in the code
- Added unit tests to ensure each method of the `OrderedStack` class behaves as expected:
  - **Initialization Test**: Confirmed the stack initializes correctly as empty
  - **Push Method Tests**: Confirmed that items are pushed onto the stack in the correct order and adjusted the push method to handle edge cases more robustly.
  - **Pop Method Tests**: Confirmed the pop functionality and added tests to handle edge cases, including popping from an empty stack
  - **Peek Method Tests**: Implemented tests for the peek functionality to return the top element and ensured it handles empty stack conditions correctly by raising an appropriate error.
  - **Size Method Tests**: Confirmed that the size method accurately reflects the number of items in the stack after various operations
- Implemented a new test for the `bitonic_sort` function to handle non-power-of-two array sizes by asserting `ValueError`
- Fixed the `peek` method within the `OrderedStack` class to include a pre-check for stack emptiness to prevent runtime errors


## Results and Lessons Learned

Learned how to use unittest library for unit testing, including setup of the class to share between unittests, using assertion for errors.
Analize algorithm and find errors and correct them by making correct implementation of that algorithm. Adjusting and implementing unittest for 100% coverage.
# This document provides the documentation on the tasks performed by Csarkovszkij Artyjom | Neptun: N852Z8

# 1) Manual Code Review Documentation

## Overview

This document shows the findings from a manual code review conducted on selected portions of the code. The review aimed to identify common coding errors, ensure adherence to coding standards, and assess the overall quality of the code. The ultimate goal was to find possible efficiency improvements.

## Methodology

The review was done on the following files:
- `algorithms/math/base_conversion.py`
- `algorithms/math/chinese_remainder_theorem.py`
- `algorithms/math/combination.py`
- `algorithms/math/cosine_similarity.py`
- `algorithms/math/decimal_to_binary_ip.py`
- `algorithms/math/diffie_hellman_key_exchange.py`
- `algorithms/math/euler_totient.py`
- `algorithms/math/extended_gcd.py`
- `algorithms/math/factorial.py`
- `algorithms/math/fft.py`
- `algorithms/math/rsa.py`

A check-list approach was adopted, utilizing a checklist to evaluate aspects such as:
- code complexity
- adherence to the DRY principle,
- efficiency and documentation of the code

## Main Results

### base_conversion.py

#### int_to_base(num, base)

- Invalid input handling: There is no check to ensure that the base is within a valid range (e.g., 2-36). Adding such checks would prevent runtime errors or unexpected behavior.
- Documentation: The function documentation is sufficient, but it could be enhanced by describing the range of acceptable values for base and what happens if num is negative.

#### base_to_int(str_to_convert, base)

- Invalid input handling: Like int_to_base, this function lacks checks for the validity of base. Additionally, there is no error handling for characters in str_to_convert that are invalid for the given base.
- Redundancy in comment: The note about using the int() built-in function might confuse users as to why they would use this function instead. Clarifying when this function is beneficial over int() would be useful.

### chinese_remainder_theorem.py

- Efficiency: The method for finding x uses a brute force approach which can be inefficient for large numbers. An optimized approach using the method of successive substitutions could be implemented for efficiency.
- Readability: The function is well-documented with comments explaining the purpose and functionality. However, additional comments explaining the inner workings of _check_coprime and the main loop could enhance understandability.

### combination.py

- Invalid input handling: There are no checks for negative inputs or when r is greater than n, which are cases that mathematically don't make sense for combinations.
- Efficiency: Recursive functions without memoization can lead to significant performance issues due to redundant calculations, as well as memory leaks especially for larger values of n and r.

### cosine_similarity.py

- Function name: The name _l2_distance might be misleading as it calculates the norm rather than the distance. A more appropriate name might be _l2_norm.
- Efficiency: The current implementation iterates over the vector elements manually. Using libraries like NumPy could greatly enhance performance due to vectorization.

### decimal_to_binary_ip.py

- Invalid input handling: There's no check for the input range. Since an IP address segment should be between 0 and 255, adding a range check would prevent incorrect values.
- Efficiency: Instead of manually checking each bit, Python's built-in functions can handle binary conversion (e.g., bin(val)[2:].zfill(8)), which could simplify and speed up the code.

### diffie_hellman_key_exchange.py

- Invalid input handling: The script includes basic checks for primes and primitive roots.
- - Complexity and Modularity: The code is quite modular, with distinct functions handling specific tasks. This separation makes it easier to understand and maintain.
- Documentation: Each function has a brief description, but the documentation could be expanded to include more details on the parameters and the return values.

### euler_totient.py

- Algorithm Explanation: The function iteratively checks each number from 2 up to the square root of n to determine if it divides n. The approach is efficient for its purpose, given its O(sqrt(n)) complexity.
- Invalid input handling: There is no error handling for non-integer or negative inputs. Since ϕ(n) is defined for positive integers, it would be useful to enforce this.

### extended_gcd.py

#### Discovered a serious issue in code implementation.
The operation quotient = old_r / r should be an integer division (quotient = old_r // r), not a floating-point division. This mistake causes the function to fail for non-integer values.
#### Unit tests refactored to validate new code.
The old unit tests were purely implemented and supposedly created solely based on the function's output, without considering computations by the tester

### factorial.py

#### factorial(n, mod=None)

- Input Validation: The function includes robust input validation, checking that n is a non-negative integer and that mod is a positive integer if provided.
- Efficiency: The iterative approach is efficient and straightforward.
- Documentation: The documentation clearly states the purpose and the functionality, including the time complexity.

#### factorial_recur(n, mod=None)

- Efficiency and Stack Overflow: While recursion in Python is elegant, it can lead to stack overflow errors for large n due to Python's default recursion depth limit. This is a significant limitation for the recursive version.
- Redundancy: The recursive function repeats the same input validation as the iterative version. While this is necessary for correctness, it could be refactored to reduce code duplication.
- Documentation: Similar to the iterative version, the documentation is clear but could benefit from example usage.

### fft.py

- Complexity: This implementation is efficient for lengths of N that are powers of two. However, the function does not check if N is indeed a power of two, which could lead to incorrect results or infinite recursion if not properly handled.
- Performance: The recursive implementation is elegant but might not be as efficient as an iterative version due to function call overhead and potential stack depth issues for very large inputs.
- Documentation: The function includes a basic description and an example, which is helpful.

### rsa.py

- Comments: Use docstrings to provide detailed information on functions.
- Efficiency: Implement the Extended Euclidean Algorithm in modinv for efficiency. Consider improving the primality test in gen_prime.
- Security: The generation of e as a random prime is unconventional; typically, e = 65537 is used. Ensure your prime generation consistently produces primes of the correct bit length.
- Bugs: Use integer division (//) for p_size and q_size to avoid type issues. Check the bit length of generated primes to ensure accuracy.

## Lessons Learned

- Regular Reviews: The review underscored the importance of regular code checks to detect problems early and reduce technical debt, ensuring the codebase remains manageable and efficient.
- Naming and Documentation: The use of clear, descriptive naming conventions and comprehensive documentation is crucial for large codebases, aiding in future modifications and making maintenance simpler.
- Input Validation and Error Handling: The review identified common lapses in input validation and error handling, emphasizing their essential role in maintaining software reliability and stability.
- Value of Manual Reviews: This exercise demonstrated the benefits of manual code reviews complementing automated testing, providing deep insights into practical software development and maintenance challenges.
<br>
<br>

# 2) Unit tests

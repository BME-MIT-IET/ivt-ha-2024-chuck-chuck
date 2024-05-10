# Static Analysis Report

Written and Documented by Mean Diamand and Doskozhoeva Eliza

## Objective

- The goal of this document is to provide the overview of some implementations of the project by using the static analysis tool to automatically reviewing the code of the project which can result in clean code.

## Tool

- For the tool that we used for running the static analysis is SonarQube which is an open source platform for inspecting code quality that perform automatic reviews with static analysis of code to detect bugs and code smells on the project.

## Overview of the Project

![](f1.png)

### Quality Gate Status:

- SonarQube has indicated that the project meets the redefined quality criteria set in SonarQube's Quality Gate. This is a good sign that the project's codebase maintains a standard of quality.

### Sections Overview:

- Security: no open issues which indicates that there aren't any issues detected in the changes concerning the security of the project after making changes.
- Reliability: 7 open issues were showing and marked as Medium severity (M). These issues pertain to potential bugs in the code that could affect the application’s behavior but are not critical.
- Maintainability: 280 Open issues which consisting of 50 High(H), 58 Medium(M), 172 Low(L). This suggests the areas in the code that might be complex, potentially poorly documented, or challenging to modify and maintain.

### List of the Issues

Since the project that we using is quite large, so we decide to document the static analysis report on only the some implementations of the project as shown below:

## maths

#### Reliability Issues:

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\polynomial.py

![](f2.png)

![](f3.png)

- These issues indicate that there is an unreachable code and need can be delete or refactor since we already raising the error, there is no point of returning.

#### Maintainability Issues:

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\chinese_remainder_theorem.py

![](f4.png)

- This issue indicates that the usage of the operator is wrong and it is preferrable to use the '!=' operator which is straightforward instead of the combination of the 'not' keyword with the '==' operator which is less readable.

![](f5.png)

![](f7.png)

![](f9.png)

![](f10.png)

- These issues indicate that it is not good to raise the generic exception class like this which will cause a negative impact on any code that is trying to catch this exceptions. It is better to catch exception that are intended to be catch. Ex: ValueError()...etc.

![](f6.png)

![](f8.png)

- These issues indicate that the usage of the operator is wrong and it is better to use the '<=' operator instead rather than using the combination of the 'not' keyword and the '>' operator which is confusing.

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\fft.py

![](f11.png)

- This issue indicates that the unused loop index which is an unused local variable can be named with '\_' symbol instead of using 'i' which may lead to curiosity of variable being declared but not use or causing a bug or incomplete code.

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\polynomial.py

![](f12.png)

![](f13.png)

- These issues indicate that the 'add' and 'sub' methods handle additions/subtraction with int, float, and Fraction types but not the Monomial object type which is different from the declared type and could lead to type errors.

![](f14.png)

- This issue indicates that having a nested function and lambdas can create tricky bugs when the variable and the function are defined in a loop.If the function is called in another iteration or after the loop finishes, it will see the variables' last value instead of seeing the values corresponding to the iteration where the function was defined.

![](f15.png)

![](f16.png)

- These issues indicate that the 'return' is not needed since we already raise error exception which make 'return' to be unreachable.

![](f17.png)

- This issue indicates that there is a code duplication in the other branch of the conditional statement which can make the code hard to read, understand and maintain. Ex: when you want to modify one of the branch and you might forget to modify the other one which is the same. The best way is to merge it together into on branch of conditional statement.

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\pythagoras.py

![](f18.png)

- This issue indicates that there is an empty 'except' clause which is not preferrable since it will catches all type of exceptions that can result in unexpected errors or bugs in the program. It is better to specify the type of the exception such as ValueError, TypeError...etc.

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\rabin_miller.py

![](f20.png)

- This issue indicates the complexity of the method that required some refactoring to reduce its Cognitive Complexity. This issue was raised due to how hard to understand the control flow of this method and hard to read, test and modify. The method was complex due to the nested function that it is having. The better way is to separate it into smaller functions which make it easy to understand, readable and also easy for extending/modification.

**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\rsa.py

![](f21.png)

- This issue is also the same as the previous one which indicates about the complexity of the method that requirement separation into smaller and understandable functions which help to reduce the Cognitive Complexity of the function.

![](f22.png)

- This issue indicates the wrong usage of the operator. In the code, using a combination between 'not' keyword with the '==' operator is not preferrable and may lead to confusion. It is better to use '!=' operator instead which is more straightforward and easy to understand.

## stack

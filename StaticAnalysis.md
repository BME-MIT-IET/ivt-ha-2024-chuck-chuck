# Static Analysis Report
## Objective
- The goal of this document is to provide the overview of the maths implementation of the project by using the static analysis tool to automatically reviewing the code of the project which can result in clean code.
## Tool
- In this task, we are utilizing the SonarLint extension for Visual Studio Code to enhance our code quality analysis process. SonarLint seamlessly integrates with our project development, providing real-time feedback on potential issues as we write and modify code. We can identify and address code quality issues efficiently, leading to a more robust and maintainable codebase. 
## Overview of the Project
![](f1.png)
### Quality Gate Status:
- SonarQube has indicated that the project meets the redefined quality criteria set in SonarQube's Quality Gate. This is a good sign that the project's codebase maintains a standard of quality.
### Sections Overview:
- Security: no open issues which indicates that there aren't any issues detected in the changes concerning the security of the project after making changes.
- Reliability: 7 open issues were showing and marked as Medium severity (M). These issues pertain to potential bugs in the code that could affect the application’s behavior but are not critical.
- Maintainability: 280 Open issues which consisting of 50 High(H), 58 Medium(M), 172 Low(L). This suggests the areas in the code that might be complex, potentially poorly documented, or challenging to modify and maintain.
### List of the Issues
Since the project that we using is quite large, so we decide to document the static analysis report on only the maths implementation of the project as shown below:
#### Reliability Issues:
**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\polynomial.py
![](f2.png)
![](f3.png)
- These issues indicate that there is an unreachable code and need can be delete or refactor since we already raising the error, there is no point of returning.
#### Maintainability Issues:
**Location:** ivt-ha-2024-chuck-chuck\algorithms\maths\chinese_remainder_theorem.py
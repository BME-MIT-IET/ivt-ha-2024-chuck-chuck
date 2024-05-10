# Overview

We used Python with the PyCharm IDE. The goal of this tasks is to setup environment that provides a basis for working on this project.
## Installation Steps

1. **Set up a Virtual Environment:** 
PyCharm it will ask you to automatically create a virtual environment, which you should accept to ensure no project dependencies interference.

2. **Install Requirements:**
Execute the following command to install the required packages:
    ```
    pip install -r test_requirements.txt
    ```

3. **Verify Installation:**
To ensure all packages are installed correctly, run:
    ```
    pip freeze
    ```
This command lists the installed packages along with their versions, which you can check with the content of `test_requirements.txt`

## Results and Lessons Learned

Successfully setting up Python environment in PyCharm allowed us to learn about virtual environment and the benefits of automated setup through dependency files.
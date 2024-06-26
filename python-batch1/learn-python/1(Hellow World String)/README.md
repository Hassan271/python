# Class Topics
- print()
- Variable
- id() function returns the address where the object is stored.
- del var_a, var_b
- Multiple Assignment a=b=c=10   a,b,c = 10,20,30

## Python Variables - Naming Convention

- A variable name must start with a letter or the underscore character
- A variable name cannot start with a number or any special character like $, (, * % etc.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
- Python variable names are case-sensitive which means Name and - NAME are two different variables in Python.
- Python reserved keywords cannot be used naming the variable.

### If the name of variable contains multiple words, we should use these naming patterns

- **Camel case** − First letter is a lowercase, but first letter of each subsequent word is in uppercase. For example: kmPerHour, pricePerLitre

- **Pascal case** − First letter of each word is in uppercase. For example: KmPerHour, PricePerLitre

- **Snake case** − Use single underscore (_) character to separate words. For example: km_per_hour, price_per_litre

<!-- =================================================== -->

# Project Setup Guide

This guide explains how to set up the development environment using Anaconda, Visual Studio Code (VS Code), and Python.

## Important Note: We are Moving To Poetry from Anaconda

[Class 1 Poetry Video](https://www.youtube.com/watch?v=g9u-H628jXg&t=16s)

# Create Project and Manage Dependencies with Poetry

`Poetry` combines dependency management, environment management, and packaging into a single tool. This means you don’t have to juggle between multiple tools like `pip`, `virtualenv`, and `setuptools`.

Poetry in Python: Poetry is Python's answer to npm and Yarn, offering similar functionalities like managing dependencies, creating virtual environments, and ensuring reproducibility of projects. It simplifies the Python development workflow, making it easy to create robust applications.

Follow the txt file in this directory.

[Python Poetry Cheatsheet](https://gist.github.com/CarlosDomingues/b88df15749af23a463148bd2c2b9b3fb)

<!-- --------------------------------------------------------------------- -->
[Poetry Windows Installation](https://gist.github.com/Isfhan/b8b104c8095d8475eb377230300de9b0)

Step-By-Step guide to installing Poetry on Windows:

1- Open Windows Powershell: Navigate to your Start menu, type "Powershell", and select "Windows Powershell" from the search results.

2- Run Installation Command: In the Powershell window, paste the following command and press Enter:

Note: If you've installed Python through the Microsoft Store, replace py with python in the command below.
cmd >> 
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python - 

3- Wait for Installation to Complete: The installation process may take some time depending on your internet connection speed. Let it run until completion.

4- Copy Installation Path: Once the installation is complete, it will provide you with a path. Copy this path as you'll need to add it to your user environment variables.
To get started you need Poetry's bin directory (C:\Users\Administrator\AppData\Roaming\Python\Scripts) in your `PATH`
environment variable.

open in explorer 
C:\Users\Administrator\AppData\Roaming\Python\Scripts

5- Add Path to Environment Variables:

Right-click on the Start button and select "System".
In the System window, click on "Advanced system settings" on the left sidebar.
In the System Properties window, click on the "Environment Variables..." button.
In the Environment Variables window, under "User variables for [YourUsername]", find the "Path" variable and select it.
Click on the "Edit..." button.
In the Edit Environment Variable window, click on "New" and paste the path you copied from the installation process.
Click "OK" on all open windows to save your changes.

poetry --version

6- Close and Reopen Powershell: Close the Powershell window and open a new one.

7- Verify Installation: In the new Powershell window, type poetry --version and press Enter. If Poetry has been successfully installed, you should see its version number printed in the terminal.

You have now successfully installed Poetry on your Windows system. You can start using it for managing your Python projects.
<!-- --------------------------------------------------------------------- -->

[Poetry Commands](https://realpython.com/dependency-management-python-poetry/#command-reference)

poetry new project_poetry1
cd project_poetry1                      # virtual Env Created 
poetry run python --version             

open
C:\Users\Administrator\project_poetry1

poetry env list

poetry add requests 

poetry run python project_poetry1\main.py
output = Hello world Return

poetry add pytest
poetry run pytest 
 
poetry build
poetry publish 

<!-- ------------------------------ -->

[Poetry vs. Pip: Modern Python Dependency Management Unveiled](https://python.plainenglish.io/poetry-vs-pip-modern-python-dependency-management-unveiled-15d39e059d39)

[The Pain and the Poetry of Python](https://www.pinecone.io/blog/pain-poetry-python/)

[Install pipx](https://pipx.pypa.io/stable/installation/)

[Follow Poetry Tutorial](https://realpython.com/dependency-management-python-poetry/)

    poetry —-version

Note: If you have a old version of Poetry Installed Upgrade it:

    pipx upgrade poetry

[Poetry Docs](https://python-poetry.org/docs/)

[What are Packages in Python and What is the Role of __init__.py files?](https://martinxpn.medium.com/what-are-packages-in-python-and-what-is-the-role-of-init-py-files-82-100-days-of-python-325a992b2b13)

[Poetry Commands](https://realpython.com/dependency-management-python-poetry/#command-reference)

poetry run python --version

# Poetry for Microservice

Poetry is a tool for dependency management and packaging in Python. While it is not specifically optimized for microservices development, but its features can be particularly beneficial in a microservices architecture. Let's explore how Poetry aligns with the needs of microservices development:

### Features of Poetry Beneficial for Microservices

1. **Dependency Management**: Poetry provides a robust system for managing project dependencies. Each microservice in a microservices architecture typically has its own set of dependencies, and Poetry can help manage these dependencies effectively, reducing conflicts and ensuring consistency.

2. **Reproducible Builds**: Poetry locks dependencies to specific versions (through `poetry.lock` file), ensuring that every build is reproducible. This is crucial in microservices, where different services need to operate consistently across various environments.

3. **Easy Packaging**: With Poetry, packaging and distribution of Python packages are simplified. This can be useful for microservices, especially if they are distributed as packages or if you are working in a Python monorepo setup.

4. **Virtual Environments Management**: Poetry automatically manages virtual environments, keeping dependencies isolated for each project. In microservices, this means that each service can have its own isolated environment, reducing the risk of dependency conflicts.

5. **Streamlined Workflow**: Poetry streamlines various tasks like adding/removing dependencies, updating dependencies, and publishing packages. This can improve developer productivity, especially in a microservices setup where managing multiple small services can become complex.

6. **Integration with CI/CD Pipelines**: Poetry can easily be integrated into Continuous Integration/Continuous Deployment (CI/CD) pipelines, which are often a critical part of microservices infrastructure for automated testing and deployment.

### Considerations for Microservices Development

1. **Service Size and Complexity**: For simple microservices, the features offered by Poetry might be more than what is needed. However, for complex services with many dependencies, Poetry's dependency management and environment isolation can be extremely valuable.

2. **Consistency Across Services**: Using the same tool for dependency management across all microservices can help maintain consistency and standardization, which is essential in a distributed architecture.

3. **Language Specificity**: Poetry is a Python-specific tool. If your microservices architecture involves multiple programming languages, you might need different tools for dependency management for services not written in Python.

4. **Learning Curve**: For teams not familiar with Poetry, there might be a learning curve involved. However, Poetry is generally considered user-friendly and well-documented.

### Conclusion

While Poetry is not specifically tailored for microservices, its features around dependency management, environment isolation, and ease of packaging align well with the requirements of microservices development in Python. It provides a modern and efficient way to manage Python projects, which can be highly beneficial in a microservices context, especially for complex services or when working in a polyglot environment where consistency in Python-based services is important.



## Our Previous Anaconda Material

## YouTube Tutorial Link 
[2 hours live session](https://www.youtube.com/watch?v=rwDHhx76MMg)

## Prerequisites

- [Anaconda](https://www.anaconda.com/products/individual#Downloads)
- [VS Code](https://code.visualstudio.com/Download)

---

## Table of Contents

1. [Running a "Hello World" Program](#running-a-hello-world-program)
2. [Setting Up a Virtual Environment](#setting-up-a-virtual-environment)

---

## Running a "Hello World" Program

You can run a simple "Hello World" program to ensure that your Python setup is working as expected.

### Using Anaconda Prompt on Windows

1. Open Anaconda prompt
2. Run the following Python command:

    ```bash
    python -c "print('Hello world')"
    ```

### Using VS Code (.py file)

1. Open VS Code and create a new Python file called `class1.py`.
2. Write the following Python code:

    ```python
    print("Hello world")
    ```

3. Install the Python extension for VS Code if you haven't done so.
4. Click on the Run button to execute the code.

### Using VS Code (.ipynb file)

1. Open VS Code and create a new Jupyter Notebook called `class1.ipynb`.
2. Insert the following Python code into a new cell:

    ```python
    print("Hello world")
    ```

3. Click on the Run button to execute the cell.

---

## Setting Up a Virtual Environment

### Creating a New Environment

1. Run the following command to create a new Conda environment:

    ```bash
    conda create -n <env_name> python==3.12 -y
    # Example: conda create -n python12 python==3.12 -y
    ```

2. Activate your newly created environment:

    ```bash
    conda activate <env_name>
    # Example: conda activate python12
    ```

### Installing Required Packages

1. Create a `requirements.txt` file with the following content:

    ```
    mypy
    ```

2. Run the following command to install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

### Selecting the Environment in VS Code

1. Open `class1.py` in VS Code.
2. Select your virtual environment as shown below:

    ![Alt text](image-2.png)

    ![Alt text](image-1.png)

### Selecting the Environment in Jupyter Notebook

1. Open `class1.ipynb` in Jupyter Notebook.
2. Select your virtual environment as shown below:

   ![Alt text](<Screenshot 2023-10-16 at 10.34.08 PM.png>)

    ![Alt text](image-1.png)







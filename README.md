# python_package
### Package your Python code as Wheel File
[link](https://www.youtube.com/watch?v=TMTHNCJo-Tc)


#### python code can be distributed many ways
- As a package
- As a web service
- As a docker image


- In this tutorial, we will cover the distribution of python code as a package,  it can be shared, distributed with others as wheel file and Install wheel file in system.



##### Pre-requisites

- Install python
- Install pip
- Setuptools should be installed
- Install wheel

- Pip install setuptools wheel

#### Check version of packages
-Pip –version
- Python –version


- Pip is python package manager to install and uninstall packages

#### Task1
Create a parent folder say python_wheel_example
In this create a subfolder say mypackage
Create a python file with few methods in mypackage
Create __init__ file empty file in mypackage
Create setup.py file using touch setup.py


#### Task2
Content for setup file

```aidl
import setuptools

setuptools.setup(name='myPackage',
version='0.1',
author='My Name',
author_email = 'test@gmail.com',
description='My first package',
packages= setuptools.find_packages(),
claaifiers=[
"Programming Language :: Python :: 3",
"License :: OSI Approved :: MIT License",
"Operating System :: OS Independent",
],
python_requires='>=3.6',
)
```

#### Task3
Python setup.py bdist_wheel


#### Task4
Cd dist

Pip install myPackage….whl

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
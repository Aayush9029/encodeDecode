from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='morse3',  
    version='2.9',
    author="Aayush Pokharel",
    author_email="aayushpokharel36@gmail.com",
    description="A morse code encryption / decryption library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aayush9029/encodeDecode",
    py_modules=["morse3"],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

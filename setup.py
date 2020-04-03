import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='morse3',  
    version='0.4',
    scripts=['morse3'] ,
    author="Aayush Pokharel",
    author_email="aayushpokharel36@gmail.com",
    description="A morse code encryption / decryption library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aayush9029/morse3",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    
)
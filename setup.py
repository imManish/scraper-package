import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(

    name="dadventures-python-sdk",
    version="0.0.1",
    author="Dadventures",
    author_email="support@dadventure.com",
    description="This is a Dadventures official scrapper tool package",
    long_description="This is official Sdk",
    long_description_content_type="text/markdown",
    url="",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],

)
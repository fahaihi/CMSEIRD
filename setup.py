import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="CMSEIRD",
  version="2.0.1",
  author="SH&XHN",
  author_email="adairmillersh@gmail.com",
  description="Infectious disease prediction model CM-SEIRD",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url="https://github.com/fahaihi",
  packages=setuptools.find_packages(),
  classifiers=[
  "Programming Language :: Python :: 3",
  "License :: OSI Approved :: MIT License",
  "Operating System :: OS Independent",
  ],
)
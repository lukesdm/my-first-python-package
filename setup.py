from setuptools import setup, find_packages
from pathlib import Path

# Requirements
try:
  this_directory = Path(__file__).absolute().parent
  with open((this_directory / "requirements.txt"), encoding = "utf-8") as f:
    requirements = f.readlines()
  requirements = [line.strip() for line in requirements]
except FileNotFoundError:
  requirements = []

# Metadata
setup(
  name = "lukepy",
  version = "0.0.0.9000",
  author = "LM",
  author_email = "luke@example.com",
  description = "Doesn't do much.",
  license = "UNLICENSE",
  packages = find_packages(),
  install_requires = requirements
)

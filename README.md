# python-ideas

## Background

This repo contains my notes from going through the [official python docs](https://docs.python.org/3.10/).

I was using Python 3.10 on Linux 21.

## Non-Script Notes

Code can be checked using the tools [black](https://github.com/psf/black), [isort](https://pycqa.github.io/isort/), and [flake8](https://github.com/pycqa/flake8)).

These tools need to be installed. This can be achieved by opening the terminal and typing:

python3 -m pip install black isort flake8

They can then be used via the terminal. For example, I tend to run them in this sequence:

isort file_name.py
black --line-length 79 file_name.py
flake8 file_name.py

This sorts the Python imports order, the layout of the code, and then reports any remaining potential issues, respectively.

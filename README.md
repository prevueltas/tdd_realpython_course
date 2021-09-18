# TDD Realpython course with PyTest

This repo contains the source code of the course 
[Test-Driven Development With PyTest](https://realpython.com/courses/test-driven-development-pytest/)

The code provided by the original author didn't work for me (and other users as you can read in the comments of the
course) out of the box.

## Setup

It uses pipenv to handle the virtual env:

```bash
pipenv install
```

## Running the test

We run pytest as a python module to have included the current directory CWD in sys.path: 

```bash
pipenv shell
python -m pytest -v
```

## Coverage report

In order to have the --cov option available we need to add the pytest-cov plugin (as included in the Pipfile):

```bash
pipenv shell
python -m pytest -v --cov
```

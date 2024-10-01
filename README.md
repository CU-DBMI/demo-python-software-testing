# demo-python-software-testing

A project to help demonstrate Python software testing.

## Using this demonstration

We use [Poetry](https://python-poetry.org/docs/) to help manage the Python environment for this project.
Please see the [installation documentation](https://python-poetry.org/docs/#installation) for more information on how to use Poetry from your system.

After installing Poetry, you'll need to install this project's environment.

```bash
poetry install
```

### Running tests

We use [`pytest`](https://docs.pytest.org/en/stable/) to run tests found in this project.
`pytest` is a part of the project environmen so we use Poetry to run it.
A [Hypothesis](https://github.com/HypothesisWorks/hypothesis) test is included as part of the tests which are processed using `pytest`.

```bash
poetry run pytest
```

Doctests may optionally be included with `pytest` runs using the following command:

```bash
poetry run pytest --doctest-modules
```

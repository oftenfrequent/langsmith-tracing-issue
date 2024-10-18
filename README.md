# Langsmith Issue

The purpose of this repo to demonstrate an issue with the `langsmith` package. Robust testing is a very important part of software development. The `langsmith` package is a great tool for testing Python code. However, it has a limitation that makes it difficult to test code with `pytest` and `unittest` while using decorators to trace function calls.

## Setup

Environment was set up with Python 3.12.6. For reproducability, please use the same version.

```bash
pip install -r requirements.txt
pytest -vv
```

After running tests, you will see that the test `test_decorator` fails when run with `trio` despite passing when run with `asyncio`.

# Django Testing

[Django testing](https://docs.djangoproject.com/en/3.0/topics/testing/) - Django Docs

## About Django testing
1. Django’s unit tests use a Python standard library module: unittest.
1. When you run your tests, the default behavior of the test utility is to find all the test cases (that is, subclasses of unittest.TestCase) in any file whose name begins with test, automatically build a test suite out of those test cases, and run that suite.

## Run tests

```bash
$ ./manage.py test
```

## The test database
1. Separate, blank databases are created for the tests.
1. Regardless of whether the tests pass or fail, the test databases are destroyed when all the tests have been executed.
1. You can prevent the test databases from being destroyed by using the **test --keepdb** option

## Order in which tests are executed¶

1. All TestCase
1. Then, all other Django-based tests (test cases based on **SimpleTestCase**, including **TransactionTestCase**) are run with no particular ordering guaranteed nor enforced among them.
1. Then any other **unittest.TestCase** tests (including doctests) that may alter the database without restoring it to its original state are run.

## The Django test client

```python
from django.test import Client
# create an instance of the client for our use
client = Client()
```
import pytest

def pytest_addoption(parser):
    parser.addoption("--branch", action="store", default="data",
        help="Please enter the branch on which to test the system")

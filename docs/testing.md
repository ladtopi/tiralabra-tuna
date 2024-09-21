# Testing report

Testing of the project is done using the `pytest` framework in Python. In
addition, `hypothesis` is used for invariant testing. The tests are located in
the `tests` directory, and can be run using the command `pytest`.

Automatic testing does not cover the user interface (which is minimal anyhow).

## Test types

Unit tests, invariant tests, and performance tests are used to test the project.

TODO: more details

## Unit test coverage

The unit test coverage of the project is measured using the `coverage` tool. The
coverage report can be generated using the command `coverage run` and viewed
using the command `coverage report`.

The coverage is monitored in Codecov.

[![codecov](https://codecov.io/github/ladtopi/tiralabra-tuna/graph/badge.svg?token=0OIABY3SPG)](https://codecov.io/github/ladtopi/tiralabra-tuna)

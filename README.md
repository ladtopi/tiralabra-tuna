# Tuna - A digital guitar tuner

[![codecov](https://codecov.io/github/ladtopi/tiralabra-tuna/graph/badge.svg?token=0OIABY3SPG)](https://codecov.io/github/ladtopi/tiralabra-tuna)

This is a course project for the _Algorithms and Artificial Intelligence Project_
at the University of Helsinki. The project consists of a digital guitar tuner
that can be used to tune a guitar using a computer. The tuner is implemented in
Python and uses Fast Fourier Transform (FFT) to analyze the sound input from a
microphone.

## Documentation

- [Specification](/docs/specification.md)
- [Week 1](/docs/week1.md)
- [Week 2](/docs/week2.md)
- [Week 3](/docs/week3.md)
- [Week 4](/docs/week4.md)
- [Week 5](/docs/week5.md)
- [Implementation](/docs/implementation.md)
- [Testing](/docs/testing.md)
- [User manual](/docs/manual.md)

## Running the application

The project uses poetry for dependency management. To run the project, make sure you have python3 and poetry installed. Then install the dependencies with `poetry install`, and run the application with the following command:

```bash
poetry run python tuna/app.py
```

More detailed instructions can be found in the [User manual](/docs/manual.md).

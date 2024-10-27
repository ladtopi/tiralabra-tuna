# Testing report

Testing of the project is done using the `pytest` framework in Python. In
addition, `hypothesis` is used for invariant testing. The tests are located in
the `tests` directory, and can be run using the command `pytest`.

Automatic testing does not cover the user interface (which is minimal anyhow).

## What has been tested

Unit tests (both static and property based invariant tests), and performance
tests are used to test the project.

Unit tests are used to verify the correctness of the individual functions, such
as the FFT and naive DFT. Since it's easier to understand the naive DFT and
implement it correctly, I used it as a reference for the correctness of the FFT
implementation. After all, the output from both should be exactly the same,
making this an excellent candidate for an invariant test.

Basically every function with a public signature is tested with unit tests, not
including the `app` module. Some functionality in the `Tuner` class is also
untested, but these are mostly very simple wrappers on the audio device library,
and are easily tested with manual tests as part of normal operation. I tried my
best to compartmentalize the functions so that they are easy to test in
isolation. Most functions have some simple static test cases (traditional unit
tests), that are used to test some known cases. For the most part, I favored
test driven development, so I generally wrote down some static test cases before
implementing the actual functions. Invariant testing with randomized inputs is
also used heavily wherever applicable, to make the tests representative with a
wide variety of inputs.

In addition to unit tests, performance tests are used to measure the performance
of the FFT implementation. The performance tests are located in the `tests/performance`
directory.

## Some key tests

For the **DFT** implementation, there are tests for some basic cases, such as
verifying the output for a simple sine and cosine wave. The output correctness
is also verified with a small complex (in form) signal. Additionally, the even
symmetry property for real signals is covered by testing with a large number of
random inputs.

The **FFT** implementation is tested against the naive DFT implementation, on
the grounds that the outputs should be the same. Naturally, `hypohesis` is
leveraged to generate a large number of random inputs. Additionally, since this
FFT implementation is radix-2, checking this precondition is tested as well.

The main **pitch detection** algorithm is tested with simple signals that are
easy to generate and test. Both sine waves and square waves (that are harmonic
by nature) are used. Again, the algorithm is tested with a large number of these
waveforms in random frequencies. The wave generators are tested separately.

Finally, the **performance** of the FFT implementation is compared to that of
the direct naive DFT implementation to verify that it is indeed (significantly)
faster. This is verified by running the same input through both implementations
10 times and comparing the average running times. This test is also run with a
larger signal, to see that the gap should start to widen quickly.

## Known deficiencies in the tests

For the most part I'm really happy with the test coverage of the project. The
only thing that bugs me a bit is that I don't have end to end tests, and I don't
have tests with signals coming from an actual guitar. However, to counter
argument the former, I did perfrom manual extensive manual testing of the
application. For the latter, I don't necessarily think testing with one or two
recorded guitar notes would have provided much value here. Also it is just an
accepted fact that the pitch detection algorithm does suffer from octave errors
with signals that have harmonics of varying intensities. The tests that are in
place do work pretty well in determining the correctness with more controlled
signals.

## Unit test coverage

The unit test coverage of the project is measured using the `coverage` tool. A
new report can be generated using the command `poetry run inv coverage`.

At the time of writing, the coverage report is as follows:

```
Name                Stmts   Miss Branch BrPart  Cover   Missing
---------------------------------------------------------------
tuna/dft.py            10      0      6      0   100%
tuna/fft.py            32      0     12      0   100%
tuna/filtering.py       5      0      0      0   100%
tuna/pitch.py          11      0      0      0   100%
tuna/tonal.py          12      0      2      0   100%
tuna/tuner.py          33      0      6      0   100%
tuna/utils.py           7      0      4      0   100%
tuna/wavegen.py         7      0      0      0   100%
---------------------------------------------------------------
TOTAL                 117      0     30      0   100%

1 empty file skipped.
```

The unit test coverage is also monitored in [Codecov](https://codecov.io/github/ladtopi/tiralabra-tuna).

## Running the tests

The tests can be run inside the Poetry environment as follows:

- `poetry run inv test-all` to run all tests
- `poetry run inv test-unit` to run only the unit tests
- `poetry run inv test-perf` to run only the performance tests

# Implementation report

This document outlines the implementation of the project, covering the structure
of the project, analysis of the key algorithms, shortcomings, and suggestions
for improvement. The document also discusses the usage of AI in the project.

## Structure

The end product in this project is a guitar tuner application. It uses a
microphone attached to the user's computer to read in audio data and then tells
the user the nearest pitch (in musical notation), as well as how far (in Hz)
from that pitch the estimated fundamental frequency is.

The project was built using Python, and resides wholly in the `tuna` package.
Relevant components are organized into suitably named modules. Different problem
areas are addressed in separate modules. The key parts in the project are
structured as follows:

```
tuna/
├── fft.py            # Fast Fourier Transform implementation
├── filtering.py      # Filtering functions (eg. noise gate)
├── pitch.py          # Pitch detection (estimating the fundamental frequency)
├── tonal.py          # Transformations between frequencies and notes
├── tuner.py          # Tuner class that provides the top level functionality
├── app.py            # CLI wrapper to the functionality provided by Tuner
```

For handling the audio input, the project uses the
[sounddevice](https://python-sounddevice.readthedocs.io/en/0.5.1/) library. The
library in turn uses the [PortAudio](https://www.portaudio.com/) system library
for interfacing with the audio hardware.

## Complexity analysis

The key algorithm in this project is the (radix-2) Cooley-Tukey FFT. It's a
divide-and-conquer algorithm that recursively breaks down a DFT of size $n =
2^k$ (for some $k \in \mathbb{N}$) into two smaller DFTs of sizes $\frac{n}{2}$,
recursively, until the base case of $n = 1$ is reached. The algorithm then
combines the results of the smaller DFTs to produce the final DFT. It's rather
easy to guess that the time complexity of the algorithm is $O(n \lg n)$. Since
formal proofs are beyond the scope of this document, we'll just leave it here.

Because one of the key aspects here is that FFT should be an efficient way of
computing the DFT, the project also implements the naive DFT for verification.
The naive DFT has a time complexity of $O(n^2)$, as can be easily seen from the
two nested $1..n$ for loops in its [implementation](/tuna/dft.py). It starts
to get quite slow on consumer hardware for even modestly sized inputs, like the
ones this project requires so that the necessary frequencies can be caught and
estimated with enough resolution.

Space complexity does not seem like a real concern from the perspective of this
project, because our design choices limit the It's worth noting that both the
naive DFT and the FFT are implemented in a way that they don't mutate the input,
so the space complexity is at least $O(n)$. For FFT, it's easy to see that the
space complexity is actually more like $O(n \lg n)$, since we have to store the
intermediate results of the recursive calls.

## Shortcomings and suggestions for improvement

The obvious shortcoming in this project is that the pitch detection algorithm is
quite naive. It is based on the assumption that the fundamental frequency will
have the highest magnitude in the fourier transform. This is not always the
case. Especially for string instruments like the guitar, the harmonic overtones
can very well have higher magnitudes than the fundamental frequency. This can
lead to so called octave errors, that this algorithm is prone to.

There are multiple pitch detection algorithms that could be used to improve the
accuracy. Probably the most notable would be the semi-recent YIN algorithm.
However, the point of this project was not to implement perfect pitch detection,
but rather to get a feel for the DSP domain by working with one of its hallmark
algorithms, the FFT.

## Usage of AI

While pondering the project setup, I used Google Gemini (and to a lesser
degree ChatGPT) to help me in wrapping my mind around the subject matter. DSP is
not something I've worked with before so the discussions were very helpful in
exploring the problem space.

# Tuna - A digital guitar tuner

This is a course project for the _Algorithms and Artificial Intelligence
Project_ at the University of Helsinki. The project consists of a digital guitar
tuner that can be used to tune a guitar using a computer. The tuner is
implemented in Python and uses Fast Fourier Transform (FFT) to analyze the sound
input from a microphone.

## Background

The problem explored in the project is essentially that of pitch detection. The
goal is to determine the _fundamental frequency_ of the sound input, which
corresponds to the pitch of the guitar string being played.

For simple waves like the sine wave, the fundamental frequency can be directly
identified from the frequency spectrum produced by the Discrete Fourier
Transform (DFT) of the waveform. This is because the signal consists of a single
frequency component, so the fundamental frequency is trivial to find from the
DFT, as exemplified in the following figure.

![sine](/docs/images/specification_files/specification_1_0.png)

For musical instruments though, the matter is a bit more complex. A vibrating
string produces a superposition of multiple frequencies, called _harmonics_,
which are integer multiples of the fundamental frequency. The fundamental
frequency is the lowest frequency in the spectrum, and it determines the pitch
of the sound. It commonly occurs though that one of these harmonic _overtones_
is actually stronger in intensity than the fundamental frequency.

![guitar](/docs/images/specification_files/specification_3_0.png)

To combat this issue, one stategy is to apply _cepstral analysis_. Notice how
the frequncy domain spikes above are evenly spaced? This is because the
harmonics of a frequency are integer multiples of the original frequency. The
intuition for finding the fundamental frequency with cepstral analysis is the
following. The cepstrum of a signal is the inverse Fourier transform of the
logarithm of the spectrum of the orignal signal. For harmonic signals like that
of a plucked guitar string, what results is a function that will have a peak at
the period that corresponds to the fundamental frequency of the original signal.

Obviously a signal can also have external elements that have an effect on the
frequency spectrum. This is why pitch detection is a non-trivial problem. These
external factors are mostly disregarded in this project, and instead a clean
enough signal is assumed.

## Approach

There are many different algorithms and techniques that can be used for pitch
detection, but this project will specifically focus on cepstral analysis. The
project will implement the Cooley-Tukey FFT algorithm to efficiently compute
both the DFT and its inverse. Cepstral analysis is then applied to extract the
fundamental frequency from the spectrum. Inspiration for implementing the
Cooley-Tukey FFT algorithm will likely be derived from the material presented by
Cormen et. al. (2009). In addition, some very simple filtering, like a noise
gate, may be applied to the input signal, but this is mostly for the usability
of the tuner.

The tuner listens to sound input from a microphone, and processes the signal in
real-time. The user can play a guitar string, and the tuner will display the
detected pitch of the string. The user can then adjust the tuning of the string
to match the desired pitch. In practice, the signal does not have to come from a
guitar, it just has to be within the typical frequency range of a guitar string.
This means that the tuner can be used to detect the pitch of one humming into
their microphone, for example.

The motivation for this being a _guitar_ tuner is first and foremost a personal
interest. It also provides a clear and practical application for the pitch
detection algorithm. This restriction also allows us to make some assumptions
about the input signal, which simplifies the problem. For example, the input
signal can be assumed to be harmonic and within a certain frequency range. And
because the desired frequency range impacts the required sampling rate, and the
typical frequency range of a guitar string is known, the sampling rate can be
optimized for this specific use case. This way runtime computational cost of the
algorithm can be minimized.

Perfomance-wise, this project would benefit from a more performance-oriented
implementation language, but Python is chosen for its simplicity and ease of
use, as well as for the existence of easy-to-use libraries for reading a
microphone. Because FFT reduces the time complexity of the DFT from `O(n^2)` to
`O(n log n)`, the algorithm is quite efficient and so the performance will
likely be adequate. If it turns out slow, we can just sample the input signal at
a lower rate, trading off some accuracy for speed and responsiveness.

The project will focus heavily on the implementation of the pitch detection
algorithm, and the user interface will be kept simple. The user interface will
first be built as a command-line interface, and a graphical user interface may
be added later if time permits.

## Notes for the course

- Course implementation: Algorithms and Artificial Intelligence Project, teaching period I, 2024.
- Degree programme: BsC Computer Science (Tietojenkäsittelytieteen kandidaatti).
- Language of documentation: English.
- I can review stuff written in at least Python, JavaScript/TypeScript, C++, and Java.

## References

- [Vibration (Wikipedia)](https://en.wikipedia.org/wiki/Vibration)
- [Pitch (music) (Wikipeda)](<https://en.wikipedia.org/wiki/Pitch_(music)>)
- [Pitch detection algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Pitch_detection_algorithm)
- [Noise gate (Wikipedia)](https://en.wikipedia.org/wiki/Noise_gate)
- [Cooley-Tukey FFT algorithm (Wikipedia)](https://en.wikipedia.org/wiki/Cooley%E2%80%93Tukey_FFT_algorithm)
- Gerhard, D. (2003). _Pitch extraction and fundamental frequency: History and
  current techniques_ (pp. 0-22). Regina, Canada: Department of Computer
  Science, University of Regina.
- Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2009).
  _Introduction to algorithms_. (3rd ed.). MIT press.

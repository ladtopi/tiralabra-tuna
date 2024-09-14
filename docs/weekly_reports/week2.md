# Report for week 2

This week I jumped in and started the implementation work. So far I have seem to
have a working FFT implementation! Obviously some issues may be lurking, but I
have have a fair confidence. Since the textbook definition of a discrete Fourier
transform is rather simple, I decided to implement a naive dft function as well
directly from the definition. It's easier to gain confidence that the simple
function is working, and it can be used to cross verify that the FFT function
gives the same output. I also plan to later use it for performance testing.

I also started to work on the actual pitch detection. I have a very simple pitch
detector in place, that works for a _very_ simple input, but really it's just a
frame and is not correct in the general case. Work remains to be done here, but
I think I'm in a pretty good position.

Next week I will continue on the pitch detection. I will also probably build a
very simple command line interface to the tuner.

Hours used: ~8h (course total 28h).

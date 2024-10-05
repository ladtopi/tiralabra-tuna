# Report for week 4

I spent this week on improving the existing functionality and structure. The
command line application now outputs the detected pitch in musical notation
(along with the delta to the note) instead of raw frequencies. The source code
is also now more cleanly organized.

I tried to improve the pitch detection using cepstral analysis, but really the
results with the simple existing method seemed so promising that I decided to
drop the cepstral analysis altogether. The essence of the project would be the
same irregardless - using FFT to estimate the fundamental frequency.

In addition to these, I explored the possibility of implementing a nice and
simple GUI for the app, but I'm not sure if it's worth the effort. The simplest
frameworks are probably not going to support the types of UI components I would
like to use, and the more complex ones may just derail my focus from the
essential. I will likely stick with the CLI for now.

Next week I will likely focus on making the top end of the app cleaner (the app
module) and continue working on the documentation, as well as perform the first
peer reviews.

Hours used: ~8h (course total 41h).

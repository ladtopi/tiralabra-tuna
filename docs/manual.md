# User manual

The application is rather simple. It's a command line application that begins
listening to microphone input as soon as it's started, read the input in frames
(of about 250ms) and then outputs the estimated pitch of the input. The pitch is
output in musical notation (eg. `A4` for the A above middle C), with the
distance to this nearest note also output in Hz.

**NOTE**: the application will select the microphone based on the default input
device, so make sure that the correct microphone is selected in your system
settings.

TODO: full installation and usage instructions

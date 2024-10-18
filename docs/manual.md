# User manual

The application is rather simple. It's a command line application that begins
listening to microphone input as soon as it's started, read the input in frames
(of about 250ms) and then outputs the estimated pitch of the input. The pitch is
output in musical notation (eg. `A4` for the A above middle C), with the
distance to this nearest note also output in Hz.

Do note that the pitch detection algorithm is rather simple, so especially
octave errors are expected. The note base should however generally be quite
correct, given a clean enough input signal.

## Installation

If you don't have Poetry installed, make sure to install it first. You can find
instructions on how to do this in the [Poetry documentation](https://python-poetry.org/docs/#installation).

After you have Poetry installed, you can install the project dependencies with:

```bash
poetry install
```

> [!IMPORTANT]
> This project relies on the [sounddevice](https://python-sounddevice.readthedocs.io/en/0.5.1/)
> library, which itself is a wrapper on [PortAudio](https://www.portaudio.com/). This
> means that you need to have PortAudio installed on your system. On Linux, this
> is not done automatically. The way to install it depends on the distribution.
> On Ubuntu you can install it with `sudo apt-get install portaudio19-dev`.

## Running

After installation you can start the application with:

```bash
poetry run inv start
```

You should now start seeing the periodically detected pitch in your terminal.
You can stop the application with `Ctrl+C`.

> [!NOTE]
> The application will select the microphone based on the default input device,
> so make sure that the correct microphone is selected in your system settings.

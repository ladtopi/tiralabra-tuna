"""
A simple CLI application wrapper around the Tuner.
"""

import sys

import sounddevice as sd

from tuna.tuner import Tuner

CLEAR = "\r\033[K"
FRAME_RATE = 1024


def select_input():
    """
    Runs the user through input device configuration.
    """
    devices, default = Tuner.list_inputs()
    print("Available input devices:")
    for did in devices:
        print(f"  - {devices[did]} ({did})")
    try:
        device = int(
            input(f"Select input device: ({default})\n").strip() or default)
        if device not in devices:
            raise ValueError("Invalid input device")
        return device
    except ValueError:
        print("The input needs to be an integer")
        sys.exit(1)
    except KeyboardInterrupt:
        print("")
        print("Cancelled")
        sys.exit(1)


def main():
    def out_replace(msg):
        """
        Output the message to the console. Replaces the previous message.
        """
        print(CLEAR + msg, end="")

    def output_pitch(pitch=None):
        if not pitch:
            out_replace("No pitch detected")
        else:
            out_replace(f"Detected pitch: {pitch[0]} ({pitch[1]:.2f}Hz)")

    def print_error(status: sd.CallbackFlags):
        print(f"\nError: {status}", file=sys.stderr)

    def on_tuner_ready():
        print("Listening to the microphone...")
        print("Press Ctrl+C to exit.")

    device = None

    if '-s' in sys.argv or '--select-input' in sys.argv:
        device = select_input()

    tuner = Tuner(frame_rate=FRAME_RATE,
                  pitch_callback=output_pitch,
                  err_callback=print_error,
                  input_device=device)

    try:
        tuner.start(ready_callback=on_tuner_ready)
    except KeyboardInterrupt:
        tuner.stop()
        print("")
        print("Goodbye!")


if __name__ == "__main__":
    main()

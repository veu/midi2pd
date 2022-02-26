# Playdate MIDI input example

This is a simple example for getting MIDI input into the Playdate simulator in macOS. The code should run on other systems as well but I didn’t test it.

The main idea is to read the MIDI input in Python and write the currently active notes into a file accessible to the Playdata simulator.

## Setup

To run this example in the Playdate simulator on macOS:

1. install the Playdate SDK,
2. connect your midi device,
3. run the following commands to start the converter, and

	```bash
	pip3 install pygame
	python3 midi2pd.py ~/Developer/PlaydateSDK/Disk/Data/midi2pd
	```

4. compile and run the `main.lua` in your simulator.

If you have multiple MIDI input devices you can select which one to use by adding another 	parameter to the converter, e.g.

```bash
python3 midi2pd.py ~/Developer/PlaydateSDK/Disk/Data/synth 0
```

A list of connected devices will be shown when running `midi2pd.py`.

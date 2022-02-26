import sys
import os
import json

import pygame
import pygame.midi

class MIDIInput():
	def __enter__(self):
		pygame.init()
		pygame.midi.init()
		self._print_device_info()

		if device_id is None:
			input_id = pygame.midi.get_default_input_id()
		else:
			input_id = device_id

		print("using input_id :%s:" % input_id)
		return pygame.midi.Input(input_id)

	def __exit__(self, type, value, traceback):
		pygame.midi.quit()
		pygame.quit()

	def _print_device_info(self):
		for i in range(pygame.midi.get_count()):
			r = pygame.midi.get_device_info(i)
			(interf, name, input, output, opened) = r

			in_out = ""
			if input:
				in_out = "(input)"
			if output:
				in_out = "(output)"

			print(
				"%2i: interface :%s:, name :%s:, opened :%s:  %s"
				% (i, interf, name, opened, in_out)
		)

if __name__ == "__main__":
	data_file = os.path.join(sys.argv[1], 'midi.json')
	try:
		device_id = int(sys.argv[-1])
	except ValueError:
		device_id = None

	notes = {}

	with MIDIInput() as input:
		while True:
			if input.poll():
				midis = input.read(10)
				events = pygame.midi.midis2events(midis, input.device_id)
				for event in events:
					print(event)
					if event.status == 144:
						note, volume = event.data1, event.data2
						if volume > 0:
							notes[note] = volume
						elif note in notes:
							del notes[note]

				with open(data_file, 'w') as outfile:
					json.dump(notes, outfile)

MIDI_PORT=""
DMX_PORT="/dev/ttyUSB0"
CONFIG="works.json"

run:
	@vmpk &
	@python3 ./midils/midils.py run $(MIDI_PORT) $(DMX_PORT) $(CONFIG)

list:
	@python3 ./midils/midils.py list


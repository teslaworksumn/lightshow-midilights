#!/usr/bin/env python3
import os
import mido
from IoThread import IoThread
from plugins import Dmx as OutDmx
from plugins import Log as OutLog
import mapper

channel_outputs = []


def main():
    dmx = OutDmx()
    vixenlog = OutLog()
    channel_values = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    mapping = mapper.get_mapping(dir_path + '/mapping.json')

    # Keyboard velocities are in range [1, 120]
    # Outputs are in range [0, 255]
    # This function roughly maps the first to the second
    def velocity_to_output(velocity):
        return (velocity - 1) * 2 + 1

    try:
        # Setup midi input
        backend_portmidi = mido.Backend('mido.backends.portmidi')
        inputs = backend_portmidi.get_input_names()
        print(inputs)
        # Start listening for midi
        input_thread = IoThread(inputs[0], vixenlog, channel_values, backend_portmidi)
        input_thread.start()
        # Wait until user exits
        print("Enter 'exit' to stop the program")
        while input("Command: ") != 'exit':
            pass
        # Cleanup
        input_thread.stop()
    except Exception as e:
        print(e)

main()

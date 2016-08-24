#!/usr/bin/env python3
import os
import mido
from IoThread import IoThread
from plugins import Dmx as OutDmx
from plugins import Log as OutLog
from mapper import Mapper

channel_outputs = []


def main():
    dmx = OutDmx()
    vixenlog = OutLog()
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = dir_path + '/mapping.json'
    mapper = Mapper(config_path)

    try:
        # Setup midi input
        backend_portmidi = mido.Backend('mido.backends.portmidi')
        inputs = backend_portmidi.get_input_names()
        print(inputs)
        # Start listening for midi
        input_thread = IoThread(backend_portmidi, inputs[0], vixenlog, mapper)
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

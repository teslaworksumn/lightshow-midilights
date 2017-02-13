#!/usr/bin/env python3
import os
import mido
from docopt import docopt
from IoThread import IoThread
from mapper import Mapper
from plugins import Dmx as OutDmx
from plugins import Log as OutLog


help_text = """MIDI Lightshow.

Usage:
    midils.py list [<backend>]
    midils.py run <midi-input> <dmx> <config> [<backend>]
    midils.py run (-d || --dry) <midi-input> <config> [<backend>]

Options:
    <backend>   Mido backend to use [default: 'mido.backends.portmidi']
    <config>    Path to output configuration file
    <dmx>       Path to dmx output device (/dev/ttyUSB* on Unix, COM* on Windows)
    -d, --dry   Dry run (output to logger)
    -h --help   Show this text
    --version   Show version

"""

channel_outputs = []


def main():
    # Parse arguments
    arguments = docopt(help_text)
    
    backend = mido.Backend(arguments['<backend>'])

    if (arguments['list']):
        inputs = backend.get_input_names()
        print(inputs)
    elif (arguments['run']):
        input_name = arguments['<midi-input>']
        mapper = get_mapper(arguments)
        (out_fn, cleanup_fn) = get_run_type_functions(arguments)

        run(input_name, mapper, backend, out_fn, cleanup_fn)
    else:
        print("How did we get here?? (docopt failed us or command not accounted for)")


# Runs midi-lightshow with a light channel mapper, a mido backend, a
# unary function to handle output, and a zero-ary function to do any necessary cleanup
def run(input_name, mapper, mido_backend, out_fn, cleanup_fn):
    try:
        # Start listening for midi
        input_thread = IoThread(mido_backend, input_name, out_fn, mapper)
        input_thread.start()
        # Wait until user exits
        print("Enter 'exit' to stop the program")
        while input("Command: ") != 'exit':
            pass
        # Cleanup
        input_thread.stop()
        cleanup_fn()
    except Exception as e:
        print(e)


# Returns the output function and cleanup function associated with the run type,
# which is determined by the user provided arguments. Dry run uses a logger,
# normal run uses a DMX output plugin
def get_run_type_functions(arguments):
    if arguments['--dry']:
        vixenlog = OutLog()
        out_fn = vixenlog.send
        cleanup_fn = lambda: None # No cleanup needed
    else:
        dmx = OutDmx()
        dmx_port = arguments['<dmx>']
        dmx.setPort(dmx_port)
        dmx.connect()
        # DMX is 1-indexed
        out_fn = lambda channels: dmx.sendDMX([ch + 1 for ch in channels])
        cleanup_fn = dmx.disconnect

    return (out_fn, cleanup_fn)


# Gets the output mapper from the user provided config file. Checks if path to said
# config file exists as well. Returns the mapper if everything worked, None if problem/not found
def get_mapper(arguments):
    config_file = arguments['<config>']
    dir_path = os.path.dirname(os.path.realpath(__file__))
    config_path = dir_path + '/configs/' + config_file
    mapper = Mapper(config_path)
    return mapper


if __name__ == '__main__':
    main()

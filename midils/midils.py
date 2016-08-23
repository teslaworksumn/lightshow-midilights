import mido
from InputThread import InputThread
from plugins import Dmx as OutDmx
from plugins import Log as OutLog

dmx = OutDmx()
vixenlog = OutLog()

def handle_message(message):
    print("Message:", message)
    vixenlog.send([255])

try:
    backend_portmidi = mido.Backend('mido.backends.portmidi')
    inputs = backend_portmidi.get_input_names()
    print(inputs)
    input_thread = InputThread(inputs[0], handle_message, backend_portmidi)
    input_thread.start()
    print("Enter 'exit' to stop the program")
    while input("Command: ") != 'exit':
        pass
    input_thread.stop()
except Exception as e:
    print(e)

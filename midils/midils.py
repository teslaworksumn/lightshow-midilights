import mido

def handle_message(message):
    print("Message:", message)

try:
    portmidi = mido.Backend('mido.backends.portmidi')
    inputs = portmidi.get_input_names()
    print(inputs)
    keyboard_in = portmidi.open_input(inputs[0], callback=handle_message)
    print("Enter 'exit' to stop the program")
    while input("Command: ") != 'stop':
        pass
except Exception as e:
    print(e)

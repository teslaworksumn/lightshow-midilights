import threading
import time


class IoThread:
    def __init__(self, name, output, channel_values, backend):
        self._name = name
        self._output = output
        self._mido_backend = backend
        self._channel_values = channel_values
        self._stop = threading.Event()

        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.setName("midils input thread for {0}".format(self._name))

    def start(self):
        self._stop.clear()
        self._thread.start()

    def stop(self):
        self._stop.set()

    def _handle_message(self, message):
        if message.type == 'note_on':
            print("Message:", message)
        elif message.type == 'note_off':
            pass

    def _run(self):
        self._mido_backend.open_input(self._name, callback=self._handle_message)
        while not self._stop.is_set():
            self._output.write(self._channel_values)
            time.sleep(0.010)

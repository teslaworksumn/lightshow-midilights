import threading
import time


class InputThread:
    def __init__(self, name, callback, backend):
        self._name = name
        self._callback = callback
        self._stop = threading.Event()
        self._mido_backend = backend

        self._thread = threading.Thread(target=self._run)
        self._thread.daemon = True
        self._thread.setName("midils input thread for {0}".format(self._name))

    def start(self):
        self._stop.clear()
        self._thread.start()

    def stop(self):
        self._stop.set()

    def _run(self):
        self._mido_backend.open_input(self._name, callback=self._callback)
        while not self._stop.is_set():
            time.sleep(0.5)

import threading
import time
import sys


class IoThread:
    def __init__(self, backend, name, output_func, mapper=None):
        self._mido_backend = backend
        self._name = name
        self._output_func = output_func
        self._mapper = mapper
        self._channel_values = []
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
        """Updates channel values when a MIDI message is received"""
        value = 0
        if message.type == 'note_on':
            value = _velocity_to_output(message.velocity)

        if message.type in ['note_on', 'note_off']:
            channels = self._get_channels(message.note)
            if channels is None:
                sys.stdout.write("Note not mapped: {0}\033[K\n".format(message.note))
            else:
                for channel in channels:
                    self._modify_channel_value(channel, value)

    def _modify_channel_value(self, channel, value):
        """Updates the value of a channel, extending the underlying array of values as necessary"""
        num_ch = len(self._channel_values)
        if channel >= num_ch:
            diff = channel - num_ch + 1
            extension = [0] * diff
            self._channel_values.extend(extension)
        self._channel_values[channel] = value

    def _get_channels(self, note):
        """Maps the note to a set of output channels if a mapper exists.
        Returns None if mapping doesn't exist"""
        if self._mapper is None:
            return note
        return self._mapper.map(note)

    def _run(self):
        """Write the channel values to the output at set intervals until stopped"""
        self._mido_backend.open_input(self._name, callback=self._handle_message)
        while not self._stop.is_set():
            if len(self._channel_values) > 0:
                sys.stdout.write("\r{0}\033[K\r".format(self._channel_values))
                self._output_func(self._channel_values)
            time.sleep(0.01)


def _velocity_to_output(velocity):
    """Approximately maps keyboard velocity in range [1, 120]
    to output value in range [0, 255]"""
    return (velocity - 1) * 2 + 1

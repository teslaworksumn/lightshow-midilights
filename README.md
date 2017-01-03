# midi-lightshow

# Setting up (this was done on a Unix system. May be slightly different commands on Windows)
Clone the repository: `git clone git@github.com:teslaworksumn/midi-lightshow.git`
Setup submodules: `git submodule init && git submodule update`
Install dependencies (may need to be run as root/sudo): `python3 setup.py install`
Run: `make run`

## Notes
-This program currently uses the path /dev/ttyUSB0 for the DMX output. This can be changed in midils/midils.py, and will soon be a command line argument.
-The machine this runs on should either have portmidi installed, or should [set up a different backend](https://mido.readthedocs.io/en/latest/backends.html) (this will require a change in midils.py as well)
-The midi input chosen is the first one found by the backend. This has worked in the past, but may act inconsistently across different machines.

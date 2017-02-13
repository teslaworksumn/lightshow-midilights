# midi-lightshow

```
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
```

# Setting up (this was done on a Unix system. May be slightly different commands on Windows)  
Clone the repository: `git clone git@github.com:teslaworksumn/midi-lightshow.git`  
Setup submodules: `git submodule init && git submodule update`  
Install dependencies (may need to be run as root/sudo): `python3 setup.py install`  
If using the PortMidi backend (default), you must install PortMidi: `sudo apt install libportmidi-dev`  
Run: `make run`

-[Different mido backends] (https://mido.readthedocs.io/en/latest/backends.html) can be used  

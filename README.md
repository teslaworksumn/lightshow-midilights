# midilights

```
Usage:  
    midilights.py list [<backend>]  
    midilights.py run <midi-input> <dmx> <config> [<backend>]  
    midilights.py run (-d || --dry) <midi-input> <config> [<backend>]  

Options:  
    <backend>   Mido backend to use [default: 'mido.backends.portmidi']  
    <config>    Path to output configuration file  
    <dmx>       Path to dmx output device (/dev/ttyUSB* on Unix, COM* on Windows)  
    -d, --dry   Dry run (output to logger)  
    -h --help   Show this text  
    --version   Show version  
```

# Setting up (this was done on a Unix system. May be slightly different commands on Windows)  
Clone the repository: `git clone --recursive git@github.com:teslaworksumn/lightshow-midilights.git`  
Install dependencies (may need to be run as root/sudo): `pip3 install -r requirements.txt`  
If using the PortMidi backend (default), you must install PortMidi: `sudo apt install libportmidi-dev`  
Run: `make run`

-[Different mido backends] (https://mido.readthedocs.io/en/latest/backends.html) can be used  

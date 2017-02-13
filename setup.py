from setuptools import setup

setup(
    name='midi-lightshow',
    version='0.2.0',
    author='Ryan Fredlund',
    author_email='rfredlund13@gmail.com',
    packages=['midils'],
    url='https://github.com/teslaworksumn/midi-lightshow',
    license='LICENSE',
    description='Interface between a midi keyboard and some dmx-controlled lights',
    install_requires=['docopt', 'mido', 'pyserial']
)

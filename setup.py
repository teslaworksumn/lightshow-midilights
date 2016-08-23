from distutils.core import setup

setup(
    name='midi-lightshow',
    version='0.1.0',
    author='Ryan Fredlund',
    author_email='rfredlund13@gmail.com',
    packages=['midils'],
    url='https://github.com/bookdude13/midi-lightshow',
    license='LICENSE',
    description='Interface between a midi keyboard and some dmx-controlled lights',
    install_requires=['mido']
)

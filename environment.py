"""
prepare an environment for multitrack mastering
create a console with 8 channels
each channel maps one bit from a byte via its assigned track

for every sequence of bits, setup the bit packets into wave packets
create colums for each channel dimensions representing each bit in the byte
pack the stream into a data tensor and render main output

store the rendered track into a stereo wave file
use the amplitudes from the master to guide program permutations
label the computations with the state transformations applied

use the rendered stereo file as a new environment
fit a function for setting up basis state description
"""

from signal import Console, Buffer, Clone

class Environment:
    def __init__(self, k):
        self.main = Console(k)
        self.state = Buffer(k)

    def __setitem__(self, level, start, stop, amplitude):
        self.state[level][start : stop] = amplitude

    def __getitem__(self, level, start, stop):
        return self.state[level][start : stop]

    def __call__(self, length, program):
        yield program.prepare(self.main.process(length))

    def store_graph(self, path):
        image = Clone(self)
        image.write(path)

    def load_graph(self, path):
        image = Clone(self)
        image.load(path)

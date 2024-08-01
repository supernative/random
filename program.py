"""
from signal import check, tell, encode, decode

class Program:
    def __init__(self, name):
        self.name = name
        self.track, self.length = check(name)

    def prepare(self, image):
        state = image.T @ self.track
        eigenstate = encode(state)
        return eigenstate

    def measure(self, state):
        eigenvector = decode(state)
        image = self.track + eigenvector
        return image

    def call(self, other):
        state = self.track @ other
        return state

    def store(self):
        tell(self.name, self.track, self.length)
"""
# NEW VERSION

"""
model description:

- a < x < b # open intervals in limit (0, 1)
- measure function : left elements , right elements >> rational choice, irrational choice
this happens by elected bodies (nodel?)

f(the programming, storage space, access points)
- holds code until storage is found
- creates access point with copy kept
- image is constructed

Note: the function (f) is said to be the HOST machine, which allows the programming.


(algorithm)

. start scanning local geometry
. every change encodes (l + r) -> (m, s)
.. m maps things that are centered around the origin
.. s maps things that are edged around the origin.
. compute the mass change at the current graph
. if change is negative, keep scanning more
. else, if greater, translate to the next point
.. else, if same, remain still.

graphs could be structured like so:

. every node is a mid point
. every edge is a side chain

a link is a map between two tracks in a stereo image.
. stereo image : left, right -> mid, side

node points are accessible via the linker
"""

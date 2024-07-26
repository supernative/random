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

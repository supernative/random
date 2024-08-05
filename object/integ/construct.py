import torch

memory = torch.load("memory.pt")

def pi(sequence):
    return sequence.permute(-1, 0, 1)

def union(function, image):
    unique, inverse_map = torch.unique(torch.tensor([[function, image]], return_inverses=True, sorted=True)
    return unique, inverse_map




def compute(memory):
    for state in memory:
        start = pi(state) # permutes the order
        stop = memory[start] # locally accessible information
        information, knowledge = union(start, stop) # locally inaccessible information and their reversible mapping
        yield information # information observable measurable from that state



def inner(left, right):
    mid = (left + right) / 2
    side = (left - right) / 2
    return mid, side

def outer(mid, side):
    left = mid + side
    right = mid - side
    return left, right

def inner_product(stereo):
    return inner(stereo[0]) * inner(stereo[1])

def outer_product(mono):
    return outer(mono[0]) * outer(mono[1])

"""
Inner product or dot product :
.. usually produce measure of similarity or dissimilarity between two vectors.
. we shall provide both similarity and difference per computation with `inner_product`.

Are difference/dissimilarity same?
.. difference is the gross computation of all mutually exclusive components.
. dissimilarity is the measure of like-ness and unlike-ness, not the specific quantities that are involved in the measure.
"""

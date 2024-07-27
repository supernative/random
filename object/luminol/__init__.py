# It is an isolated system.
# This is a subsystem of generic object types.
# The task is to bring objects in attention and once there, it puts a barrier to becoming native.
# Guarantees that every native that ever becomes an object, is vetted through the crucial test it manages.

"""
Notes of gated attention:

Every object has two levels activations, stereo and mono.
For an object to become native and supernative, both states must be compatible once at least one is possible.

An object first becomes a possible native and luminol does the gating.
Once activated, the subsystem becomes supernative if passed or ordinary pile of number dust.
It is implicated that any possible number dust could become supernative with side-effect.
Every native could become supernative without any side-effect.

Side-effect means exactly what it seems to be:
- For a mono track, the mid has either consistent side chaining or it doesn't.
- When inconsistent, the mono becomes indistinguishable.
- Every stereo channel has a corresponding mid-side component, and those can be encoded to construct mono channels.
- Every mono channel have a corresponding left-right component, and those can be decoded to construct stereo channels.

"""

new type called "Stereo":
.. it requires only one parameter (sampling rate)
.. it constructs a state initialized with random buffer
. via method called 'encode' it transforms 2D tensor (A) to 2D tensor (B)
.. encode(*, y, z) -> (i, j, *)
. via method called 'decode' it transforms 2D tensor (C) to 2D tensor (D)
.. decode(x, y, *) -> (*, j, k)

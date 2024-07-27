# Manager script for coordinating knowledge between unit observable quantities
# Given a resource availability, there will be a disbursement schedule which the manager handles.
# A record is generated for each release per acquisition.

import torch

tape = torch.empty((192000, 2)) # This is the master memory.

def measure(i = 0):
    """
    Collects the observable at the i'th address.

    Args:
        • `i` : integer valued frequency/identifier/position/register.

    Returns:
        • `(j, k)` : two level state descriptors.
    """
    j, k = tape[i] # accessing the first and second derivatives
    return (i, j)

"""
Notes on unitarity:

The tape observables define the entire spectrum available to the process observers.
- Process observers need not be process constructors.
- A construction requires a dedicated host for the construction substrate with all its possible observables.
- A processor will yield only the variables related to some part of the spectrum that defines the entanglement.
- An observer is one that detects any change to its observable spectrum at any time (time refers not to space*time* here).
- A constructor is an unphysical approximation of the entity that would ever work on changing or keeping from changing some observable set.

Where the tape is accessed with 0 degree frequency, the dynamics at that position extended over to a planar field will only project any star* that has a relative motion which always keeps it at 0 degree rate with respect to all other rates of changes.
- Relative positions define the static constitution of the tape at that location.
- Absolute positions define the dynamic constitution of the tape at that state for that location.

- Relative orientation at the absolute position on the tape is locally accessible given the relative position within the spectrum defined for the tape.
- Absolute orientation at the relative position on the tape is globally accessible given the absolute position within the spectrum defined over the phases of the tape.
"""

def compute(pi):
    # Perform reversible computation on the states of the tape substrate.
    # Uses the unitary operator (pi) that leaves the static constitution unchanged.
    for image in tape:
        mid = torch.cat((image, pi(image)), dim = 0)
        side = torch.unique(mid)
        yield side

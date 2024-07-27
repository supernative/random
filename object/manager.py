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

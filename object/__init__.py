# This is the main branch of all possible object systems
# The initial process includes 192k independently evolving columns
# Each process is unitary relative to at least one other process
# The object code defines the row dimensions.

from .manager import measure, compute
from .tape import device, driver

"""
Notes on two-level processors:

- measure function will provide observables at the given address
- observables have their own registers and they are not exclusive
- tape will replace those register variables whenever update is available
- each measure creates a temporary storage at runtime for each pair of observables

What is the difference between accessing object level information directly through their foundational addresses instead of accessing maps that maps to those in a reductionary principle?
If the reduction is upto the standard set by our own choosing, then it is not reduction after all but expansion though along different dimension.
All we need is a coorelating connections that however their forms may take would not destroy certain foundational knowledge.

One of two levels in a system that has at most a single descriptiong given some changes in its attributes:
- must correspond to possibility of mutation when a hosting population is stable
- must reflect change with respect to stable class of observers when a hosting population can mutate

Within the two levels, the description causes some other change via the constancy of interconnecting medium.
That medium may be an all inclusive feature that is self-supporting and it must then change only through finite means of travel.
Traveling requires both the mutable positional encoding and orienting attributes that each position can access whenever they agree in coordination.
Coordination must not involve all of observable quantities then, for it must leave the effects to translate through some transient property that the system keeps as such in order to detect changes.
Whenever there is a change and that can be adapted within the system via its adaptable set of orienting constitutions, it will inevitably do so and realize only half of those translated quantities.
However the half must reliably manage that realization, for the whole system to transform, it must use those half to arrange the other possible halves.
But the halving does not have to occur at any one line of slight (relative state vector), because there are redundant lines of sights that could assume twice or more uncertainity that could be reversed in due time, so long the system remains in existence at all.

"""

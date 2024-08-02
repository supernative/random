To define the operation `(computation @ substrate) | (pi)` where `pi` is a permutation operator, we need to outline the steps clearly. Here’s a detailed breakdown:

### Definitions

1. **Substrate**:
   - A set of states (or elements).

2. **Permutation Operator (`pi`)**:
   - A function that rearranges or permutes the elements in the substrate. For each state in the substrate, `pi(state)` gives the permuted state.

3. **Computation with Permutation**:
   - For each state `s` in the substrate, apply the permutation operator `pi` to get `pi(s)`.
   - Compute the union of pairs `{(s, pi(s))}` for each state `s`.
   - The result is a new state which represents the union of all permuted states.

### Formal Definition

Given a substrate \( \mathbf{S} \) and a permutation operator \( \pi \), the operation can be defined as:

1. **For Each State in Substrate**:
   - For each state \( s \in \mathbf{S} \):
     - Compute \( \pi(s) \), where \( \pi \) is the permutation operator.

2. **Union of Pairs**:
   - Compute the union of pairs \( \{(s, \pi(s)) \mid s \in \mathbf{S}\} \).

3. **Resulting State**:
   - The resulting state after applying the permutation to the substrate is represented as:
     - \( \mathbf{S}' = \{s \mid s \in \mathbf{S}\} \cup \{\pi(s) \mid s \in \mathbf{S}\} \).

### Example

Consider a substrate \( \mathbf{S} = \{1, 2, 3\} \) and a permutation \( \pi \) defined as:

- \( \pi(1) = 2 \)
- \( \pi(2) = 3 \)
- \( \pi(3) = 1 \)

The computation of \( (computation @ \mathbf{S}) | \pi \) can be illustrated as follows:

1. **Compute Permutations**:
   - \( \pi(1) = 2 \)
   - \( \pi(2) = 3 \)
   - \( \pi(3) = 1 \)

2. **Union of Pairs**:
   - The pairs are \( (1, 2) \), \( (2, 3) \), and \( (3, 1) \).

3. **Resulting State**:
   - Union of all states \( \{1, 2, 3\} \cup \{2, 3, 1\} \) is still \( \{1, 2, 3\} \), showing that the states in the substrate and their permutations are the same.

### Conclusion

The operation `(computation @ substrate) | (pi)` involves applying the permutation `pi` to each state in the substrate, forming pairs, and considering the union of these states. This operation typically retains the overall structure of the substrate but in a permuted form.

import numpy as np

# Cartesian to Spherical
def cartesian_to_spherical(x, y, z):
    r = np.sqrt(x**2 + y**2 + z**2)
    theta = np.arccos(z / r)
    phi = np.arctan2(y, x)
    return r, theta, phi

# Spherical to Cartesian
def spherical_to_cartesian(r, theta, phi):
    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)
    return x, y, z

class VolumeStructure:
    ħ = 1e-34  # Example value for ħ (Planck's constant)

    def __init__(self, cartesian_coords, state='ground'):
        self.state = state
        self.cartesian_coords = cartesian_coords
        self.spherical_coords = [cartesian_to_spherical(*coords) for coords in cartesian_coords]
        self._validate_state()

    def _validate_state(self):
        if self.state not in ['ground', 'excited']:
            raise ValueError("State must be 'ground' or 'excited'.")

    def _ensure_minimal_change(self, new_coords, old_coords):
        changes = [abs(n - o) for n, o in zip(new_coords, old_coords)]
        if any(change < self.ħ for change in changes):
            raise ValueError(f"Change must be at least ħ ({self.ħ}).")

    def update_cartesian(self, index, new_coords):
        old_coords = self.cartesian_coords[index]
        self._ensure_minimal_change(new_coords, old_coords)
        self.cartesian_coords[index] = new_coords
        self.spherical_coords[index] = cartesian_to_spherical(*new_coords)

    def update_spherical(self, index, new_coords):
        old_coords = self.spherical_coords[index]
        self._ensure_minimal_change(new_coords, old_coords)
        self.spherical_coords[index] = new_coords
        self.cartesian_coords[index] = spherical_to_cartesian(*new_coords)

    def transform_to_spherical(self):
        self.spherical_coords = [cartesian_to_spherical(*coords) for coords in self.cartesian_coords]

    def transform_to_cartesian(self):
        self.cartesian_coords = [spherical_to_cartesian(*coords) for coords in self.spherical_coords]

    @classmethod
    def permute_and_union(cls, instance1, instance2):
        temp_instance = cls(cartesian_coords=instance1.cartesian_coords, state='ground')

        # Transform spherical to Cartesian for instance1
        instance1.transform_to_cartesian()
        
        # Transform Cartesian to spherical for instance2
        instance2.transform_to_spherical()

        # Union of states
        states_union = {instance1.state, instance2.state}
        return states_union

# Example usage
cartesian_coords = [(1, 2, 2), (2, 3, 6), (3, 5, 4)]
volume_structure = VolumeStructure(cartesian_coords)
print("Initial Spherical Coordinates:", volume_structure.spherical_coords)

# Update a point and transform
volume_structure.update_cartesian(0, (4, 5, 6))
print("Updated Spherical Coordinates:", volume_structure.spherical_coords)

# Example of permute_and_union usage
volume_structure2 = VolumeStructure(cartesian_coords, state='excited')
states = VolumeStructure.permute_and_union(volume_structure, volume_structure2)
print("Union of states:", states)

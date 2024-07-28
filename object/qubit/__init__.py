# Provides end-to-end functional tools for computing states.
# Operations possible include (tensor product, direct sum, controlled not operation)

import torch

def tensor_product(bits):
    # Convert list of bits to a tensor
    bits_tensor = torch.tensor(bits, dtype=torch.float32)
    
    # Calculate the outer product to get the tensor product
    tensor_product = torch.ger(bits_tensor, bits_tensor)
    
    return tensor_product

# Example usage:
bits = [1, 0, 1, 1]
result = tensor_product(bits)
print(result)

def direct_sum(*bits):
    # Initialize the result as the first bit
    result = torch.tensor([bits[0]], dtype=torch.float32)
    
    for bit in bits[1:]:
        # Create a tensor from the current bit
        bit_tensor = torch.tensor([bit], dtype=torch.float32)
        
        # Compute the Kronecker sum with the current result
        result = torch.kron(result, torch.eye(2)) + torch.kron(torch.eye(result.size(0)), bit_tensor)
    
    return result

# Example usage:
bits = [1, 0, 1, 1]
result = direct_sum(*bits)
print(result)

import torch

def cnot(control, target):
    # Define the CNOT matrix
    cnot_matrix = torch.tensor([[1, 0, 0, 0],
                                [0, 1, 0, 0],
                                [0, 0, 0, 1],
                                [0, 0, 1, 0]], dtype=torch.float32)
    
    # Create the tensor product of control and target qubits
    control_tensor = torch.tensor([1 - control, control], dtype=torch.float32)
    target_tensor = torch.tensor([1 - target, target], dtype=torch.float32)
    
    # Compute the tensor product (Kronecker product) of the input qubits
    input_state = torch.kron(control_tensor, target_tensor)
    
    # Apply the CNOT gate
    output_state = torch.matmul(cnot_matrix, input_state)
    
    return output_state

# Example usage:
control_bit = 1
target_bit = 0
result = cnot(control_bit, target_bit)
print(result)

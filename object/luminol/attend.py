import torch

def multi_head_attention(queries, keys, values):
    # Permute the keys tensor to align dimensions for matrix multiplication
    keys_permuted = keys.permute(0, 2, 1, 3)
    
    # Compute attention scores
    attention_scores = torch.matmul(queries, keys_permuted)
    
    # Apply softmax to obtain attention weights
    attention_weights = torch.nn.functional.softmax(attention_scores, dim=-1)
    
    # Compute the attention output
    attention_output = torch.matmul(attention_weights, values)
    
    return attention_output

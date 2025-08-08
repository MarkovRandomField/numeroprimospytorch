import torch

def find_primes_pytorch(limit):
    """
    Finds all prime numbers up to a given limit using a PyTorch tensor.

    Args:
        limit (int): The maximum number to search for primes.

    Returns:
        list: A list of prime numbers.
    """
    # Create a boolean tensor initialized to True
    # If a CUDA device is available, move the tensor to the GPU for faster processing
    is_prime = torch.ones(limit + 1, dtype=torch.bool)
    
    # 0 and 1 are not prime
    is_prime[0] = is_prime[1] = False

    # Iterate from 2 up to the square root of the limit
    for num in range(2, int(torch.sqrt(torch.tensor(limit)).item()) + 1):
        if is_prime[num]:
            # Mark all multiples of the current prime as not prime
            # This is a key step where PyTorch's slicing and tensor operations
            # make the code concise and efficient.
            is_prime[num*num:limit+1:num] = False

    # Get the indices of the elements that are still True
    primes = torch.nonzero(is_prime).squeeze().tolist()
    
    return primes

# Define the limit
limit = 10000000

# Find the prime numbers
prime_numbers = find_primes_pytorch(limit)

# Print the results
print(f"There are {len(prime_numbers)} prime numbers up to {limit}.")
print(prime_numbers)

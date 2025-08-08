import torch
import time

def find_primes_pytorch(limit):
    """
    Encuentra todos los números primos hasta un límite dado usando
    un tensor de PyTorch.

    Args:
        limit (int): El número máximo hasta el que se buscarán los primos.

    Returns:
        list: Una lista de números primos.
    """
    is_prime = torch.ones(limit + 1, dtype=torch.bool)
    is_prime[0] = is_prime[1] = False

    for num in range(2, int(torch.sqrt(torch.tensor(limit)).item()) + 1):
        if is_prime[num]:
            is_prime[num*num:limit+1:num] = False

    primes = torch.nonzero(is_prime).squeeze().tolist()
    return primes

def print_blinking_primes(primes):
    """
    Imprime una lista de números primos parpadeando.

    Args:
        primes (list): La lista de números primos a imprimir.
    """
    # Código de escape ANSI para parpadear
    blinking_code = "\033[5m"
    # Código para resetear el formato
    reset_code = "\033[0m"

    blinking_primes_list = []
    
    for prime in primes:
        blinking_primes_list.append(f"{blinking_code}{prime}{reset_code}")
        
    print(" ".join(blinking_primes_list))

# Definir el límite
limit = 1000

# Encontrar los números primos
prime_numbers = find_primes_pytorch(limit)

# Imprimir los resultados
print(f"Hay {len(prime_numbers)} números primos hasta {limit}.")
print_blinking_primes(prime_numbers)

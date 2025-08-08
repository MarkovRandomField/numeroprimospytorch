import torch

def find_primes_pytorch(limit):
    """
    Encuentra todos los números primos hasta un límite dado usando
    un tensor de PyTorch.

    Args:
        limit (int): El número máximo hasta el que se buscarán los primos.

    Returns:
        list: Una lista de números primos.
    """
    # Crea un tensor booleano inicializado en True
    is_prime = torch.ones(limit + 1, dtype=torch.bool)
    
    # 0 y 1 no son primos
    is_prime[0] = is_prime[1] = False

    # Itera desde 2 hasta la raíz cuadrada del límite
    for num in range(2, int(torch.sqrt(torch.tensor(limit)).item()) + 1):
        if is_prime[num]:
            # Marca todos los múltiplos del número primo actual como no primos
            is_prime[num*num:limit+1:num] = False

    # Obtiene los índices de los elementos que siguen siendo True
    primes = torch.nonzero(is_prime).squeeze().tolist()
    
    return primes

def print_colored_primes(primes):
    """
    Imprime una lista de números primos usando diferentes colores.

    Args:
        primes (list): La lista de números primos a imprimir.
    """
    # Códigos de escape ANSI para diferentes colores de texto
    colors = [
        "\033[91m",  # Rojo
        "\033[92m",  # Verde
        "\033[93m",  # Amarillo
        "\033[94m",  # Azul
        "\033[95m",  # Magenta
        "\033[96m",  # Cian
    ]
    reset_color = "\033[0m" # Código para resetear el color

    colored_primes_list = []
    num_colors = len(colors)
    
    for i, prime in enumerate(primes):
        color = colors[i % num_colors]
        colored_primes_list.append(f"{color}{prime}{reset_color}")
        
    print(" ".join(colored_primes_list))

# Define el límite
limit = 10000

# Encuentra los números primos
prime_numbers = find_primes_pytorch(limit)

# Imprime los resultados
print(f"Hay {len(prime_numbers)} números primos hasta {limit}.")
print_colored_primes(prime_numbers)

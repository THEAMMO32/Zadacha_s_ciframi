def find_kth_digit(k):
    """
    Find the k-th digit in the infinite sequence 123456789101112...
    
    Args:
        k (int): Position of the digit (1-indexed)
    
    Returns:
        int: The digit at position k
    """
    if k <= 0:
        raise ValueError("k must be a positive integer")
    
    # Find which group of numbers (by digit count) contains position k
    digits = 1  # Current number of digits (1-digit, 2-digit, etc.)
    count = 9  # Count of numbers with 'digits' digits
    start = 1  # First number with 'digits' digits
    total_positions = 0  # Total positions covered so far
    
    # Determine which digit-length group contains position k
    while total_positions + digits * count < k:
        total_positions += digits * count
        digits += 1
        count *= 10
        start *= 10
    
    # Calculate which number within the group
    remaining = k - total_positions
    number_index = (remaining - 1) // digits
    digit_index = (remaining - 1) % digits
    
    # Find the actual number and extract the digit
    number = start + number_index
    digit = int(str(number)[digit_index])
    
    return digit


def main():
    """Main function to get user input and display result."""
    try:
        k = int(input("Введите позицию k: "))
        result = find_kth_digit(k)
        print(f"Цифра на позиции {k}: {result}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    main()

def is_narc(n): #Added a colon
    """Check if a number is narc."""

    num_str = str(n) # converted == to =
    num_digits = len(num_str) #Converted == to = 
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    #Removed one * 
    return sum_of_powers == n

def print_narcis_numbers(start, end): #Added a colon and a comma 
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #Added a colon
        if is_narc(num): #Added a colon at the end and changed is_narcissistic to is_narc
            print(num)
print_narcis_numbers(1000, 5000) #Changed the function call 

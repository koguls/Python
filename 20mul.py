def find_multiple_of_20(n):
    multiple = n
    while True:
        if multiple % 20 == 0:
            break
        multiple += 1
    return multiple

# Example usage
n = 20
result = find_multiple_of_20(n)
print(f"The smallest multiple of 20 greater than or equal to {n} is: {result}")     

  

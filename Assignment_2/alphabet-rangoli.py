import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    rows = []
    
    for i in range(size):
        s = '-'.join(alphabet[i:size])
        rows.append((s[::-1] + s[1:]).center(4*size-3, '-'))
    
    print('\n'.join(rows[::-1] + rows[1:]))

# Example usage:
size = int(input())
print_rangoli(size)

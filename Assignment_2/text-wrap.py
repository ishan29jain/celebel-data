import textwrap

def wrap(string, width):
    return textwrap.fill(string, width)

# Example usage:
string, width = input(), int(input())
print(wrap(string, width))

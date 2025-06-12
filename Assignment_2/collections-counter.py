from collections import Counter

def calculate_total(price, items):
    counter = Counter(items)
    total = sum(counter[item] * price[item] for item in counter)
    return total

n = int(input())
prices = list(map(int, input().split()))
items = list(map(int, input().split()))
print(calculate_total(prices, items))

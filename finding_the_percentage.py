n = int(input())
marks = {}

for _ in range(n):
    parts = input().split()
    marks[parts[0]] = list(map(float, parts[1:]))

query_name = input()
print(f"{sum(marks[query_name]) / 3:.2f}")

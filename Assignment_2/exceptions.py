try:
    x, y = map(int, input().split())
    print(x // y)
except ZeroDivisionError as e:
    print("Error Code:", e)
except ValueError as e:
    print("Error Code:", e)

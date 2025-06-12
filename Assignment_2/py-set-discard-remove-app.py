def set_operations():
    s = set(map(int, input().split()))
    n = int(input())
    
    for _ in range(n):
        operation = input().split()
        cmd = operation[0]
        num = int(operation[1]) if len(operation) > 1 else None
        
        if cmd == 'discard':
            s.discard(num)
        elif cmd == 'remove':
            try:
                s.remove(num)
            except KeyError:
                pass  
        elif cmd == 'pop':
            s.pop()
    
    print(sum(s))

set_operations()

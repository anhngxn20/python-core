def s(n):
    if n == 0:
        return 0
    else:
        return n + s(n - 1)
    
def decToBin(n):
    if n < 2:
        print(n, end='')
        return
    decToBin(n//2)
    print(n % 2, end='')
    
if __name__ == '__main__':
    n = 4
    print(s(4))
    decToBin(32)
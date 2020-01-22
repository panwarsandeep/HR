tr = {0:0,1:1}
def fibonacci(n):
    if tr.get(n) is not None:
        return tr.get(n)
    tr[n] = fibonacci(n-1)+fibonacci(n-2)
    return tr[n]

    # Write your code here.

n = int(raw_input())
print(fibonacci(n))

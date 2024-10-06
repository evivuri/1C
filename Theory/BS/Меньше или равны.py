def ans(n, k, a):
    a.sort()
    if k < n:
        return a[k - 1]
    else:
        return -1
n, k = map(int, input().split())
a = list(map(int, input().split()))
print(ans(n, k, a))
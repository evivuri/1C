def merge(a, b):
    c = []
    a_ind, b_ind = 0, 0
    while a_ind < len(a) and b_ind < len(b):
        if a[a_ind] < b[b_ind]:
            c.append(a[a_ind])
            a_ind += 1
        else:
            c.append(b[b_ind])
            b_ind += 1
    c += a[a_ind:]
    c += b[b_ind:]
    ans = *c, sep=" "
    return ans


def mergesort(l):
    if len(l) <= 1:
        return l
    m = len(l) // 2
    a = mergesort(l[:m])
    b = mergesort(l[m:])
    return merge(a, b)
n = int(input())
a = list(map(int, input().split()))
print(mergesort(a))

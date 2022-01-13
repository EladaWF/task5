# https://codeforces.com/problemset/problem/510/A
n, k = map(int, input().split())
for i in range(1, n+1):
    if (i % 2 != 0):
        for j in range(k):
            print('#', end='')
    elif ( i% 2 == 0 and i % 4 != 0):
        for j in range(k):
            if (j == k - 1):
                print('#', end='')
            else:
                print('.', end='')
    else:
        for j in range(k):
            if (j == 0):
                print('#', end='')
            else:
                print('.', end='')
    print()

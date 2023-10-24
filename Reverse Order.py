N = int(input())
list_1 = []
for i in range(N):
    M = input()
    list_1 += [M]
for i in range(N):
    print(list_1[N - i - 1])

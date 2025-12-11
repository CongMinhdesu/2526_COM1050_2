a = list(map(int,input().split()))
k = 0
for i in range (len(a)):
    if a[i]%2 == 0:
        k = k + a[i]
print(k)
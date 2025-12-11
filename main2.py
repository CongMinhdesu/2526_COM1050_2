n = int(input())
check = [2,3,5,7]
ans = []
while True:
    cnt = 0
    for i in range (len(check)):
        if n % check[i] == 0:
            n = n / check[i]
            cnt = cnt + 1
            ans.append(check[i])
    if cnt == 0:
        kkk = n
        break
for i in range (len(ans)):
        print(ans[i],end='x')
print (int(kkk))
        
    
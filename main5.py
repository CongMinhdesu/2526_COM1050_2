n =int(input())
cnt5=0
cnt2=0
cnt0=0
for i in range (1,n+1):
    if i % 10 == 5 :
        cnt5 = cnt5 + 1
    elif i % 10 == 2:
        cnt2 = cnt2 + 1
    elif i%10 == 0:
        cnt0 = cnt0 + 1
k = min(cnt5,cnt2)
print(k+cnt0)
n = int(input())
cnt = 0
while True:
    n = n / 1000
    if n < 1:
        break
    else:
        cnt = cnt + 1
    
print(cnt)
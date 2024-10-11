t=int(input())
for i in range (0,t):
    n,m=map(int,(input()).split())
    z=n-m
    if n-m>0:
        print(n-m)
    else:
        print("0")
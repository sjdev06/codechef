# cook your dish here
t=int(input())
for y in range (0,t):
    x,n= map(int, input().split())
    z=x//10
    print(z*n)
# cook your dish here
a,b,x,y=map(int,(input()).split())
if x>y:
    print(max(a,b))
else:
    print(min(a,b))
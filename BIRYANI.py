t=int(input())
for x, y in zip(range(0, t), range(0, t)):
    x,y=map(int,(input()).split())
    print(x * y)

#new to learn
#1 zip range is used to iterate two or more variables in a single for loop
#2 x,y input should be taken inside the for loop
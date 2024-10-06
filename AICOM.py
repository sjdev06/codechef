#My code 1
x=int(input("enter the difficulty level"))
if x>59:
    print("no")
else :
    print("yes")

    #MY CODE 2

X = int(input())

if X <= 60:
    print("YES")
else:
    print("NO")


#chat gpt code

x = list(map(int, input("Enter the difficulty levels (space-separated): ").split()))

# Process each difficulty level
for level in x:
    if level > 59:
        print("No")
    else:
        print("Yes")

t = int(input())
for i in range(0,t):
    x=int(input(""))
    if x>=2000:
        print("YES")
    else:
        print("NO")

#Why the Original Code Was Wrong:
#The for loop causes the check to repeat 4000 times, so if t >= 2000, "YES" is printed 4000 times.
#For competitive programming or input-output-based coding platforms, you want to avoid such unnecessary loops.
#This solution will now print the result only once.
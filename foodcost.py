
# MY code
x, y = map(int, input().split())
print(x*6+y)

#MY CODE (MODIFIED)
z=input()
z=z.split()
print(int(z[0])*6+int(z[1]))

#chatgpts code

input_str = input('mess charges (enter two values separated by space) = ')
# Split the input by space, and convert each part to an integer
x, y = map(int, input_str.split())
print("First charge:", x)
print("Second charge:", y)
print("the weekly foodcost is = ",x*6+y)

#problems encountered!
#Exception at line 2: ValueError with value invalid literal for int() with base 10: '100 500'
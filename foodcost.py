
# MY code
x=int(input('daily cost of mess food'))
y=int(input('sunday meals charges'))
print("the weekly cost of food is ",x*6+y)

#chatgpts code
input_str = input('mess charges (enter two values separated by space) = ')
# Split the input by space, and convert each part to an integer
x, y = map(int, input_str.split())
print("First charge:", x)
print("Second charge:", y)
print("the weekly foodcost is = ",x*6+y)

#problems encountered!
#Exception at line 2: ValueError with value invalid literal for int() with base 10: '100 500'
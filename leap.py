def is_leap():
    year = int(input())
    leap = False

    # Write your logic here
    if year % 4 == 0:
        if year % 400 == 0:
            print("this is a leap year")


    else:
        print("false")
    return leap

is_leap()
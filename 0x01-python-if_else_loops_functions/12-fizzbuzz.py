#!/usr/bin/python3
def fizzbuzz():
    txt = ""
    for num in range(1, 101):
        if(num % 3 == 0 and num % 5 != 0):
            txt = txt + "Fizz "
        elif(num % 3 != 0 and num % 5 == 0):
            txt = txt + "Buzz "
        elif(num % 3 == 0 and num % 5 == 0):
            txt = txt + "FizzBuzz "
        else:
            txt = txt + str(num) + " "
    print(txt.format(), end="")

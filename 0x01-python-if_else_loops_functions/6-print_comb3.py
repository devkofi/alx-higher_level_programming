#!/usr/bin/python3
text = ""
for value in range(0, 100):
    if(value < 10):
        text = text + f"0{value}, "
    elif(value == 99):
        text = text + f"{value}\n"
    else:
        text = text + f"{value}, "
print(text.format(), end="")

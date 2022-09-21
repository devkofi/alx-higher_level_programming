#!/usr/bin/python3
text = []
for value in range(100):
    if(value < 10):
        text.append(f"0{value}")
    else:
        text.append(f"{value}")
print(text, end="")

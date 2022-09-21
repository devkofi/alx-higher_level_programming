#!/usr/bin/python3
txt = ""
for alphabet in range(97, 123):
    if(alphabet % 2 != 0):
        txt += chr(alphabet - 32)
    else:
        txt += chr(alphabet)
print(txt[::-1].format(), end="")

#!/usr/bin/python3
def uppercase(text):
    txt = ""
    for char in text:
        asc = 0
        if(ord(char) > 90):
            asc = int(ord(char) - 32)
            txt = txt + f"{chr(asc)}"
        else:
            txt = txt + char
    print(txt.format())

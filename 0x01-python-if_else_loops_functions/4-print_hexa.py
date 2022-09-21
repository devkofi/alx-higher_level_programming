#!/usr/bin/python3
text = ""
for hex_value in range(0, 99):
    text = "{} = {}"
    print(text.format(hex_value, str(hex(hex_value))), end="\n")

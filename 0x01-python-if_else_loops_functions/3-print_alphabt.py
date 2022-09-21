#!/usr/bin/python3
text = ""
for alphabet in range(97, 123):
    if(alphabet == 101 or alphabet == 113):
        continue
    text = text + chr(alphabet)
print(str(text.format()), end="")

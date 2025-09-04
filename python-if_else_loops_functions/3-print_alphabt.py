#!/usr/bin/python3
i = 97
alphabet = ""
while i < 123:
    if i == ord('e') or i == ord('q'):
        i += 1
        continue
    alphabet = alphabet + chr(i)
    i += 1
print("{}".format(alphabet))

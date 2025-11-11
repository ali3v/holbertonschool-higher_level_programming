#!/usr/bin/python3
s = ''.join(chr(122-i).upper() if i % 2 else chr(122-i) 
            for i in range(26))
print("{}".format(s), end='')

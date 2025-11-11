#!/usr/bin/python3
print("{}".format(''.join(chr(c).upper() if i % 2 else chr(c) for i, c in enumerate(range(122, 96, -1)))), end='')

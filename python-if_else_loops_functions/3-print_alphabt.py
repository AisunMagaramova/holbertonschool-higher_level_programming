#!/usr/bin/python3
print("{}".format(
    "".join(chr(c) for c in range(97, 123) if chr(c) not in "qe")), end="")

import time
import os

spectrum = 'spectrum.luminol'

def print(string):
    with open(spectrum, 'a') as f:
        f.write("\n")
        f.write(string)

def while_true(condition):
    query = input("~ ")
    if query.strip() != condition:
        print("{} ~".format(query))
        while_true(condition)

print("<{}>".format(time.time()))
while_true("break")
print("<{}>".format(time.time()))

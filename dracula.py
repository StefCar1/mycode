#!/usr/bin/env python3

count= 0
with open("dracula.txt","r") as foo:
    for line in foo:
        if "vampire" in line:
            print(line.lower())
        if "vampire" in line.lower():
            count += 1
            print(count)

counter= 0

with open("dracula.txt","r") as foo:
    with open("vampytimex.txt","w") as fang:
        for line in foo:
            if "vampire" in line.lower():
                print(line)
                counter += 1
                fang.write(line)

print(counter)


#!/usr/bin/env python3
name = input("Please enter the file`s name: ")
fobj = open (name)
print(fobj.read())
fobj.close()


import socket
import json
import math

def floor(x):
    return math.floor(float(x))

def nroot(n, x):
    answer = x ** (1/n)
    if answer % 1 == 0:
        return int(answer)
    else:
        return answer

def reverse(s):
    return s[::-1]

def validAnagram(str1, str2):
    return sorted(str1) == sorted(str2)

def sort(*srt):
    return sorted(srt)

functions = {
    "floor": floor,
    "nroot": nroot,
    "reverse": reverse,
    "validAnagram": validAnagram,
    "sort": sort
}

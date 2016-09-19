#!/usr/bin/env python

import sys
import re
import io

hex = sys.argv[1].lower()
if re.match('^0?x?[a-f0-9]+$', hex) == None:
    print("The string {0} is not a hexadecimal number.".format(hex))
    exit(1)

def hex_digit_2_dec(hex_digit):
    hexs = [
            '0', '1', '2', '3', 
            '4', '5', '6', '7', 
            '8', '9', 'a', 'b', 
            'c', 'd', 'e', 'f']
    return hexs.index(hex_digit)

def hex_2_dec(hex):
    decimal = 0
    for digit in hex:
        decimal = decimal * 16 + hex_digit_2_dec(digit)
    return decimal 

if hex[0] == '0' and hex[1] == 'x':
    dec = hex_2_dec(hex[2:])
elif hex[0] == 'x':
    dec = hex_2_dec(hex[1:])
else:
    dec = hex_2_dec(hex)
print("Decimal {0}".format(dec))

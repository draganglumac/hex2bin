#!/usr/bin/env python

import sys
import re
import io

hex = sys.argv[1]
if re.match('0?x?[A-Fa-f0-9]+', hex) == None:
    print("The string {0} is not a hexadecimal number.".format(hex))
    exit(1)

def hex_digit_2_bin(hex_digit):
    hexs = [
            '0', '1', '2', '3', 
            '4', '5', '6', '7', 
            '8', '9', 'a', 'b', 
            'c', 'd', 'e', 'f']
    binaries = [
            '0000', '0001', '0010', '0011',
            '0100', '0101', '0110', '0111',
            '1000', '1001', '1010', '1011',
            '1100', '1101', '1110', '1111']
    return binaries[hexs.index(hex_digit)]

def hex_2_bin(hex):
    if len(hex) % 2 == 0:
        digits = hex
    else:
        digits = "0{0}".format(hex)
    
    binary = io.StringIO('')
    i = 1
    for digit in digits:
        binary.write(hex_digit_2_bin(digit))
        if i % 2 == 0:
            binary.write(' ')
        i += 1

    binary.seek(0)
    bin_value = binary.readline();
    binary.close()
    return bin_value

print("Binary {0}".format(hex_2_bin(hex[2:])))


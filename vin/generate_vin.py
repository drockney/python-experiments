"""Generate a random VIN. Validation logic taken from:
https://vin.dataonesoftware.com/vin_basics_blog/bid/112040/use-vin-validation-to-improve-inventory-quality
"""
import sys
import random

# Initialize the VIN array
vin = []

# String containing the output VIN
vin_output = ""

# A VIN is allowed to have letters or numbers, except
# for i, o, or q. Build a map that will correlate with
# these values in the array. First position is the character
# for the string, second is the check-digit value
valid_values = [["0",0], ["1",1], ["2",2], ["3",3], ["4",4],
                ["5",5], ["6",6], ["7",7], ["8",8], ["9",9],
                ["A",1], ["B",2], ["C",3], ["D",4], ["E",5],
                ["F",6], ["G",7], ["H",8], ["J",1], ["K",2],
                ["L",3], ["M",4], ["N",5], ["P",7], ["R",9],
                ["S",2], ["T",3], ["U",4], ["V",5], ["W",6],
                ["X",7], ["Y",8], ["Z",9]]
check_digit = 9
checksum = 0

# A VIN is 17 alphanumeric values. In the US and
# Canada, the 9th character is a special checksum.
# Generate 16 alphanumeric values
for digit in range(0, 16):
    vin.append(random.randrange(0,len(valid_values),1))

# Generate checksum value, which is the sum of all digits
# except the check digit, then modulo 11
for digit in range(0, len(vin)):
    if (digit != (check_digit - 1)):
        checksum += valid_values[vin[digit]][1]
checksum = checksum % 11

# Generate complete string
for digit in range(0, len(vin)):
    if (digit != (check_digit - 1)):
        vin_output+=valid_values[vin[digit]][0]
    else:
        if(checksum < 10):
            vin_output+=str(checksum)
        else:
            vin_output+="X"
print(vin_output)

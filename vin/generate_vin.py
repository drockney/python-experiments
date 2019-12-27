"""Generate a random VIN. Validation logic taken from:
https://vin.dataonesoftware.com/vin_basics_blog/bid/112040/use-vin-validation-to-improve-inventory-quality
"""
# TODO:
# * Set functions up to be externalizable so that they can be
#     added to, say, a VIN validator or VIN exploder
# * Make main() do something with parameters
import sys
import random
import csv

# A VIN is allowed to have letters or numbers, except
# for i, o, or q. Build a map that will correlate with
# these values in the array. First position is the character
# for the string, second is the check-digit value
def loadCsvList(fileName = '', delimiter = ','):
    with open(fileName) as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        linenum=0
        listName = []
        next(reader)
        for row in reader:
            listName.append(row)
    return(listName)

def generateChecksum(vin, checkDigit = 9):
    checksum = 0
    # Generate checksum value, which is the sum of all digits
    # except the check digit according to the validVinValues
    # table multiplied by the weightTable values for each position
    # in the VIN, then take modulo 11 of the whole mess
    validVinValues = loadCsvList('validVINvalues.csv')
    weightTable = loadCsvList('weightTable.csv')
    for digit in range(0, len(vin)):
        if (digit != (checkDigit - 1)):
            # Find the index for that particular digit in the validVinValues
            # table, then use it to pull its check value
            x = [x for x in validVinValues if vin[digit] in x][0]
            checksum += (int(x[1])*int(weightTable[digit][0]))
    # If the number is 0-9, leave it, otherwise replace it with an 'X'
    if((checksum % 11) < 10):
        vin[checkDigit - 1] = str(checksum % 11)
    else:
        vin[checkDigit - 1] = 'X'
    return(vin)

def randomizeArray(country = '', year = 0, make = ''):
    # A VIN is 17 alphanumeric values. In the US and
    # Canada, the 9th character is a special checksum.
    # Generate 16 alphanumeric values (17, but we will
    # throw the 9th away)
    validVinValues = loadCsvList('validVINvalues.csv')
    makeValues = loadCsvList('makes.csv', '|')
    yearValues = loadCsvList('YearChart.csv')
    vin = []
    # Let's make a random VIN
    for digit in range(0, 17):
        vin.append(validVinValues[random.randrange(0,len(validVinValues),1)][0])

    # Let's pick a random make, unless the user has specified one
    if (len(make) > 0):
        make = [x for x in makeValues if make in x][0][0]
    else:
        make = makeValues[random.randrange(0,len(makeValues),1)][0]
    for digit in range(0, (len(make))):
        vin[digit] = make[digit]
    # pick a random year, unless the user specified one
    if (year > 0):
        vin[9] = [x for x in yearValues if year in x][0][1]
    else:
        vin[9] = yearValues[random.randrange(0,len(yearValues),1)][1]
    # Create the checksum value
    vin = generateChecksum(vin)
    return(vin)

def validateVin(vin, country = '', year = 0, make = ''):
    checkedVin = generateChecksum(list(vin))
    if ("".join(vin) == "".join(checkedVin)):
        print("".join(vin),"has a valid checksum")
    else:
        print("".join(vin),"has an *invalid* checksum")

def main(country = '', year = 0, make = '', vin = []):
    # Did we receive a VIN? If so, we'll check it for
    # consistency. We'll also print make, country, and year.
    if (len(vin) > 0):
        validateVin(vin, country, year, make)
    else:
        # Some random value, unless country, 
        # make, and/or year is listed.
        vin = randomizeArray(country, year, make)
        print("".join(vin))

if __name__ == '__main__':
    main()

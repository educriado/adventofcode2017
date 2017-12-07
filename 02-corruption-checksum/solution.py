"""Eduardo Criado - Second challenge of Advent of Code. Calculating the checksum of a spreadsheet.
"""

def calculate_checksum(spreadsheet):
    """Calculates the checksum of a spreadsheet, which is the sum of every row's difference of its
    highest and lowest value."""
    checksum = 0
    for row in spreadsheet:
        for number in row:
            i = 0
            found = False
            while i < len(row) and not found:
                if row[i] != number and (row[i] % number == 0):
                    found = True
                    checksum += row[i] / number
                i += 1
    return checksum

def main():
    """Reads input from file, calculates checksum of spreadsheet and prints the result."""
    input_file_path = "input.txt"
    spreadsheet_file = open(input_file_path, "r")
    #Create list of lists
    spreadsheet = [[int(number) for number in row.split("\t")] for row in spreadsheet_file]
    print "The checksum of the spreadsheet is {}".format(calculate_checksum(spreadsheet))

if __name__ == '__main__':
    main()

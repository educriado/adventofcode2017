"""Eduardo Criado - Code for first challenge of Advent of Code 2017."""

def inverse_captcha(number):
    """Return the inverse captcha value depending on the received number."""
    return 0

def main():
    """Reads number from input file and prints result of inverse captcha."""
    input_file_path = "input.txt"
    f = open(input_file_path, "r")
    number = int(f.readline())
    result = inverse_captcha(number)
    print "The result using {} is {}".format(number, result)

if __name__ == "__main__":
    main()

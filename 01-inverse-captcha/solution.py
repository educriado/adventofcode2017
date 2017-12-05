"""Eduardo Criado - Code for first challenge of Advent of Code 2017."""

def inverse_captcha(num_list):
    """Return the inverse captcha value depending on the received digits."""
    i = 0
    result = 0
    while i < len(num_list):
        if num_list[i] == num_list[(i + (len(num_list) / 2)) % len(num_list)]:
            result += num_list[i]
        i += 1
    return result

def main():
    """Reads number from input file and prints result of inverse captcha."""
    input_file_path = "input.txt"
    num_file = open(input_file_path, "r")
    num = int(num_file.readline())
    #Turn num into array of digits
    num_list = [int(i) for i in str(num)]
    result = inverse_captcha(num_list)
    print "The result using {} is {}".format(num, result)

if __name__ == "__main__":
    main()

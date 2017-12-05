"""Eduardo Criado - Code for first challenge of Advent of Code 2017."""

def inverse_captcha(num_list):
    """Return the inverse captcha value depending on the received number."""
    i = 0
    result = 0
    while i < (len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            result += num_list[i]
        i += 1
    #Check the last element
    if num_list[0] == num_list[i]:
        result += num_list[i]
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

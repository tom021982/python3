# program to reverse a string

def reverseWords(input):
    inputWords = input.split(" ")
    inputWords = inputWords[-1::-1]
    output = (' ').join(inputWords)

    return output

if __name__ == "__main__":
    input = 'this is a test program'
    print(reverseWords(input))


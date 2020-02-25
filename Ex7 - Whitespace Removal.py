# Write a function remove_whitespace that removes extra whitespace (spaces, new line, tab)
# from the beginning and end of a string. You should implement the functionality on your own
# and not use system functions.


def remove_whitespace(string):
    whitespace = [' ', '\n', '\t']
    while True:
        if (string[0] not in whitespace) and (string[-1] not in whitespace):
            # if beginning and end of string are whitespace free -> process is complete
            return string
        if string[0] in whitespace:   # remove a whitespace char from beginning of string
            string = string[1:]
        if string[-1] in whitespace:  # remove a whitespace char from end of string
            string = string[:-1]

# After you’ve done that, find a system function that does this , and write a new function
# remove_whitespace_revised that uses the new function you’ve found


def remove_whitespace_revised(string):
    return string.strip()

string = '           \t    \n  a  b  \n c  d  \n  e'

print(remove_whitespace(string))  # debug output
print(remove_whitespace_revised(string))  # debug output

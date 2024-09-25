# formatted = "(123)456-7890"
# unformatted = "1234567890"
#
# start = input("Please enter your phone number: ")
#
# if start == unformatted:
#     print(formatted)
# elif start == formatted:
#     print("Looks like you already got it!")
# else:
#     print("Invalid number")


# These constants hold the lengths of formatted and unformatted phone numbers.
# Constants are in all caps.
FORMATTED_LENGTH = 13
UNFORMATTED_LENGTH = 10


valid = True  # Flag to indicate a valid format.
print("Please enter the telephone number.:In this format: (xxx)xxx-xxxx: ")
telephone = input()

# isFormatted = "unformatted"
# if len(telephone) == FORMATTED_LENGTH:
#     isFormatted = "formatted"
# elif len(telephone) != UNFORMATTED_LENGTH:
#     print("invalid format - changing to: 0123456789")
#     telephone = "0123456789"
#
# print("you entered:", telephone, "len=", len(telephone), "format:", isFormatted)

"""
   Determine if the number is properly formatted:  (703)123-4567
                                        indicies:  0123456789012
    len == FORMATTED_LENGTH
    '(' at offset 0
    ')' at offset 4
    '-' at offset 8
    => then convert to unformatted: 7031234567 using string slicing

   else assume it's unformatted: 7031234567
                       indicies: 0123456789
    => then convert to formatted 

"""

if len(telephone) == FORMATTED_LENGTH and telephone[0] == '(' and telephone[4] == ')' and telephone[8] == '-':
    telephone = telephone[1:4] + telephone [5:8] + telephone [9:]
else:
    telephone = '(' + telephone[0:3] + ')' + telephone[3:6] + '-' + telephone[6:10]
print(f"Yeah, that's {telephone}")
"""
slicing:  str[start:end]  start is inclusive, end is exclusive
     ex:  str = "hello there fred"
                 0123456789012345
                       -----
          str[6:11]  => "there"
"""

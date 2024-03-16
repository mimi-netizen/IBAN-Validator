# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

        '''line 03: ask the user to enter the IBAN (the number can contain spaces, as they significantly improve number readability...
line 04: ...but remove them immediately)
line 06: the entered IBAN must consist of digits and letters only – if it doesn't...
line 07: ...output the message;
line 08: the IBAN mustn't be shorter than 15 characters (this is the shortest variant, used in Norway)
line 09: if it is shorter, the user is informed;
line 10: moreover, the IBAN cannot be longer than 31 characters (this is the longest variant, used in Malta)
line 11: if it is longer, make an announcement;
line 12: start the actual processing;
line 13: move the four initial characters to the number's end, and convert all letters to upper case (step 02 of the algorithm)
line 14: this is the variable used to complete the number, created by replacing the letters with digits (according to the algorithm's step 03)
line 15: iterate through the IBAN;
line 16: if the character is a digit...
line 17: just copy it;
line 18: otherwise...
line 19: ...convert it into two digits (note the way it's done here)
line 20: the converted form of the IBAN is ready – make an integer out of it;
line 21: is the remainder of the division of iban2 by 97 equal to 1?
line 22: If yes, then success;
line 23: Otherwise...
line 24: ...the number is invalid.'''
    
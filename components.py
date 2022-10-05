# Checks if a string is a valid number in the specified base. Takes a string containing the input and a string containing the base ("bin", "dec", or "hex"). Throws a ValueError if the input is invalid and does nothing if it is valid.
def check_numstring(num: str, base: str):
    valid_digits = {
        "bin": ("0", "1"), # Valid digits for binary (base 2) numbers
        "dec": ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"), # Valid digits for decimal (base 10) numbers
        "hex": ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F") # Valid digits for hex (base 16) numbers
    }
    
    # Throw an error if the input is not a string
    if type(num) is not str:
        raise ValueError("numstring check requires input as a string but recieved it as " + str(type(num)))

    # Throw an error if the base is not a string
    if type(base) is not str:
        raise ValueError("numstring check requires base as a string but recieved it as " + str(type(base)))

    # Throw an error if the base is invalid
    if base not in ("bin", "dec", "hex"):
        raise ValueError("numstring check requires a base of hex/dec/bin but recieved " + str(base))
    
    # Prevents false negatives from hex numbers with lowercase characters.
    if base == "hex":
        num = num.upper()

    # Throw an error if the number contains any digits that are invalid for its base.
    is_valid = lambda char: char in valid_digits[base] # hehe lambda go brrrr
    checksum = [i for i in num if is_valid(i)] # Returns the input with any invalid digits removed
    if list(num) != checksum: # Only valid numbers will have identical checksums
        raise ValueError("numstring " + num + " in base " + base + " is invalid")
    
    return num

# Converts a hex (base 16) number to a decimal (base 10) number. Takes a string containing the hex number and returns a string containing the converted decimal number.
def hex_to_dec(num):
    num = check_numstring(num, "hex") # Ensure that the input is valid before continuing

    num = num[::-1] # Reverses the digit order, which is waaay easier than trying to loop backwards.

    dval = lambda d: "0123456789ABCDEF".index(d) # Converts a hex digit to its decimal value

    output = 0

    for i, d in enumerate(num):
        baseval = dval(d) # Find the base value of the digit
        trueval = baseval * (16 ** i) # Multiply the base value by 16 ^ [the digit's place in the number] to find its actual value
        output += trueval # Add the digit's value to the output

    return str(output)

# Converts a binary (base 2) number to a decimal (base 10) number. Takes a string containing the binary number and returns a string containing the converted decimal number.
def bin_to_dec(num):
    num = check_numstring(num, "bin") # Ensure that the input is valid before continuing

    num = num[::-1] # Reverses the digit order, which is waaay easier than trying to loop backwards.

    output = 0

    for i, d in enumerate(num):
        baseval = int(d) # Find the base value of the digit
        trueval = baseval * (2 ** i) # Multiply the base value by 2 ^ [the digit's place in the number] to find its actual value
        output += trueval # Add the digit's value to the output

    return str(output


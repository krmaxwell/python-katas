def ArabicNumeral(roman: str) -> int:
    """Convert a Roman numeral to an Arabic number"""

    if type(roman) != str:
        raise TypeError("Roman numeral must be a string")

    for char in roman:
        if char not in "IVXLCDM":
            raise ValueError(
                "Invalid character in input. Valid characters are I,V,X,L,C,D,M."
            )
    if len(roman) == 0:
        return 0

    if len(roman) == 1:
        if roman == "I":
            return 1
        elif roman == "X":
            return 10
        elif roman == "C":
            return 100
        elif roman == "M":
            return 1000
        elif roman == "V":
            return 5
        elif roman == "L":
            return 50
        elif roman == "D":
            return 500
        return 0

    if roman[0] == "V":
        if roman[1] != "I":
            raise ValueError("Invalid numeral: can't subtract auxiliary symbol.")
    if roman[0] == "L":
        if roman[1] == "C" or roman[1] == "M":
            raise ValueError("Invalid numeral: can't subtract auxiliary symbol.")

    # Only works for post-fixed smaller values
    if roman[0] == "I":
        if roman[1] == "V" or roman[1] == "X":
            return ArabicNumeral(roman[1:]) - 1
        return 1 + ArabicNumeral(roman[1:])
    elif roman[0] == "X":
        if roman[1] == "L" or roman[1] == "C":
            return ArabicNumeral(roman[1:]) - 10
        return 10 + ArabicNumeral(roman[1:])
    elif roman[0] == "C":
        if roman[1] == "D" or roman[1] == "M":
            return ArabicNumeral(roman[1:]) - 100
        return 100 + ArabicNumeral(roman[1:])

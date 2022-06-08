def ArabicNumeral(roman: str) -> int:
    """Convert a Roman numeral to an Arabic number"""

    conversion_values = {
        "I": 1,
        "X": 10,
        "C": 100,
        "M": 1000,
        "V": 5,
        "L": 50,
        "D": 500,
    }

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
        return conversion_values[roman]

    # check for consecutive subtraction
    if (conversion_values[roman[0]] < conversion_values[roman[1]]) and (
        conversion_values[roman[1]] < conversion_values[roman[2]]
    ):
        raise ValueError("Invalid numeral: two consecutive subtractions.")

    if roman[0] == "V" and roman[1] != "I":
        raise ValueError("Invalid numeral: can't subtract auxiliary symbol.")
    if roman[0] == "L" and (roman[1] == "C" or roman[1] == "M"):
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
    elif roman[0] == "L":
        return 50 + ArabicNumeral(roman[1:])

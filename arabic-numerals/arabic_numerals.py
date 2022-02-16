def ArabicNumeral(roman: str) -> int:
    """Convert a Roman numeral to an Arabic number"""
    if roman not in "IVXLCDM":
        raise ValueError(
            "Invalid character in input. Valid characters are I,V,X,L,C,D,M."
        )

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

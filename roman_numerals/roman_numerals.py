class RomanNumeral:
    def __init__(self, arabic: int):
        self.arabic = arabic

        self._numeral_map = {
            "ones": {1: "I", 5: "V", 10: "X"},
            "tens": {1: "X", 5: "L", 10: "C"},
            "hundreds": {1: "C", 5: "D", 10: "M"},
            "thousands": {1: "M"},
        }
        self._ones_digit = self.arabic % 10
        self._tens_digit = (self.arabic // 10) % 10
        self._hundreds_digit = (self.arabic // 100) % 10
        self._thousands_digit = (self.arabic // 1000) % 10
        self.numeral = (
            self._calc_digit("thousands", self._thousands_digit)
            + self._calc_digit("hundreds", self._hundreds_digit)
            + self._calc_digit("tens", self._tens_digit)
            + self._calc_digit("ones", self._ones_digit)
        )

    def _calc_digit(self, place: str, digit: int) -> str:
        if digit <= 3:
            return self._numeral_map[place][1] * digit
        elif digit == 4:
            return self._numeral_map[place][1] + self._numeral_map[place][5]
        elif digit == 9:
            return self._numeral_map[place][1] + self._numeral_map[place][10]
        else:
            return (
                self._numeral_map[place][5] + (digit - 5) * self._numeral_map[place][1]
            )

    def _triple_digit(self) -> str:
        digit = (self.arabic // 100) % 10
        if digit == 0:
            return ""
        elif digit <= 3:
            return "C" * digit
        elif digit == 4:
            return "CD"
        elif digit == 9:
            return "CM"
        else:
            return "D" + (digit - 5) * "C"

    def __str__(self) -> str:
        return self.numeral

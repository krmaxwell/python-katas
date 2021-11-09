def balance_check(input):
    # Returns True if the input string contained balanced pairs of parentheses
    # Otherwise returns False
    stack = []
    for char in input:
        if char in set("({["):
            stack.append(char)
        elif char in set(")}]"):
            try:
                last_char = stack.pop()
            except IndexError:
                return False
            if char == ")" and last_char != "(":
                return False
            if char == "}" and last_char != "{":
                return False
        else:
            return False
    return len(stack) == 0


if __name__ == "__main__":
    balance_check("()")

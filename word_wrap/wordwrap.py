def wrap(original_str: str, n: int) -> str:
    full_strings = []
    words = original_str.strip().split()
    current_line = ""
    for word in words:
        if len(current_line) == 0 and len(word) > n:
            full_strings.append(word[0:n])
            current_line = word[n:]
        elif len(current_line) + len(word) + 1 > n:
            full_strings.append(current_line.strip())
            current_line = word
        else:
            current_line += " " + word
    return "\n".join(full_strings + [current_line.strip()])
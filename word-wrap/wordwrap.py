def wrap(original_str, n):
    if len(original_str) <= n:
        return original_str
    return "\n".join(original_str.split())

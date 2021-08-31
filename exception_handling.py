# Doesn't handle exception
def unsafe_convert_to_number(var):
    return float(var)


# Handles exception
def safe_convert_to_number(var):
    try:
        return float(var)
    except ValueError:
        return None

print(unsafe_convert_to_number("foo"))
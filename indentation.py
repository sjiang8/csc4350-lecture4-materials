# quite nested!
def is_input_a_number_in_twenties_nested(input):
    if isinstance(input, (float, int)):
        if 20 <= input:
            if 30 > input:
                return True
    return False

# un-nested!
def is_input_a_number_in_twenties_unnested(input):
    if not isinstance(input, (float, int)):
        return False
    if 20 > input:
        return False
    if 30 <= input:
        return False
    return True
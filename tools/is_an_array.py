def is_an_array(input_data):
    if isinstance(input_data, list):
        return True
    else:
        raise TypeError(f"Input is not an array.\n{input_data}")

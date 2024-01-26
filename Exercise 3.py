def display_even_index_characters(input_str):
    # Use slicing with a step of 2 to get characters at even indices
    even_index_characters = input_str[::2]

    # Iterate through each character and print it
    for char in even_index_characters:
        print(char)


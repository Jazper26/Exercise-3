def display_even_index_characters(input_str):
    # Use slicing with a step of 2 to get characters at even indices
    even_index_characters = input_str[::2]

    # Iterate through each character and print it
    for char in even_index_characters:
        print(char)

# Accept a string from the user
user_input = input("Enter a string: ")

# Display characters at even index
display_even_index_characters(user_input)
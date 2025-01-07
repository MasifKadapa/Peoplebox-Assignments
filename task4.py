def snake_to_camel(snake_dict):
    camel_dict = {}
    for key, value in snake_dict.items():
        # Split the key by underscores, capitalize letters after the first word, and join them back
        camel_key = ''.join([word.capitalize() if i > 0 else word for i, word in enumerate(key.split('_'))])
        # Make the first character lowercase
        camel_dict[camel_key[0].lower() + camel_key[1:]] = value
    return camel_dict

# Example usage
snake_case_json = {
    "first_name": "John",
    "last_name": "Doe",
    "email_address": "john.doe@example.com"
}

camel_case_json = snake_to_camel(snake_case_json)
print(camel_case_json)

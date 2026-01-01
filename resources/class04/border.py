def print_with_border(text, border_char):
    border = border_char * 60
    print(border)
    print(text)
    print(border)


print_with_border("Hello, World!", '-')
print_with_border("Hello, World!", '*')
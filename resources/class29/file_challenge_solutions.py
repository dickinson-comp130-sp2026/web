def print_first_line():
    in_file = open('two-poems.txt')
    line = in_file.readline()
    print('The first line is: "' + line + '"')
    print('repr(line) is:', repr(line))
    print('line.strip() is: "' + line.strip() + '"')
    in_file.close()


def print_first_five_lines():
    in_file = open('two-poems.txt')
    for i in range(1, 6):
        line = in_file.readline().strip()
        print('line', i, ':', line)
    in_file.close()

def print_even_lines():
    in_file = open('two-poems.txt')
    line_num = 0
    for line in in_file:
        line_num = line_num + 1
        if line_num % 2 == 0:
            print(line.strip())

    in_file.close()

def write_even_lines():
    in_file = open('two-poems.txt')
    out_file = open('even-lines.txt', 'w')
    line_num = 0
    for line in in_file:
        line_num = line_num + 1
        if line_num % 2 == 0:
            out_file.write(line)

    in_file.close()


# print_first_line()
# print_first_five_lines()
print_even_lines()
write_even_lines()
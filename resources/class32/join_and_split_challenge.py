def print_csv_file(filename):
    input_file = open(filename)
    column_width = 30
    for line in input_file:
        # challenge 1: fix next line
        # data = line.strip().___________
        for i in range(len(data)):
            data[i] = data[i].ljust(column_width)
        # challenge 2: fix next line
        # print(_________________)
    input_file.close()


print_csv_file('courses.csv')

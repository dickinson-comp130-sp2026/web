def print_csv_file(filename):
    input_file = open(filename)
    column_width = 30
    for line in input_file:
        data = line.strip().split(',')
        for i in range(len(data)):
            data[i] = data[i].ljust(column_width)
        print(''.join(data))
    input_file.close()


print_csv_file('courses.csv')

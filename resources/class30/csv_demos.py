import random


# This function shows how to process a CSV file without using lists. Once we have
# learned about lists, there is a better way of doing this.
def print_enrollments():
    input_file = open('courses.csv')
    # Read and ignore the first line.
    line = input_file.readline()
    # Process all remaining lines, starting with the second line
    while True:
        line = input_file.readline().strip()
        if len(line) == 0:
            break
        # challenge: complete the next 4 lines
        # first_comma_index = line._______________
        # last_comma_index = line._____________
        # course = line[_________________]
        # enrollment = line[____________________]
        print('course', course, ': enrollment is', enrollment)
    input_file.close()


# This function shows how to process a CSV file using the split() method, which returns a
# list. Once we have studied lists, please use this technique for processing CSV files.
def print_enrollments_using_lists():
    input_file = open('courses.csv')
    # Read and ignore the first line.
    line = input_file.readline()
    # Process all remaining lines, starting with the second line
    while True:
        line = input_file.readline().strip()
        if len(line) == 0:
            break
        data = line.split(',')
        course = data[0]
        enrollment = data[-1]
        print('course', course, ': enrollment is', enrollment)
    input_file.close()

# Write 10 random sums into a CSV file
def write_random_sums():
    output_file = open('random_sums.csv', 'w')
    # write the CSV headers
    output_file.write('x,y,x+y\n')
    # write ten random sums
    for i in range(10):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        sum = x + y
        # challenge: complete the next line
        # output_file.write(______________________________)
    output_file.close()


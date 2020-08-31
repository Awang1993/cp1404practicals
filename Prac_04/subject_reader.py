"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"
subjects = []


def main():
    data = get_data()
    for part in subjects:
        print("{0:^6} is taught by {1:<12} and has {2:>3} students".format(part[0], part[1], part[2]))


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        parts[2] = int(parts[2])
        line = subjects.append(parts)
    input_file.close()
    return subjects


main()
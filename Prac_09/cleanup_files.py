"""
CP1404/CP5632 Practical
Demos of various os module examples
"""

import shutil
import os


def main():
    """Demo os module functions."""


    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Old')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    name = []

    for files in os.listdir('.'):
        if " " not in files:
            filenames = files.split('.')
            string = filenames[0]
            for character in enumerate(string):
                if character[0] == 0 or character[1].islower():
                    name.append(character[1])
                if character[1].isupper() and character[0] != 0:
                    name.append(" ")
                    name.append(character[1])
                filenames[0] = "".join(name)
            name.clear()
            new_file = filenames[0] + "." + filenames[1]
            # print(new_file)
            os.rename(files, new_file)
    for filename in os.listdir('.'):
        new_name = get_fixed_filename(filename)
        os.rename(filename, new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))



main()
# demo_walk()
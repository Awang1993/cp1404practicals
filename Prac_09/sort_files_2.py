"""
CP1404 - Practicals
Sort Files 2
"""

import os
import shutil


def main():
    """Main program for sorting files"""

    extensions = []
    directories = []

    os.chdir('FilesToSort')
    read_directory(extensions)

    # Grabs extension from list for sorting
    for extension in extensions:
        directory_name = input("Sort {} files into:".format(extension))
        # stores existing directories in a list to check if new one needs to be created
        if directory_name not in directories:
            os.mkdir(directory_name)
            directories.append(directory_name)
            # Scans current directory contents to see if there is a match, ignoring subdirectories
        for file in os.listdir('.'):
            filenames = file.split('.')
            if os.path.isdir(file):
                continue
            if extension == filenames[1]:
                shutil.move(file, directory_name)



def read_directory(extensions):
    """Reads current directories and stores new extensions in a list"""
    for file in os.listdir('.'):
        filenames = file.split('.')
        if os.path.isdir(file):
            continue
        if filenames[1] not in extensions:
            extensions.append(filenames[1])
    print(extensions)


main()

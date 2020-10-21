"""
CP1404 - Practicals
Sort Files 1
"""

import os
import shutil


def main():
    """Main program for sorting files"""
    extensions = []

    os.chdir('FilesToSort')

    print(os.listdir('.'))  # MARKER
    print(extensions)  # MARKER

    """Adds extension as a new item in the list if it does not exist"""
    for file in os.listdir('.'):
        filenames = file.split('.')
        if filenames[1] in extensions:
            continue
        else:
            extensions.append(filenames[1])

    create_directory(extensions)


def create_directory(extensions):
    """Create a directory for each item in the list"""
    for extension in extensions:
        os.mkdir(extension)


main()

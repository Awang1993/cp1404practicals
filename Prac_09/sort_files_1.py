"""
CP1404 - Practicals
Sort Files 1
"""

import os
import shutil


def main():
    """Main program for sorting files"""

    os.chdir('FilesToSort')

    # print(os.listdir('.'))  # MARKER
    # print(FILES)  # MARKER

    """Adds extension as a new item in the list if it does not exist"""
    for file in os.listdir('.'):
        filename = file.split('.')
        try:
            os.mkdir(filename[1])
        except FileExistsError:
            shutil.move(file, filename[1])
        except IndexError:
            continue


main()

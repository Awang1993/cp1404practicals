"""
CP1404 Practical
Programming Languages
"""

from Prac_06.programming_languages import ProgrammingLanguage


def main():
    """Intermediate Exercises"""
    LANGUAGES = []

    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    LANGUAGES.append(ruby)
    LANGUAGES.append(python)
    LANGUAGES.append(visual_basic)
    print(ruby.language_str())
    print(python.language_str())
    print(visual_basic.language_str())
    print("The dynamically typed languages are:")
    for language in LANGUAGES:
        if language.is_dynamic() == True:
            print(language.name)


main()
"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    while score <= 0 or score >= 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(score_check(score))


def score_check(score):
    if score < 50:
        return "Bad"
    elif score > 91:
        return "Excellent"
    else:
        return "Passable"


main()

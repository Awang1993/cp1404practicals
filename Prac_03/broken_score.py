"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    while score <= 0 or score >= 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print("You scored {:.0f}. Your mark was {}".format(score, score_check(score)))
    random_score = random.randint(0, 100)
    print("You scored {:.0f}. Your mark was {}".format(random_score, score_check(random_score)))


def score_check(number):
    if number < 50:
        return "Bad"
    elif number > 91:
        return "Excellent"
    else:
        return "Passable"


main()

"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """main function for processing scores"""
    score = float(input("Enter score: "))
    print(f"score: \n{return_score(score)}")


def return_score(score):
    """return result based on score provided in main"""
    if score < 0 or score > 100:
        return "invalid score"
    elif score >= 90:
        return "excellent"
    elif score >= 50:
        return "pass"
    elif score >= 0:
        return "fail"


main()

value = random.randint(0, 100)
print(f"\nthe random number is {value} which gives a score of: \n{return_score(value)}")

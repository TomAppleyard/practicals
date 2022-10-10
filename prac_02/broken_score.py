"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    """main function for processing scores"""
    score = float(input("Enter score: "))
    process_score(score)


def process_score(score):
    """print message depending on score provided in main"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("pass")
    elif score >= 0:
        print("fail")


main()

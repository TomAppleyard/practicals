""" Menu for different ways to process a score. """


def main():
    new_score = ""
    print("choose option:\nG: input score\nP: print result from score\nS: show stars from score\nQ: quit")
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            new_score = int(input("score: "))
        elif choice == "P":
            print(return_result(new_score))
        elif choice == "S":
            print(print_stars(new_score))
        print("choose option:\nG: input score\nP: print result from score\nS: show stars from score\nQ: quit")
        choice = input(">>> ").upper()
    print("さようなら")


def return_result(new_score):
    """ Return result based on score provided in main. """
    if new_score < 0 or new_score > 100:
        return "invalid score"
    elif new_score >= 90:
        return "excellent"
    elif new_score >= 50:
        return "pass"
    elif new_score >= 0:
        return "fail"


def print_stars(new_score):
    """ Print the score number as stars. """
    return "*" * new_score


main()

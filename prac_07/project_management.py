import datetime

from project_class import Project
from datetime import date


def main():
    menu_choice = input("Menu Choice: ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("choose file to load from: ")
            load_data(filename)
        elif menu_choice == "S":
            print("Save")

        elif menu_choice == "D":
            display_projects(projects)
            print("Display")

        elif menu_choice == "F":
            print("Filter")
        elif menu_choice == "A":
            print("Add")
        elif menu_choice == "U":
            print("Update")
        # else:
        #     # print("Incorrect menu choice")
    menu_choice = input("Menu Choice: ").upper()
    print("Thanks for coming")


main()


def load_data(filename):
    projects = []
    infile = open(filename, 'r')
    infile.readline()
    for line in infile:
        parts = line.strip().split("\t")
        date_string = parts[1]
        time = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        project = Project(parts[0], time, int(parts[2]), float(parts[3]), int(parts[4]))
        projects.append(project)
    return projects


def display_projects(projects):
    completed_projects = [project for project in projects if project.is_complete()]
    incomplete_projects = [project for project in projects if not project.is_complete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")

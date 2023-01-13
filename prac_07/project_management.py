import datetime

from project_class import Project


def main():
    menu_choice = input("Menu Choice: ").upper()
    projects = []
    while menu_choice != "Q":
        if menu_choice == "L":
            infile_name = input("choose file to load from: ")
            projects = load_data(infile_name)
            menu_choice = input("Menu Choice: ").upper()
        elif menu_choice == "S":
            outfile_name = input("choose file to save to: ")
            save_data(outfile_name, projects)
            print("Saved")
            menu_choice = input("Menu Choice: ").upper()
        elif menu_choice == "D":
            display_projects(projects)
            print("Display")
            menu_choice = input("Menu Choice: ").upper()
        elif menu_choice == "F":
            date_filter(projects)
            print("Filter")
            menu_choice = input("Menu Choice: ").upper()
        elif menu_choice == "A":
            add_project(projects)
            print("Add")
            menu_choice = input("Menu Choice: ").upper()
        elif menu_choice == "U":
            update_project(projects)
            print("Update")
            menu_choice = input("Menu Choice: ").upper()
        else:
            print("Incorrect menu choice")
    menu_choice = input("Menu Choice: ").upper()
    print("Thanks for coming")


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
    completed_projects = [project for project in projects if project.iscomplete()]
    incomplete_projects = [project for project in projects if not project.iscomplete()]
    print("Incomplete Projects: ")
    for project in incomplete_projects:
        print(f"\t{project}")
    print("Completed Projects: ")
    for project in completed_projects:
        print(f"\t{project}")


def save_data(outfile_name, projects):
    outfile = open(outfile_name, 'w')
    projects_string = '\t'.join(map(str, projects))
    print(projects_string)
    print(projects_string, file=outfile)
    outfile.write(projects_string)


def date_filter(projects):
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
    for project in projects:
        if project.start_date > date:
            print(project)


def add_project(projects):
    new_name = input("add project name: ")
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    new_start_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    new_priority = input("add project priority: ")
    new_estimate = input("add project estimate: ")
    new_completion = input("add project completion: ")
    new_project = Project(new_name, new_start_date, new_priority, new_estimate, new_completion)
    projects.append(new_project)


def update_project(projects):  # no time to add option to change priority
    project_number = 0
    for project in projects:
        project_number += 1
        print(f"{project_number}\t{project}")
    chosen_project = int(input("Choose project number: ")) - 1
    new_completion = int(input("How much is completed now?: "))
    new_priority = int(input("WHat is the new priority?: "))
    projects[chosen_project].change_completion(new_completion)
    projects[chosen_project].change_priority(new_priority)


main()

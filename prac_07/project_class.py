class Project:
    def __init__(self, name="", start_date="", priority=0, money_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.estimate = money_estimate
        self.completion = completion_percentage

    def __repr__(self):
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.estimate}," \
               f" completion: {self.completion}%"

    def iscomplete(self):
        return self.completion == 100

# filename = input("choose file to load from: ")
#             infile = open(filename, 'r')
#             projects = []
#             infile.readline()
#             # projects_data = [line.strip() for line in infile]
#             for project_data in projects_data:
#                 project = project_data.split('\t')
#                 projects.append(project)
#             for parts in projects:
#                 date_string = parts[1]
#                 date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
#             project = Project(parts[0], date, int(parts[2]), float(parts[3]), int(parts[4]))
#             print(projects)
#             menu_choice = input("Menu Choice: ").upper()

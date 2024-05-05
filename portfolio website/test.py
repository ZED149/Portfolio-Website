

from project import Project

pr = Project.load_projects_from_db()
pr = [i.get() for i in pr]
for index, p in enumerate(pr):
    if (index % 3) == 0:
        print(f"{index, p}")
import json

projects = json.load(open('projects.json'))


complete_projects = []
for project in projects:
    if 'cloc' in project:
        complete_projects.append(project)
        
json.dump(complete_projects, open('complete_projects.json', 'w'))


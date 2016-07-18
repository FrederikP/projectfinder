import json
import csv

projects = json.load(open('complete_projects.json'))

java_projects = filter(lambda project: 'Java' in project['cloc'] and 'Java' in project['language'], projects)

sorted_projects = sorted(java_projects, key=lambda project: project['cloc']['Java']['code'])

flattened_projects = [{'name' : project['name'], 'java_loc': project['cloc']['Java']['code'], 'java_files':project['cloc']['Java']['nFiles']} for project in sorted_projects]

with open('apache_java_projects.csv', 'w') as csvfile:
    fieldnames = ['name', 'java_loc', 'java_files']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(flattened_projects)
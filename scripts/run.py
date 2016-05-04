from projectfinder.apache import ProjectFinder
from projectfinder.infoenricher import LineOfCodeCounter
import json
import sys
import traceback

print 'Getting project info'

projects = ProjectFinder().get_projects()
counter = LineOfCodeCounter()

print 'Starting to analyze projects'
error_count = 0
for idx, project in enumerate(projects):
    print 'Analyzing project %s/%s: %s' % (idx + 1, len(projects), project['name'])
    sys.stdout.flush()
    try:
        counter.count_lines(project)
    except:
        print 'Error during analysis of: %s' % project['name']
        traceback.print_exc()
        error_count = error_count + 1
        
if error_count > 0:
    print "%s errors during analysis"

with open('projects.json', 'w') as out:
    json.dump(projects, out, indent=True)
'''
Created on May 4, 2016

@author: frederik
'''
import requests

PROJECTS_URL = 'https://projects.apache.org/json/foundation/projects'

class ProjectFinder(object):
    '''
    Retrieves projects from apache project directory
    '''

    def get_projects(self, languages=[]):
        r = requests.get(PROJECTS_URL)
        if r.status_code == 200:
            results = []
            projects = r.json()
            for name, project in projects.iteritems():
                language = project['programming-language']
                if len(languages) > 0:
                    if language not in languages:
                        continue
                project_info = {}
                project_info['name'] = name
                if 'repository' not in project:
                    continue
                project_info['repositories'] = project['repository']
                project_info['language'] = language
                results.append(project_info)
            return results
                
        else:
            raise RuntimeError('Could not load projects from apache project directory.')
        
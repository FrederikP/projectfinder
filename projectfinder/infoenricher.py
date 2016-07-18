'''
Created on May 4, 2016

@author: frederik
'''
from svn.remote import RemoteClient
from git import Repo
import os
import subprocess
import json

TMP_DIR = 'tmp'
CLOC_OUT = 'cloc.json'

class LineOfCodeCounter(object):
    '''
    Count lines of code to improve project information
    '''


    def count_lines(self, project_info):
        try:
            os.mkdir(TMP_DIR)
            repository = project_info['repositories'][0]
            tmp_path = os.path.join(TMP_DIR, project_info['name'])
            if 'svn' in repository:
                svn_repo = RemoteClient(repository)
                svn_repo.checkout(tmp_path)
            elif 'git' in repository:
                Repo.clone_from(repository, tmp_path)
            
            project_dir = tmp_path
            trunk_path = os.path.join(tmp_path, 'trunk')
            if os.path.isdir(trunk_path):
                project_dir = trunk_path
            subprocess.call(['./cloc.exe', '--json', '--out=%s' % CLOC_OUT, project_dir])
        
            try:
                with open(CLOC_OUT) as cloc_file:
                    cloc = json.load(cloc_file)
                    project_info['cloc'] = cloc    
            finally:
                if os.path.isfile(CLOC_OUT):
                    os.remove(CLOC_OUT)
        
        finally:
            if os.path.isdir(TMP_DIR):
                subprocess.call(['rm', '-rf', TMP_DIR])
            
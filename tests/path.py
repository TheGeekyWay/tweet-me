import os
import sys

'''
Since tweetme.py is now present in parent directory we need to add appropriate path in order to
access it as a module.
Path is added with respect to the location user is running the tests from.
'''
parent_directory_path = os.getcwd().split('/')
if 'tests' in parent_directory_path:
    parent_directory_path = parent_directory_path[:len(os.getcwd().split('/'))-1]
parent_directory_path = '/'.join(parent_directory_path)
if parent_directory_path not in sys.path:
    sys.path.append(parent_directory_path)

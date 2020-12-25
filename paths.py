'''
Example file on file paths
'''
import os
print(os.path.join('images', 'scenary', 'sunset.jpg'))

# returns current working directory
print(os.getcwd())

# returns complete file path of current file
print(os.path.realpath(__file__))

# returns the directory of the current file = getcwd()
print(os.path.dirname(os.path.realpath(__file__)))

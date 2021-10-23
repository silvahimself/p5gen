import argparse
import os
import shutil

parser = argparse.ArgumentParser(description='Generate p5.js projects')
# parser.add_argument('integers', metavar='N', type=int, nargs='+',
#                     help='an integer for the accumulator')
parser.add_argument('-t', '--use-typescript', action='store_true',
                    help='sum the integers (default: find the max)')
parser.add_argument("-p", "--path",
                    help="project name/path\nExamples:\np5gen -p my_project\np5gen -p new-folder/my_project", required=True)

args = parser.parse_args()

path = args.path

# options
useTypescript = args.use_typescript


# insert files in project based on configuration
template_base = './pub' + ('/ts' if useTypescript else '/js')

# copy template files to project folder
shutil.copytree(template_base, args.path)

print('Project created.')

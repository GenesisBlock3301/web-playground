import os
f = __file__
current_file_name = os.path.abspath(f)
project_dir = os.path.dirname(current_file_name)
print("File",f)
print("Current File Name",current_file_name)
print("Project Dir",project_dir)
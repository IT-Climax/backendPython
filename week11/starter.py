import os
import subprocess

def create_survey_project():
    #create a folder structure
    base_dir = "survey"
    folders =[
        "src",
        "src/api",
        "src/api/controllers",
        "src/api/models",
        "src/api/errors",
        "src/api/resources",
        "src/db",
        "src/db/models",
        "src/utils",
        "src/tests",
        
    ]


    for folder in folders:
        os.makedirs(os.path.join(base_dir, folder), exist_ok=True)

if __name__ == "__main__":
    create_survey_project()
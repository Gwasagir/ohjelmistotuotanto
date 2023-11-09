from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)
        parsed_content = toml.loads(content).get('tool').get('poetry')
        # print(parsed_content)
        
        project_name = parsed_content.get('name')
        project_description = parsed_content.get('description')

        project_dependencies = []
        for key in parsed_content.get('dependencies'):
            project_dependencies.append(key)
    
        project_dev_dependencies = []
        for key in parsed_content.get('group').get('dev').get('dependencies'):
            project_dev_dependencies.append(key)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(project_name , project_description, project_dependencies, project_dev_dependencies)

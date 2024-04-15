# project.py
class Project:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)


# task.py
class Task:
    def __init__(self, description, responsible_person, deadline):
        self.description = description
        self.responsible_person = responsible_person
        self.deadline = deadline
        self.status = "Pending"

    def update_status(self, status):
        self.status = status

# exceptions.py
class ProjectNotFoundError(Exception):
    pass


class TaskNotFoundError(Exception):
    pass

# file_operations.py
import pickle

def save_projects(projects, filename):
    with open(filename, 'wb') as f:
        pickle.dump(projects, f)

def load_projects(filename):
    try:
        with open(filename, 'rb') as f:
            projects = pickle.load(f)
    except FileNotFoundError:
        projects = []
    return projects

# project_manager.py

from project import Project
from task import Task
from exceptions import ProjectNotFoundError, TaskNotFoundError
from file_operations import save_projects, load_projects


class ProjectManager:
    def __init__(self, projects_file):
        self.projects_file = projects_file
        self.projects = load_projects(self.projects_file)

    def create_project(self, name):
        project = Project(name)
        self.projects.append(project)
        self._save_projects()

    def delete_project(self, project_name):
        for project in self.projects:
            if project.name == project_name:
                self.projects.remove(project)
                self._save_projects()
                return
        raise ProjectNotFoundError(f"Project '{project_name}' not found.")

    def create_task(self, project_name, description, responsible_person, deadline):
        for project in self.projects:
            if project.name == project_name:
                task = Task(description, responsible_person, deadline)
                project.add_task(task)
                self._save_projects()
                return
        raise ProjectNotFoundError(f"Project '{project_name}' not found.")

    def delete_task(self, project_name, task_description):
        for project in self.projects:
            if project.name == project_name:
                for task in project.tasks:
                    if task.description == task_description:
                        project.remove_task(task)
                        self._save_projects()
                        return
                raise TaskNotFoundError(f"Task '{task_description}' not found in project '{project_name}'.")
        raise ProjectNotFoundError(f"Project '{project_name}' not found.")

    def _save_projects(self):
        save_projects(self.projects, self.projects_file)

class ProjectManager:
    def create_project(self, project_name, responsible_person, deadline):
        pass

    def update_project(self, project_name, responsible_person=None, deadline=None):
        pass

    def delete_project(self, project_name):
        pass

    def get_project_info(self, project_name):
        pass

class TaskManager:
    def create_task(self, project_name, task_description, responsible_person, deadline):
        pass

    def update_task(self, project_name, task_description, responsible_person=None, deadline=None):
        pass

    def delete_task(self, project_name, task_description):
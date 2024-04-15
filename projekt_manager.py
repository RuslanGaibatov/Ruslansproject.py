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

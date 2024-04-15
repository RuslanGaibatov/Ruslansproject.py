class Task:
    def __init__(self, description, responsible_person, deadline):
        self.description = description
        self.responsible_person = responsible_person
        self.deadline = deadline
        self.status = "Pending"

    def update_status(self, status):
        self.status = status


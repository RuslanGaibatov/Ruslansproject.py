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
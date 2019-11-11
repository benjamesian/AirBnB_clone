"""Models

Application objects are defined here as well as functions for manipulating and
storing them

"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

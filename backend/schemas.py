# What data does the API accept

from pydantic import BaseModel

class ProjectIdea(BaseModel):
    name: str
    requirements: str

class TaskIdea(BaseModel):
    project_id: int
    title: str
    description: str
    status: str

class ProjectUpdate(BaseModel):
    name: str
    requirements: str

class TaskUpdate(BaseModel):
    project_id: int
    title: str
    description: str
    status: str
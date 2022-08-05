# Python
from typing import List

# FastAPI
from fastapi import APIRouter
from fastapi import status
from fastapi import Body, Path

#
from models.index import projects
from config.db import conn
from schemas.index import Project

project = APIRouter()



## Projects

### Register project

@project.post(
    path="/project/new/", 
    response_model=Project, 
    status_code=status.HTTP_201_CREATED,
    tags=["Projects"],
    summary="Publish a project in the app"
    )
def publish_project(project: Project = Body(...)):
    """
    Publish Project

    This path operation post a project in the app and save the information in the database

    Parameters: 
    - Request body parameter: 
        - **project: Project** -> A project model with name, blockchain, marketplace, size, description, release date, website and RRSS

    Returns a project model with name, blockchain, marketplace, size, description, release date, website and RRSS
    """
    return project

### Show a project

@project.get(
    path="/project/detail/{project_id}",
    status_code=status.HTTP_200_OK,
    tags=["Projects"],
    summary="Show a Project"
    )
def show_project(
    project_id: int = Path(
        ..., 
        gt=0,
        title="Project ID",
        description="This is de Project ID, it´s required"
        ) 
):
    """
    Show a Project

    This path operation show a project in the database

    Parameters: 
    - Path parameter: 
        - **project id: int** -> A project identifier

    Returns confirmation of whether the project exists in the database or not
    """
    pass

### Update a project

@project.put(
    path="/project/{project_id}", 
    response_model=Project, 
    status_code=status.HTTP_202_ACCEPTED,
    tags=["Projects"]
    )
def update_project(
    project_id: int = Path(
        ...,
        title="Project ID",
        description="This is the Project ID",
        gt=0
    ),
    project: Project = Body(...)
    ):
    return project  
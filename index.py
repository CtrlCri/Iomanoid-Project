from fastapi import FastAPI

from routes.user import user
from routes.project import project


app = FastAPI()

app.include_router(user)
app.include_router(project)


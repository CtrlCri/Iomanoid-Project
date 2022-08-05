from fastapi import FastAPI

from routes.index import user, project

app = FastAPI()

app.include_router(user)
app.include_router(project)


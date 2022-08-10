from fastapi import FastAPI

#from routes import user
#from routes.project import project
from routes import user

app = FastAPI()

app.include_router(user)
#app.include_router(project)


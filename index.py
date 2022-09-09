from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes import user, project, subscriber

app = FastAPI()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")

app.include_router(user)
app.include_router(project)
app.include_router(subscriber)


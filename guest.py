from config.db import SessionLocal

from fastapi import FastAPI
from fastapi import Depends

from starlette.responses import RedirectResponse

from sqlalchemy.orm import Session

app = FastAPI()



def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    return RedirectResponse(url="/docs/")


@app.post("/guest/project/")
def guest_project_post(db: Session=Depends(get_db)):
    """_summary_

    Returns:
        _type_: _description_
    """
    
    return "hola Crih"
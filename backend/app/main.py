from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import SessionLocal, engine
from . import models, crud

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "Hospital System Running"}

@app.get("/doctors")
def doctors(db: Session = Depends(get_db)):
    return crud.get_doctors(db)

@app.post("/appointment")
def book(appt: dict, db: Session = Depends(get_db)):
    result = crud.create_appointment(db, appt)
    if not result:
        return {"error": "Slot taken"}
    return result

@app.get("/appointments")
def all_appts(db: Session = Depends(get_db)):
    return db.query(models.Appointment).all()

@app.get("/logs")
def logs(db: Session = Depends(get_db)):
    return db.query(models.AuditLog).all()
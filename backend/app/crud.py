from sqlalchemy.orm import Session
from datetime import datetime
from . import models

def create_user(db: Session, user):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user

def get_doctors(db: Session):
    return db.query(models.Doctor).all()

def create_appointment(db: Session, appt):
    conflict = db.query(models.Appointment).filter(
        models.Appointment.doctor_id == appt.doctor_id,
        models.Appointment.time == appt.time
    ).first()

    if conflict:
        return None

    new_appt = models.Appointment(**appt.dict())
    db.add(new_appt)

    # 🔥 LOGGING
    log = models.AuditLog(
        action="CREATE",
        details=f"Appointment booked for patient {appt.patient_id}",
        timestamp=datetime.now()
    )

    db.add(log)
    db.commit()
    return new_appt

def delete_appointment(db: Session, id: int):
    appt = db.query(models.Appointment).get(id)
    db.delete(appt)

    log = models.AuditLog(
        action="DELETE",
        details=f"Appointment {id} deleted",
        timestamp=datetime.now()
    )

    db.add(log)
    db.commit()
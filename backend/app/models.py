from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from .database import Base

class User(Base):
    _tablename_ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))   # ✅ patient name stored
    email = Column(String(100), unique=True)
    password = Column(String(200))
    role = Column(String(20))  # patient/admin

class Doctor(Base):
    _tablename_ = "doctors"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    specialization = Column(String(100))

class Appointment(Base):
    _tablename_ = "appointments"

    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey("users.id"))
    doctor_id = Column(Integer, ForeignKey("doctors.id"))
    time = Column(DateTime)

class AuditLog(Base):
    _tablename_ = "audit_logs"

    id = Column(Integer, primary_key=True)
    action = Column(String(50))  # CREATE / DELETE
    details = Column(String(200))
    timestamp = Column(DateTime)
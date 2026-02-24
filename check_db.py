from models import db, User
from app import app  # make sure app.py is in the same folder

with app.app_context():
    users = User.query.all()
    for u in users:
        print(f"ID: {u.id}, Name: {u.name}, Email: {u.email}, Role: {u.role}, Class: {getattr(u, 'student_class', None)}")
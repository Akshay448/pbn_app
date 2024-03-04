# from django.db import models
#
# used with viwset
# class Patient(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     phone_number = models.CharField(max_length=20)
#     date_of_birth = models.DateField()
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"


from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    phone_number = Column(String(20))
    date_of_birth = Column(Date)

    def __repr__(self):
        return f"<Patient(first_name='{self.first_name}', last_name='{self.last_name}')>"

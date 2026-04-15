"""
Database models for activities and participants
"""

from sqlalchemy import Column, Integer, String, Text, List
from sqlalchemy.orm import relationship
from database import Base


class Activity(Base):
    """
    Activity model representing an extracurricular activity
    """
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), unique=True, nullable=False, index=True)
    description = Column(Text, nullable=False)
    schedule = Column(String(255), nullable=False)
    max_participants = Column(Integer, nullable=False)

    # Relationship to participants
    participants = relationship("Participant", back_populates="activity", cascade="all, delete-orphan")

    def to_dict(self):
        """Convert activity to dictionary format matching the original API"""
        return {
            "description": self.description,
            "schedule": self.schedule,
            "max_participants": self.max_participants,
            "participants": [p.email for p in self.participants]
        }


class Participant(Base):
    """
    Participant model representing a student enrolled in an activity
    """
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), nullable=False, index=True)
    activity_id = Column(Integer, nullable=False, index=True)

    # Relationship to activity
    activity = relationship("Activity", back_populates="participants")

    def __repr__(self):
        return f"<Participant(email={self.email}, activity_id={self.activity_id})>"

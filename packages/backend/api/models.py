from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    logo = Column(String)

    quizes = relationship("Quiz", back_populates="project")


class Quiz(Base):
    __tablename__ = "quizes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    project_id = Column(Integer, ForeignKey("projects.id"))

    project = relationship("Project", back_populates="quizes")
    questions = relationship("Question", back_populates="quiz")


class Question(Base):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, index=True)
    quiz_id = Column(Integer, ForeignKey("quizes.id"))

    quiz = relationship("Quiz", back_populates="questions")
    answers = relationship("Answer", back_populates="question")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    answer = Column(String, index=True)
    is_valid = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey("questions.id"))

    question = relationship("Question", back_populates="answers")

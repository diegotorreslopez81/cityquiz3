from sqlalchemy.orm import Session

from ..models import Quiz
from ..schemas import QuizCreateSchema


class QuizService:
    def get_quiz(db: Session, quiz_id: int):
        return db.query(Quiz).filter(Quiz.id == quiz_id).first()

    def get_quiz_by_name(db: Session, name: str):
        return db.query(Quiz).filter(Quiz.name == name).first()

    def get_quizes(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Quiz).offset(skip).limit(limit).all()

    def create_quiz(db: Session, quiz: QuizCreateSchema):
        db_quiz = Quiz(name=quiz.name, project_id=quiz.project_id)
        db.add(db_quiz)
        db.commit()
        db.refresh(db_quiz)
        return db_quiz

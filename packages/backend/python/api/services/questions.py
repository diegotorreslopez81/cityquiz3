from sqlalchemy.orm import Session

from ..models import Question
from ..schemas import QuestionCreateSchema


class QuestionService:
    def get_question(db: Session, question_id: int):
        return db.query(Question).filter(Question.id == question_id).first()

    def get_questions(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Question).offset(skip).limit(limit).all()

    def create_question(db: Session, question: QuestionCreateSchema):
        db_question = Question(question=question.question, quiz_id=question.quiz_id)
        db.add(db_question)
        db.commit()
        db.refresh(db_question)
        return db_question

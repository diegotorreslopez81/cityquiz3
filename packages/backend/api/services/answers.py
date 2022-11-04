from sqlalchemy.orm import Session

from ..models import Answer
from ..schemas import AnswerCreateSchema


class AnswerService:
    def get_answer(db: Session, answer_id: int):
        return db.query(Answer).filter(Answer.id == answer_id).first()

    def get_answer_by_name(db: Session, name: str):
        return db.query(Answer).filter(Answer.name == name).first()

    def get_answeres(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Answer).offset(skip).limit(limit).all()

    def create_answer(db: Session, answer: AnswerCreateSchema):
        db_answer = Answer(name=answer.name, project_id=answer.project_id)
        db.add(db_answer)
        db.commit()
        db.refresh(db_answer)
        return db_answer

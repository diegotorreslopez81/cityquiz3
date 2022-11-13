from sqlalchemy.orm import Session

from ..models import Quiz, Question, Answer
from ..schemas import QuizCreateSchema, QuizAnswerSchema, QuestionToRead


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

    def answer_quiz(db: Session, quiz_answer: QuizAnswerSchema):
        db_questions = db.query(Question).filter(Question.quiz_id == quiz_answer.quiz_id).all()
        valid_answers = {}
        answer_result = dict(correct = 0, incorrect = 0, result = False)
        for db_question in db_questions:
            db_valid_answer = db.query(Answer).filter(Answer.question_id == db_question.id, Answer.is_valid==True).first()
            valid_answers[db_question.id] = db_valid_answer.id

        for profile_answer in quiz_answer.answers:
            if valid_answers[profile_answer.question_id] == profile_answer.answer_id:
                answer_result["correct"] += 1
            else:
                answer_result["incorrect"] += 1

        if answer_result["correct"]/len(valid_answers) > 0.7:
            answer_result["result"] = True
        
        return answer_result

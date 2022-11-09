from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from .schemas import (
    ProjectSchema,
    ProjectCreateSchema,
    QuizSchema,
    QuizCreateSchema,
    QuizToRead,
    QuestionCreateSchema,
    QuestionSchema,
    AnswerCreateSchema,
    AnswerSchema,
)

from .database import SessionLocal, engine, Base
from .services import ProjectService, QuizService, QuestionService, AnswerService

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# PROJECTS
@app.post("/projects/", response_model=ProjectSchema)
def create_project(project: ProjectCreateSchema, db: Session = Depends(get_db)):
    db_project = ProjectService.get_project_by_name(db, name=project.name)
    if db_project:
        raise HTTPException(status_code=400, detail="Name already registered")
    return ProjectService.create_project(db=db, project=project)


@app.get("/projects/", response_model=List[ProjectSchema])
def read_projects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _projects = ProjectService.get_projects(db, skip=skip, limit=limit)
    return _projects


@app.get("/projects/{project_id}", response_model=ProjectSchema)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = ProjectService.get_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return db_project


# QUIZES
@app.post("/quizes/", response_model=QuizSchema)
def create_quizes(quiz: QuizCreateSchema, db: Session = Depends(get_db)):
    return QuizService.create_quiz(db=db, quiz=quiz)


@app.get("/quizes/", response_model=List[QuizToRead])
def read_quizes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _quizes = QuizService.get_quizes(db, skip=skip, limit=limit)
    return _quizes


@app.get("/quizes/{quiz_id}", response_model=QuizToRead)
def read_quiz(quiz_id: int, db: Session = Depends(get_db)):
    db_quiz = QuizService.get_quiz(db, quiz_id=quiz_id)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="quiz not found")
    return db_quiz


# QUESTIONS
@app.post("/questions/", response_model=QuestionSchema)
def create_questions(question: QuestionCreateSchema, db: Session = Depends(get_db)):
    return QuestionService.create_question(db=db, question=question)


@app.get("/questions/", response_model=List[QuestionSchema])
def read_questions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _questions = QuestionService.get_questions(db, skip=skip, limit=limit)
    return _questions


@app.get("/questions/{question_id}", response_model=QuestionSchema)
def read_question(question_id: int, db: Session = Depends(get_db)):
    db_question = QuestionService.get_question(db, question_id=question_id)
    if db_question is None:
        raise HTTPException(status_code=404, detail="question not found")
    return db_question


# ANSWERS
@app.post("/answers/", response_model=AnswerSchema)
def create_answers(answer: AnswerCreateSchema, db: Session = Depends(get_db)):
    return AnswerService.create_answer(db=db, answer=answer)


@app.get("/answers/", response_model=List[AnswerSchema])
def read_answers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _answers = AnswerService.get_answers(db, skip=skip, limit=limit)
    return _answers


@app.get("/answers/{answer_id}", response_model=AnswerSchema)
def read_answer(answer_id: int, db: Session = Depends(get_db)):
    db_answer = AnswerService.get_answer(db, answer_id=answer_id)
    if db_answer is None:
        raise HTTPException(status_code=404, detail="answer not found")
    return db_answer


@app.get("/")
def read_root():
    return {"Hello": "City Quiz"}

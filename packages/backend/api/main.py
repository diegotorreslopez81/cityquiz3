from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .schemas import (
    ProjectSchema,
    ProjectCreateSchema,
    QuizSchema,
    QuizCreateSchema,
    QuizToRead,
    QuizAnswerSchema,
    QuizAnswerResult,
    QuestionCreateSchema,
    QuestionSchema,
    AnswerCreateSchema,
    AnswerSchema,
    ProfileSchema,
    ProfileCreateSchema,
    ProfileCreateNftSchema,
)

from .database import SessionLocal, engine, Base
from .services import (
    ProjectService,
    QuizService,
    QuestionService,
    AnswerService,
    ProfileService,
)

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
        raise HTTPException(status_code=404, detail="Project not found")
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
        raise HTTPException(status_code=404, detail="Quiz not found")
    return db_quiz


@app.post("/quizes/answer", response_model=QuizAnswerResult)
def read_quiz(quiz_answer: QuizAnswerSchema, db: Session = Depends(get_db)):
    db_quiz = QuizService.answer_quiz(db, quiz_answer=quiz_answer)
    if db_quiz is None:
        raise HTTPException(status_code=404, detail="Quiz not found")
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
        raise HTTPException(status_code=404, detail="Question not found")
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
        raise HTTPException(status_code=404, detail="Answer not found")
    return db_answer


# PROFILES
@app.post("/profiles/", response_model=ProfileSchema)
def create_profile(profile: ProfileCreateSchema, db: Session = Depends(get_db)):
    return ProfileService.create_profile(db=db, profile=profile)


@app.get("/profiles/{wallet}", response_model=ProfileSchema)
def read_profile(wallet: str, db: Session = Depends(get_db)):
    db_profile = ProfileService.get_profile_by_wallet(db, wallet=wallet)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return db_profile


@app.get("/profiles/", response_model=List[ProfileSchema])
def read_profiles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _profiles = ProfileService.get_profiles(db, skip=skip, limit=limit)
    return _profiles


@app.patch("/profiles/{wallet}/nft", response_model=ProfileSchema)
def save_nft(wallet: str, nft: ProfileCreateNftSchema, db: Session = Depends(get_db)):
    print(nft, wallet)
    return ProfileService.create_profile_nft(db=db, wallet=wallet, nft=nft)


@app.get("/")
def read_root():
    return {"Hello": "City Quiz"}

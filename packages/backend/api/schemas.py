from typing import Union, List
from pydantic import BaseModel

# ANSWER
class AnswerBase(BaseModel):
    question_id: int
    answer: str
    is_valid: bool = False


class AnswerCreateSchema(AnswerBase):
    pass


class AnswerSchema(AnswerBase):
    id: int

    class Config:
        orm_mode = True


class AnswerToRead(BaseModel):
    id: int
    answer: str

    class Config:
        orm_mode = True


# QUESTION
class QuestionBase(BaseModel):
    quiz_id: int
    question: str


class QuestionCreateSchema(QuestionBase):
    pass


class QuestionSchema(QuestionBase):
    id: int

    class Config:
        orm_mode = True


class QuestionToRead(BaseModel):
    id: int
    question: str
    answers: List[AnswerToRead]

    class Config:
        orm_mode = True


# QUIZ
class QuizBase(BaseModel):
    name: str
    project_id: int


class QuizCreateSchema(QuizBase):
    pass


class QuizSchema(QuizBase):
    id: int

    class Config:
        orm_mode = True


class QuizToRead(BaseModel):
    id: int
    name: str
    questions: List[QuestionToRead]

    class Config:
        orm_mode = True


class QuizAnswerResult(BaseModel):
    correct: int
    incorrect: int
    result: bool


class QuizAnswerPair(BaseModel):
    question_id: int
    answer_id: int


class QuizAnswerSchema(BaseModel):
    wallet: str
    quiz_id: int
    answers: List[QuizAnswerPair]


# PROJECT
class ProjectBase(BaseModel):
    name: str
    logo: str
    description: Union[str, None] = None


class ProjectCreateSchema(ProjectBase):
    pass


class ProjectSchema(ProjectBase):
    id: int
    quizes: List[QuizToRead]

    class Config:
        orm_mode = True


# PROFILES
class ProfileBase(BaseModel):
    wallet: str
    nickname: str = None
    nfts: str = None


class ProfileCreateSchema(ProfileBase):
    pass


class ProfileCreateNftSchema(BaseModel):
    nft: str


class ProfileSchema(ProfileBase):
    id: int

    class Config:
        orm_mode = True

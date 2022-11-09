from typing import Union, List
from pydantic import BaseModel

# ANSWER
class AnswerBase(BaseModel):
    question_id: int
    answer: str
    valid: bool = False

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










# Project: "MOONBEAN"
#     Quiz: #1231
#         Question: 001 - name of the creators?
#             answer: 001 - "fred and tell" valid: False
#             answer: 002 - "Pepe y Moni" valid: False
#             answer: 003 - "Peter and Jhon" valid: True

#         Question: 002 - En que año inicio?
#             answer: 004 - "2014" valid: False
#             answer: 005 - "2021" valid: True
#             answer: 006 - "2022" valid: False


# {
#     wallet: 012873640182736401287346012,
#     quiz: {
#         id: 1231,
#         answers: {
#             {
#                 question: 001,
#                 answer: 002
#             },
#             {
#                 question: 002,
#                 answer: 005
#             },
#         }
#     }
# }

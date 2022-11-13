from sqlalchemy.orm import Session

from ..models import Project
from ..schemas import ProjectCreateSchema


class ProjectService:
    def get_project(db: Session, project_id: int):
        return db.query(Project).filter(Project.id == project_id).first()

    def get_project_by_name(db: Session, name: str):
        return db.query(Project).filter(Project.name == name).first()

    def get_projects(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Project).offset(skip).limit(limit).all()

    def create_project(db: Session, project: ProjectCreateSchema):
        db_project = Project(
            name=project.name, logo=project.logo, description=project.description
        )
        db.add(db_project)
        db.commit()
        db.refresh(db_project)
        return db_project

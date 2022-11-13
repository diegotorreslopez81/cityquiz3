from sqlalchemy.orm import Session

from ..models import Profile
from ..schemas import ProfileCreateSchema, ProfileCreateNftSchema


class ProfileService:
    def get_profile(db: Session, profile_id: int):
        return db.query(Profile).filter(Profile.id == profile_id).first()

    def get_profile_by_wallet(db: Session, wallet: str):
        return db.query(Profile).filter(Profile.wallet == wallet).first()

    def get_profiles(db: Session, skip: int = 0, limit: int = 100):
        return db.query(Profile).offset(skip).limit(limit).all()

    def create_profile(db: Session, profile: ProfileCreateSchema):
        db_profile = Profile(wallet=profile.wallet, nickname=profile.nickname)
        db.add(db_profile)
        db.commit()
        db.refresh(db_profile)
        return db_profile

    def create_profile_nft(db: Session, wallet: str, nft: ProfileCreateNftSchema):
        db_profile = db.query(Profile).filter(Profile.wallet == wallet).first()
        if db_profile.nfts:
            db_profile.nfts = f"{db_profile.nfts}, {nft.nft}"
        else:
            db_profile.nfts = nft.nft
        db.commit()
        db.refresh(db_profile)
        return db_profile

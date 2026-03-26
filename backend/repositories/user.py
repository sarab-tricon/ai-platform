from sqlalchemy.orm import Session
from db.models import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):

    def create_user(self, email: str, password: str):
        user = User(email=email, password=password)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_id(self, user_id: int):
        return self.db.query(User).filter(User.id == user_id).first()
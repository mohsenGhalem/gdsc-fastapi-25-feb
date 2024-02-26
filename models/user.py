
from datetime import datetime

from passlib.context import CryptContext
from pydantic import BaseModel

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")




class UserRegister(BaseModel):
    email: str
    password: str

    def hash_password(self):
        self.password = pwd_context.hash(self.password)


class User(BaseModel):
    id: str = None
    email: str
    name: str = ""
    age: int = 0
    img_link: str = ""
    created_at: datetime = datetime.now()


def verify_password(plain_password, hashed_password) -> bool:
    print(plain_password)
    print(hashed_password)
    return pwd_context.verify(plain_password, hashed_password)
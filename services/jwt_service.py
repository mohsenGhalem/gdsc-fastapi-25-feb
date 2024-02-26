
import datetime

import jwt
import os

secretKey = os.environ['SECRET_KEY']
algorithm = os.environ['ALGORITHM']


def generate_token(user_id: str):
    payload = {"sub": user_id, "exp": datetime.datetime.now() + datetime.timedelta(days=3)}
    token = jwt.encode(payload, secretKey, algorithm=algorithm)
    return token


def verify_token_validity(token: str) -> object:
    try:
        decoded = jwt.decode(token, secretKey, algorithms=[algorithm])
        return decoded['sub']
    except:
        return None
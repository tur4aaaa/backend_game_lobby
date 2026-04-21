import jwt 
import datetime

secret = "secret_key"
ALGORITHM = "HS256"

def create_token(user_id:int):
    payload = {
        "user_id": user_id,
        "exp":datetime.datetime.utcnow() + datetime.timedelta(minutes = 15)
    }

    token = jwt.encode(payload,secret,algorithm = ALGORITHM)
    return token

def verify_token(token:str):
    try:
        payload = jwt.decode(token,secret,algorithms = [ALGORITHM])
        return payload["user_id"]
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
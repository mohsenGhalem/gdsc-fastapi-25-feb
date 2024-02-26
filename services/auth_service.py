from fastapi import HTTPException, APIRouter, status

from db.db_connection import get_database, close_db_connection
from models.api_response import ApiResponse
from models.user import UserRegister, User, verify_password
from services.jwt_service import generate_token

router = APIRouter(
    prefix="/v1/auth",
    tags=['auth v1']
)


@router.post('/register', response_model=ApiResponse, status_code=status.HTTP_201_CREATED)
def register(user_register: UserRegister) -> ApiResponse:
    dbname = get_database()
    auth_collection = dbname['auth']

    found = auth_collection.find_one({'email': user_register.email})

    if found is None:
        try:
            user_register.hash_password()
            auth_data = dict(user_register)
            auth_collection.insert_one(auth_data)
            user = User(id=str(auth_data['_id']), email=auth_data['email'])
            user_json = dict(user)

            # Insert The user information on db
            users_collection = dbname['users']
            users_collection.insert_one(user_json)
            user_json.pop('_id')
            # Generate Token
            token = generate_token(user_id=user_json['id'])

            data = {
                'token': token,
                'info': user_json
            }
            close_db_connection()
            return ApiResponse(message="SUCCESS", success=True, data=data)
        except Exception as e:
            print(f'ERROR = {e}')
            data = {
                'token': None,
                'info': None
            }
            close_db_connection()
            raise HTTPException(status_code=500,
                                detail=str(ApiResponse(message="SERVER_ERROR", success=False, data=data)))
    else:
        data = {
            'token': None,
            'info': None
        }
        close_db_connection()

        raise HTTPException(status_code=403, detail=str(ApiResponse(message="ALREADY_EXISTS", success=True, data=data)))

# Login Method
@router.post("/login", response_model=ApiResponse)
def authenticate(user_register: UserRegister):
    try:
        dbname = get_database()
        auth_collection = dbname['auth']
        found = auth_collection.find_one({'email': user_register.email})

        if found is None:
            close_db_connection()
            raise HTTPException(status_code=404,
                                detail=str(ApiResponse(message="NOT_FOUND", success=False, data={})))
        else:
            close_db_connection()
            if not verify_password(user_register.password, found['password']):
                return ApiResponse(message="PASSWORD_INVALID", success=True, data={})
            else:
                users_collection = dbname['users']

                user = users_collection.find_one({'id': str(found['_id'])})

                token = generate_token(str(found['_id']))
                del user['_id']
                data = {'token': token, 'info': dict(user)}
                close_db_connection()
                return ApiResponse(message="SUCCESS", success=True, data=data)

    except Exception as e:

        print(f'ERROR = {e}')
        close_db_connection()
        raise HTTPException(status_code=500,
                            detail=str(ApiResponse(message="SERVER_ERROR", success=False, data={})))
from fastapi import APIRouter, HTTPException, Header
from db.db_connection import get_database

from models.api_response import ApiResponse
from models.user import UserUpdate
from services.jwt_service import verify_token_validity


router = APIRouter(prefix="/v1/users", tags=["User OP v1"])

#Here I get the user id from decrypted token and then update the user info
@router.patch("/", response_model=ApiResponse)
def update_user_info(user: UserUpdate, token: str = Header(...)) -> ApiResponse:
    uid = verify_token_validity(token=token)

    if uid is None:
        raise HTTPException(
            status_code=401,
            detail=dict(ApiResponse(message="UNAUTHORIZED", success=False)),
        )

    else:

        dbname = get_database()
        user_collection = dbname["users"]
        existing_user = dict(user)
        print(existing_user)
        updated = user_collection.update_one({"id": uid}, {"$set": existing_user})
        if updated.matched_count == 1:
            return ApiResponse(
                message="SUCCESS",
                success=True,
                data=dict(user),
            )
        else:
            raise HTTPException(
                status_code=404,
                detail=dict(
                    ApiResponse(
                        message="NOT_FOUND",
                        success=False,
                    )
                ),
            )


#TODO: Create a class that will be used to create a response object for the API
from pydantic import BaseModel


class ApiResponse(BaseModel):
    message: str
    success: bool
    data: dict = {}
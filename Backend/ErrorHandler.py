from fastapi.exceptions import RequestValidationError
# from pydantic import BaseModel, ValidationError
from starlette.requests import Request
from starlette.responses import JSONResponse

from config import app # requires Backend.


# SOURCE: https://github.com/tiangolo/fastapi/issues/484

@app.exception_handler(RequestValidationError)
async def handler1(request: Request, exc: Exception):
    print("ValidationError")
    print(type(exc))
    return JSONResponse(status_code=500, content={
        "success": False,
        "message": str(exc)
    })

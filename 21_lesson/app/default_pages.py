import json
import aiofiles

from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path


default_router = APIRouter()


current_file_path = Path(__file__)
parent_directory = current_file_path.parent.parent

json_file_path = parent_directory / "src" / "data.json"


@default_router.get("/")
async def read_root():
    async with aiofiles.open(json_file_path, mode='r') as file:
        contents = await file.read()
        
    message = json.loads(contents)["message"]
    return message



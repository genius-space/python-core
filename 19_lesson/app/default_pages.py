from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path
import json


default_router = APIRouter()


current_file_path = Path(__file__)
parent_directory = current_file_path.parent.parent

json_file_path = parent_directory / "src" / "data.json"


@default_router.get("/")
def read_root():
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    return data
    # return FileResponse("src/python.png")



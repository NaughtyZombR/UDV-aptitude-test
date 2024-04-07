import json
from enum import Enum
from pathlib import Path


class DataFile(Enum):
    NEWS = "news.json"
    COMMENTS = "comments.json"


def load_data(file_type: DataFile) -> dict:
    """Функция для загрузки данных из JSON файла"""
    file_path = Path(__file__).parent.parent / file_type.value
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except json.decoder.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")

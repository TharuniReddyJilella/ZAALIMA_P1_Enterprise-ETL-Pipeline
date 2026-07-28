import json
from pathlib import Path
from datetime import datetime


class FileWriter:

    @staticmethod
    def save_json(data, prefix: str):

        Path("data/raw").mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"data/raw/{prefix}_{timestamp}.json"

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        return filename
import json
from pathlib import Path


class JSONWriter:
    @staticmethod
    def save(data, filename: str):
        output_dir = Path("data/raw")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_file = output_dir / filename

        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"Data saved to {output_file}")
from pathlib import Path


class CSVWriter:

    @staticmethod
    def save(df, filename: str):
        output_dir = Path("data/processed")
        output_dir.mkdir(parents=True, exist_ok=True)

        output_path = output_dir / filename

        df.to_csv(output_path, index=False)

        print(f"Processed data saved to {output_path}")
import pandas as pd


class CustomerTransformer:
    def transform(self, input_file: str):
        df = pd.read_json(input_file)

        print("\nOriginal Data\n")
        print(df.head())

        return df
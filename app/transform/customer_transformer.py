import pandas as pd


class CustomerTransformer:
    def transform(self, input_file: str):
        # Read raw JSON
        df = pd.read_json(input_file)

        print("\n===== ORIGINAL DATA =====")
        print(df.head())

        # Keep only the columns we need
        df = df[
            [
                "id",
                "name",
                "username",
                "email",
                "phone",
                "website",
            ]
        ]

        # Rename columns
        df = df.rename(
            columns={
                "id": "customer_id",
                "name": "customer_name",
                "username": "username",
                "email": "email",
                "phone": "phone_number",
                "website": "website",
            }
        )

        print("\n===== CLEANED DATA =====")
        print(df.head())

        # Check for missing values
        print("\n===== MISSING VALUES =====")
        print(df.isnull().sum())

        # Fill missing values
        df["phone_number"] = df["phone_number"].fillna("Unknown")
        df["website"] = df["website"].fillna("Not Available")

        return df
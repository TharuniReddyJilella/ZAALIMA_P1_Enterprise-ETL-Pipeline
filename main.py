from app.extract.stripe_extractor import StripeExtractor
from app.transform.customer_transformer import CustomerTransformer
from app.utils.json_writer import JSONWriter
from app.utils.csv_writer import CSVWriter
from app.load.sqlite_loader import SQLiteLoader

def main():
    print("=" * 60)
    print("Enterprise ETL Pipeline")
    print("=" * 60)

    # -----------------------------
    # Step 1: Extract data
    # -----------------------------
    extractor = StripeExtractor()

    customers = extractor.extract_customers(
        page=1,
        limit=5
    )

    print(f"\nFetched {len(customers)} customers")

    # -----------------------------
    # Step 2: Save raw JSON
    # -----------------------------
    JSONWriter.save(
        customers,
        "stripe_customers_page1.json"
    )

    # -----------------------------
    # Step 3: Transform data
    # -----------------------------
    transformer = CustomerTransformer()

    cleaned_df = transformer.transform(
        "data/raw/stripe_customers_page1.json"
    )

    # -----------------------------
    # Step 4: Save processed CSV
    # -----------------------------
    CSVWriter.save(
        cleaned_df,
        "customers.csv"
    )

    print("\nETL Pipeline completed successfully!")
    loader = SQLiteLoader()

    loader.load(
    cleaned_df,
    "customers"
)

    loader.close()
    print("\nETL Pipeline completed successfully!")

if __name__ == "__main__":
    main()
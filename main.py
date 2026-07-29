from app.extract.stripe_extractor import StripeExtractor
from app.utils.json_writer import JSONWriter


def main():
    extractor = StripeExtractor()

    customers = extractor.extract_customers(
        page=1,
        limit=5,
    )

    print(f"Fetched {len(customers)} customers")

    JSONWriter.save(
        customers,
        "stripe_customers_page1.json",
    )


if __name__ == "__main__":
    main()
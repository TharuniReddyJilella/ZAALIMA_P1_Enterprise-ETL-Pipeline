from app.extract.stripe_extractor import StripeExtractor
from app.transform.customer_transformer import CustomerTransformer
from app.utils.json_writer import JSONWriter


def main():
    extractor = StripeExtractor()

    customers = extractor.extract_customers(
        page=1,
        limit=5,
    )

    JSONWriter.save(
        customers,
        "stripe_customers_page1.json",
    )

    transformer = CustomerTransformer()

    transformer.transform(
        "data/raw/stripe_customers_page1.json"
    )


if __name__ == "__main__":
    main()
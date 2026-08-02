from app.extract.stripe_extractor import StripeExtractor


def test_extract_customers():
    extractor = StripeExtractor()

    customers = extractor.extract_customers(
        page=1,
        limit=5
    )

    assert isinstance(customers, list)
    assert len(customers) == 5
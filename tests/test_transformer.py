import pandas as pd

from app.transform.customer_transformer import CustomerTransformer


def test_transform():
    transformer = CustomerTransformer()

    df = transformer.transform("data/raw/stripe_customers_page1.json")

    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0
    assert "customer_id" in df.columns
    assert "customer_name" in df.columns
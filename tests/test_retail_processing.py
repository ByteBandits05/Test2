def test_row_count():
    import pandas as pd
    df = pd.read_csv("/dbfs/mnt/data/raw/retail.csv")
    assert len(df) > 0

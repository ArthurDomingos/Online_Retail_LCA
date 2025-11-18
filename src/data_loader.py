def load_data():
    from ucimlrepo import fetch_ucirepo
    online_retail = fetch_ucirepo(id=352)
    df = online_retail.data.features.reset_index()
    df = df.rename(columns={'index':'InvoiceNo'})
    return df

# Main analysis pipeline

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import matplotlib.ticker as ticker

## Dropping rows that CustomerID is null
df_filtered = df[df["CustomerID"].notna()].reset_index(drop=True)

## Converting CustomerID to int
df_filtered["CustomerID"] = df_filtered["CustomerID"].astype(int)

## Creating Total Price Column that will be Qty * Price
df_filtered["Total_Price"] = df_filtered["Quantity"] *  df_filtered["UnitPrice"]
## Filtering Total Price > 0
df_filtered = df_filtered[df_filtered['Total_Price'] > 0].reset_index(drop=True)

display(df_filtered)

df_filtered['InvoiceDate'] = pd.to_datetime(df_filtered['InvoiceDate'])

# Getting the last transaction date to calculate recency
last_transaction_date = df_filtered['InvoiceDate'].max() + pd.Timedelta(days=1)

# Grouping data
df_rfm = df_filtered.groupby('CustomerID').agg({
    'InvoiceDate' : lambda date: (last_transaction_date - date.max()).days,
    'InvoiceNo' : 'nunique',
    'Total_Price' : 'sum'
})

# Renaming RFM column names
df_rfm.rename(columns={'InvoiceDate': 'Recency',
                       'InvoiceNo': 'Frequency',
                       'Total_Price': 'Monetary'}, inplace=True)

#Range Score for RFM
r_range_score = range(4,0,-1)
fm_range_score = range(1,5)

#Splitting Ranges in Quartiles and creating scores for each variable
df_rfm['Recency_Score'] = pd.qcut(
    df_rfm['Recency'].rank(method='first'),
    q=4,
    labels=r_range_score
)

df_rfm['Frequency_Score'] = pd.qcut(
    df_rfm['Frequency'].rank(method='first'),
    q=4,
    labels=fm_range_score
)

df_rfm['Monetary_Score'] = pd.qcut(
    df_rfm['Monetary'].rank(method='first'),
    q=4,
    labels=fm_range_score
)

#Final RFM Score
df_rfm['Final_Score'] = df_rfm['Recency_Score'].astype(int) + df_rfm['Frequency_Score'].astype(int) + df_rfm['Monetary_Score'].astype(int)  

display(df_rfm)

grouped_df = df_filtered.groupby(['CustomerID', 'Country']).agg({
    'Quantity': 'sum',
    'Total_Price': 'sum',
    'InvoiceNo': 'nunique'   
})

# Renaming RFM column names
grouped_df.rename(columns={'Quantity': 'Total_products',
                       'InvoiceNo': 'Number_of_purchases',
                       'Total_Price': 'Total_value'}, inplace=True)

grouped_df = grouped_df.reset_index()

display(grouped_df)

from stepmix.stepmix import StepMix
from stepmix.utils import get_mixed_descriptor

results = []
for k in range(2, 9):  # test 2 to 8 classes
    print(f"\nFitting model with {k} classes...")

    model = StepMix(
        n_components=k,
        measurement=mixed_descriptor,
        n_init=1,
        random_state=123,
        verbose=0
    )
    
    model.fit(mixed_data)

    ll      = model.lower_bound_               # log-likelihood
    aic     = model.aic(mixed_data)            # <== NOW PASS X
    bic     = model.bic(mixed_data)            # <== pass X
    caic    = model.caic(mixed_data)           # <== pass X
    sabic   = model.sabic(mixed_data)          # <== pass X
    entropy = model.entropy(mixed_data)        # <== pass X
    n_params = model.n_parameters               # attribute

    results.append([k, ll, aic, bic, caic, sabic, entropy])

columns = ["Classes", "LogLikelihood", "AIC", "BIC", "CAIC", "SABIC", "Entropy"]
model_comparison = pd.DataFrame(results, columns=columns)

display(model_comparison)

model = StepMix(
    n_components=6,
    measurement=mixed_descriptor,
    n_init=1,
    random_state=123,
    verbose=3
)

model.fit(mixed_data)

# Class predictions
lca_df['mixed_pred'] = model.predict(mixed_data)

# Get class predictions
lca_df["Class"] = model.predict(mixed_data)

# Show summary statistics by class
class_summary = lca_df.groupby("Class").agg({
    "Number_of_purchases": "mean",
    "Total_products": "mean",
    "Total_value": "mean",
    "Recency": "mean",
    "Frequency": "mean",
    "Monetary": "mean"
})

display(class_summary)

# Class distribution
lca_df["Class"].value_counts()

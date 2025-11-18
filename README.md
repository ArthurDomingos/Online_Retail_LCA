# Online Retail Customer Segmentation Using Latent Class Analysis (LCA)

This project applies **Latent Class Analysis (LCA)** to the *Online
Retail Dataset* to identify hidden customer groups based on purchasing
behavior.\
The analysis includes data preprocessing, feature engineering,
visualization, and model selection using information criteria (AIC, BIC,
CAIC).

------------------------------------------------------------------------

## 📊 Project Overview

Traditional segmentation methods (like k-means) assume hard clusters and
focus mainly on distances.\
**Latent Class Analysis**, however:

-   Models *probabilistic* membership\
-   Supports *mixed data types*\
-   Identifies deep, hidden behavioral segments\
-   Uses statistical information criteria to choose the best number of
    groups

This project discovers meaningful customer patterns such as: -
High-value repeat buyers\
- Occasional bulk purchasers\
- One-time low-volume shoppers\
- Country-specific purchasing behavior\
...and more.

------------------------------------------------------------------------

## 🧱 Repository Structure

    OnlineRetailProject/
    │
    ├── notebooks/
    │   └── lca.ipynb            # Original exploratory notebook
    │
    ├── src/
    │   ├── data_loader.py       # Functions to load and prepare data
    │   ├── visualizations.py    # All plotting functions
    │   └── main.py              # Full analysis pipeline (LCA, grouping, summaries)
    │
    ├── requirements.txt         # Python dependencies
    └── README.md                # Project documentation

------------------------------------------------------------------------

## 🧩 Features

### ✔ Data Loading & Cleaning

-   Fetch dataset from UC Irvine ML repository\
-   Filter invalid transactions\
-   Handle missing Customer IDs\
-   Create revenue, frequency, monetary features

### ✔ Visualization Suite

Includes: - Monthly sales trends\
- Top/Bottom revenue countries\
- Customer purchase distribution\
- Model selection criteria plots (AIC, BIC, CAIC)

### ✔ Latent Class Analysis (LCA)

-   Automated multiple‑K testing (2--8 classes)\
-   Model selection using information criteria\
-   Mixed data descriptor (continuous + categorical)\
-   Final segmentation with **StepMix**

### ✔ Customer Segment Summary

-   Revenue\
-   Average basket size\
-   Number of purchases\
-   Country distribution\
-   Segment size proportions

------------------------------------------------------------------------

## 🚀 How to Run the Project

### 1. Clone the repository

``` bash
git clone https://github.com/yourusername/OnlineRetailCustomerLCA.git
cd OnlineRetailCustomerLCA
```

### 2. Install dependencies

``` bash
pip install -r requirements.txt
```

### 3. Run the main analysis

``` bash
python src/main.py
```

### 4. View notebook

Open the notebook:

``` bash
jupyter notebook notebooks/lca.ipynb
```

------------------------------------------------------------------------

## 📦 Requirements

Main libraries: - `pandas` - `matplotlib` - `seaborn` - `ucimlrepo` -
`scikit-learn` - `stepmix`

Install them with:

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## 📈 Results Interpretation

Once the LCA model is fitted, the project outputs: - Best number of
customer classes\
- Segment assignments for each customer\
- Summary tables for each class\
- Visual illustrations of differences

This enables: - Precision marketing campaigns\
- Behavioral‑based segmentation\
- Strategy for retention and revenue growth\
- Country‑specific targeting

------------------------------------------------------------------------

## 🧪 Extending the Project

You can enhance this repository by: - Adding RFM features\
- Testing hierarchical LCA\
- Running LCA per region\
- Comparing K-means vs LCA segments\
- Deploying the segmentation with an API

If you'd like help implementing any of the above, I can add the code
structure.

------------------------------------------------------------------------

## 📄 License

MIT License (recommended).\
If you want, I can generate a LICENSE file for you.

------------------------------------------------------------------------

## 🤝 Contributions

Pull requests are welcome.\
For major changes, please open an issue first to discuss what you'd like
to modify.

------------------------------------------------------------------------

## 🙋 About

This project was created to build a **clean, production‑ready
repository** based on an exploratory notebook.\
If you'd like help deploying it on GitHub or improving its
modularization, just ask!

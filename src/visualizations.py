# Visualization functions

def plot_monthly_sales():
    # Apply a nicer style
    sns.set(style="whitegrid")

    # Create a copy to avoid modifying original df
    df_plot = df_filtered.copy()

    # Ensure the date column is datetime
    df_plot['InvoiceDate'] = pd.to_datetime(df_plot['InvoiceDate'], errors='coerce')
    df_plot = df_plot.dropna(subset=['InvoiceDate'])

    # Set date as index for resampling
    df_plot = df_plot.set_index('InvoiceDate')

    # Compute monthly sales (sum of Total_Price)
    monthly_sales = df_plot['Total_Price'].resample('M').sum()

    # Plot
    plt.figure(figsize=(15, 7))
    plt.plot(monthly_sales.index, monthly_sales.values)

    plt.title('Monthly Sales Over Time', fontsize=18)
    plt.xlabel('Date', fontsize=14)
    plt.ylabel('Total Revenue (Millions)', fontsize=14)

    # Format Y-axis in millions
    ax = plt.gca()
    ax.yaxis.set_major_formatter(
        ticker.FuncFormatter(lambda y, pos: f'{y/1_000_000:.1f}M')
    )

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_monthly_sales()

def plot_countries_revenue():
    # Style
    sns.set(style="whitegrid")

    # Copy df to avoid modifying original
    df_plot = df_filtered.copy()

    # Ensure column name is correct
    # (No renaming needed since your column is Total_price)

    # Group by country and sum total revenue
    country_sales = (
        df_plot.groupby('Country')['Total_Price']
            .sum()
            .sort_values(ascending=True)   # ascending=True for horizontal bars
    )

    # Plot
    plt.figure(figsize=(12, 12))
    plt.barh(country_sales.index, country_sales.values)

    plt.title("Total Revenue by Country", fontsize=18)
    plt.xlabel("Total Revenue (Millions)", fontsize=14)
    plt.ylabel("Country", fontsize=14)

    # Format axis in millions (M)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{x/1_000_000:.1f}M'))

    plt.tight_layout()
    plt.show()

plot_countries_revenue()

def plot_bot_rev_countries():
    # Style
    sns.set(style="whitegrid")

    # Copy df
    df_plot = df_filtered.copy()

    # Group by country and sum revenue
    country_sales = (
        df_plot.groupby('Country')['Total_Price']
            .sum()
            .sort_values(ascending=True)
    )

    # Select bottom 10
    bottom_10 = country_sales.head(20)

    # Formatter to use dots as thousand separator
    def dot_thousand(x, pos):
        return f"{int(x):,}".replace(",", ".")

    # Plot
    plt.figure(figsize=(12, 8))
    plt.barh(bottom_10.index, bottom_10.values)

    plt.title("Bottom 10 Countries by Total Revenue", fontsize=18)
    plt.xlabel("Total Revenue", fontsize=14)
    plt.ylabel("Country", fontsize=14)

    # Apply the formatter
    ax = plt.gca()
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(dot_thousand))

    plt.tight_layout()
    plt.show()
    
plot_bot_rev_countries()

def plot_model_selection_variables():
    plt.figure(figsize=(12, 6))
    plt.plot(model_comparison["Classes"], model_comparison["AIC"], marker='o', label="AIC")
    plt.plot(model_comparison["Classes"], model_comparison["BIC"], marker='o', label="BIC")
    plt.plot(model_comparison["Classes"], model_comparison["CAIC"], marker='o', label="CAIC")
    plt.plot(model_comparison["Classes"], model_comparison["SABIC"], marker='o', label="SABIC")

    plt.title("Model Selection for Latent Class Analysis")
    plt.xlabel("Number of Classes")
    plt.ylabel("Information Criterion Value")
    plt.legend()
    plt.grid(True)
    plt.show()

plot_model_selection_variables()

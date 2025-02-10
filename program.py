# Step 1: Read Company Data
companyDatas = open("companies.csv", "r")
historicalDatas = open("historical_prices.csv", "r")

# Dictionaries to store data
companies = {}  # Stores company details
stockPrices = {}  # Stores stock price history
monthly_returns = {}  # Stores calculated monthly returns

# Skip headers
next(companyDatas)
next(historicalDatas)

# Read company data
for line in companyDatas:
    parts = line.strip().split(",")

    compTickers = parts[0]   # Stock symbol (e.g., AAPL)
    compNames = parts[1]     # Company name (e.g., Apple Inc.)
    compSectors = parts[2]   # Sector (e.g., Technology)
    
    # Store company data in a dictionary
    companies[compTickers] = {"name": compNames, "sector": compSectors}

# Read historical stock prices
for line in historicalDatas:
    parts = line.strip().split(",")

    compTickers = parts[0]  # Stock symbol
    dates = parts[1]  # Date of stock price
    closingPrice = float(parts[2])  # Convert price to float

    # Ensure each company has a list for storing price history
    if compTickers not in stockPrices:
        stockPrices[compTickers] = []  

    # Store price history as (date, closing price)
    stockPrices[compTickers].append((dates, closingPrice))

# Close files
companyDatas.close()
historicalDatas.close()

# Step 3: Calculate Monthly Returns
for ticker, price_list in stockPrices.items():
    price_list.sort()  # Ensure prices are sorted by date
    monthly_returns[ticker] = []  # Initialize list for storing monthly returns

    for i in range(1, len(price_list)):  # Start from second month
        prev_date, prev_price = price_list[i - 1]  # Previous month
        curr_date, curr_price = price_list[i]  # Current month

        # Calculate monthly return percentage
        monthly_return = ((curr_price - prev_price) / prev_price) * 100
        monthly_returns[ticker].append((curr_date, round(monthly_return, 2)))  # Store rounded result

# Print Monthly Returns
print("\n📊 Monthly Returns:")
for ticker, returns in monthly_returns.items():
    print(f"{ticker}:")
    for date, percent in returns:
        print(f"  {date}: {percent}%")

# Step 4: Calculate Average Monthly Return per Sector
sector_returns = {}  # Dictionary to store sector-wise returns

for ticker, returns in monthly_returns.items():
    sector = companies[ticker]["sector"]  # Get the sector of the company
    
    # Ensure sector key exists
    if sector not in sector_returns:
        sector_returns[sector] = []

    # Store all returns in the sector
    for _, percent in returns:
        sector_returns[sector].append(percent)

# Compute and Print Sector Averages
print("\n📈 Sector-Wise Average Monthly Returns:")
for sector, returns in sector_returns.items():
    avg_return = sum(returns) / len(returns)  # Compute average
    print(f"{sector}: {round(avg_return, 2)}%")
# 📊 Stock Performance Analyzer

A Python program to analyze **stock performance** and compute **monthly sector returns** based on historical price data.

---

## 🚀 Features
✅ Reads **company details** from `companies.csv`  
✅ Reads **historical stock prices** from `historical_prices.csv`  
✅ Calculates **monthly return** for each company  
✅ Computes **average monthly return per sector**  
✅ Displays a **formatted summary report**  

---

## 📂 File Structure
```
StockPerformanceAnalyzer/
│── companies.csv               # Company details (Ticker, Name, Sector)
│── historical_prices.csv       # Historical stock prices (Date, Ticker, Price)
│── stock_analyzer.py           # Main Python script
│── README.md                   # Project documentation
```

---

## 📥 Input Format  
### **📜 `companies.csv`**
```
Ticker,Company Name,Sector
AAPL,Apple Inc.,Technology
MSFT,Microsoft Corporation,Technology
GOOGL,Alphabet Inc.,Technology
JPM,JPMorgan Chase & Co.,Finance
BAC,Bank of America Corporation,Finance
XOM,ExxonMobil Corporation,Energy
```


### **📜 `historical_prices.csv`**
```
Ticker,Date,Closing Price
AAPL,2024-01-31,180.00
AAPL,2024-02-29,190.00
AAPL,2024-03-31,185.00
MSFT,2024-01-31,320.00
MSFT,2024-02-29,330.00
MSFT,2024-03-31,310.00
JPM,2024-01-31,150.00
JPM,2024-02-29,155.00
JPM,2024-03-31,157.00
```


---

## ⚡ How It Works
1. **Reads `companies.csv`** → Stores company names & sectors.  
2. **Reads `historical_prices.csv`** → Extracts stock price history.  
3. **Calculates Monthly Returns** → Uses the formula:
   Monthly Return = (New Price - Old Price)/Old Price x 100
4. **Computes Sector-Wise Returns** → Averages monthly returns by sector.  
5. **Displays Results** → Prints stock performance and sector insights.  

---

## 📊 Example Output
```
📈 Monthly Returns:
AAPL: 2024-02-29: 5.56% 2024-03-31: -2.63%
MSFT: 2024-02-29: 3.13% 2024-03-31: -6.06%
```
```
📈 Sector-Wise Average Monthly Returns:
Technology: 0.51%
Finance: 1.93%
Energy: 3.66%
```

---

## 👨‍💻 Author
- **Emir Ucgun**  
- GitHub: [github.com/Emirucgun](https://github.com/Emirucgun)


---

🎉 **Enjoy analyzing stock performance with Python!** 🚀

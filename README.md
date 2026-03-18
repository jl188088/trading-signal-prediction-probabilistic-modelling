# Trading Signal Prediction using Probabilistic Modeling

<img width="1536" height="1024" alt="structure" src="https://github.com/user-attachments/assets/e55c3f5f-f407-48df-88c4-9538b5d653e7" />

## Overview
This project implements an end-to-end data science pipeline for predicting trading signals from financial time-series data. It integrates data ingestion, feature engineering, probabilistic machine learning, and risk modeling to generate actionable insights for decision-making.

The system is designed to reflect real-world data science workflows, emphasizing reproducibility, interpretability, and modular architecture.

---

## Problem Statement
Financial markets exhibit complex and time-dependent behavior, making reliable signal generation challenging. Traditional approaches often lack probabilistic confidence and integrated risk awareness.

This project addresses these limitations by:

- Modeling price movement as a probabilistic classification task
- Incorporating volatility-based risk assessment
- Producing interpretable outputs for decision support

---

## Methodology

### Data Ingestion
Historical market data is retrieved via API and stored for processing.

### Data Processing
Data is cleaned, sorted chronologically, and prepared for time-series analysis.

### Feature Engineering
Derived features include:

- Returns
- Moving averages (SMA)
- Momentum
- Rolling volatility

### Modeling
A Hidden Markov Model (HMM) is used to capture probabilistic market regimes and generate state-based signals.

### Risk Modeling
Risk is quantified using:

- Rolling volatility
- Value-at-Risk (VaR)

Risk is categorized into:

- Low
- Medium
- High

### Portfolio Optimization
- Multi-asset portfolio allocation using PyPortfolioOpt
- Optimal weights maximize expected return for a given risk

### Backtesting & Metrics
- Strategy returns
- Sharpe ratio
- Maximum drawdown
  
---

## Project Structure


 ```javascript
 
trading-signal-prediction/
├── data/
│   ├── raw/               ── Raw CSV/API downloads
│   └── processed/         ── Cleaned and preprocessed data
│
├── notebooks/
│   ├── data_exploration.ipynb      ── Explore raw data
│   ├── feature_engineering.ipynb   ── Test & visualize features
│   └── backtesting.ipynb           ── Backtest strategies
│
├── src/
│   ├── data/             ── Fetching & preprocessing scripts
│   ├── features/         ── Feature engineering (returns, SMA, momentum)
│   ├── models/           ── Probabilistic models (HMM, Bayesian)
│   ├── risk/             ── Risk scoring & probabilistic risk modeling
│   ├── signals/          ── Signal generation logic
│   ├── portfolio/        ── Multi-asset portfolio optimization
│   └── trading/          ── Trading API wrappers & execution
│
├── models/
│   ├── hmm.pkl           ── Hidden Markov Model
│   └── portfolio.pkl     ── Optimized portfolio weights
│
├── configs/
│   └── config.yaml       ── Main pipeline & trading config
│
├── outputs/
│   ├── predictions.csv   ── Latest model predictions
│   └── backtest.csv      ── Historical backtesting results
│
├── dashboard/
│   ├── app.py            ── Streamlit dashboard
│   └── components/       ── Custom UI components (charts, metrics)
│
├── main.py               ── Run full offline pipeline
├── main_live.py          ── Run live trading simulation
├── requirements.txt      ── Python dependencies
└── README.md             ── Project documentation
};
```

---

## Technology Stack

- Python
- PySpark
- Pandas / NumPy
- Scikit-learn
- hmmlearn (Hidden Markov Models)
- PyPortfolioOpt (Portfolio optimization)
- Streamlit (Dashboard)
- yFinance / Alpaca API

---

## Pipeline Workflow

1. Data ingestion  
2. Data preprocessing  
3. Feature engineering  
4. Probabilistic modeling (HMM)  
5. State prediction & probability calculation  
6. Risk classification (VaR & volatility)  
7. Portfolio optimization (multi-asset)  
8. Backtesting & metrics computation  
9. Trading signal generation  
10. Visualization & dashboard

---
## Output
The system generates:

- Trading signals (Buy/Sell)
- Probability scores
- Risk levels (Low/Medium/High)
- Portfolio allocation per asset
- Backtesting metrics: Sharpe ratio, drawdowns
- Interpretable insights
  
## Future Work
- Real-time data streaming
- Advanced models (XGBoost, deep learning, reinforcement learning)
- Multi-asset portfolio optimization
- Interactive backtesting dashboard

## Author
Jayalle Pangilinan

---

### Install Dependencies
```bash
pip install -r requirements.txt

# Run Full Pipeline
python main.py

# Run Live Trading Simulation
python main_live.py

# Launch Dashboard
streamlit run dashboard/app.py

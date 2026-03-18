# Trading Signal Prediction using Probabilistic Modeling

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

### Output
The system generates:

- Trading signal (Buy/Sell)
- Prediction probability
- Risk classification
- Portfolio allocation
- Text-based insights

---

## Project Structure


trading-signal-prediction/
│
├── data/ # Raw and processed market data
├── notebooks/ # Jupyter notebooks for exploration, modeling, and backtesting
├── src/ # Source code modules
│ ├── data/
│ ├── features/
│ ├── models/
│ ├── risk/
│ ├── signals/
│ ├── portfolio/
│ └── trading/
├── models/ # Saved trained models (HMM, portfolio, etc.)
├── configs/ # YAML configuration files
├── outputs/ # Generated predictions, backtest results, metrics
├── dashboard/ # Streamlit dashboard
├── main.py # Run full pipeline (offline)
├── main_live.py # Run live trading simulation
├── requirements.txt # Python dependencies
└── README.md # Project documentation


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

## Usage

### Install Dependencies
```bash
pip install -r requirements.txt
Run Full Pipeline
python main.py
Run Live Trading Simulation
python main_live.py
Launch Dashboard
streamlit run dashboard/app.py
Output

Trading signals (Buy/Sell)

Probability scores

Risk levels (Low/Medium/High)

Portfolio allocation per asset

Backtesting metrics: Sharpe ratio, drawdowns

Interpretable insights

Future Work

Real-time data streaming

Advanced models (XGBoost, deep learning, reinforcement learning)

Multi-asset portfolio optimization

Interactive backtesting dashboard

## Author

Jayalle Pangilinan
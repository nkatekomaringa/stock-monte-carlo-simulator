# Monte Carlo Stock Price Forecaster & Portfolio Risk Pipeline

An end-to-end Python quantitative finance pipeline that fetches historical market data using `yfinance`, models asset price dynamics using **Geometric Brownian Motion (GBM)**, and runs **Monte Carlo simulations** to forecast future price distributions and estimate portfolio **Value at Risk (VaR)** and **Conditional VaR (CVaR)**.

## Features
- **Data Acquisition**: Flexible historical stock & ETF price fetching via `yfinance`.
- **Statistical Drift & Volatility**: Log-return calculations with drift adjustment ($ drift = \mu - \frac{1}{2}\sigma^2 $).
- **Monte Carlo Engine**: Vectorized multi-path price simulation across customizable time horizons (e.g., 30, 90, 252 trading days).
- **Risk Metrics**: Calculates median target price, 90% & 95% confidence intervals, 5% Value at Risk (VaR), and Expected Shortfall (CVaR).
- **Visualization**: Modular plotting functions for simulation trajectories and terminal price histograms.

## Project Structure
```text
stock-monte-carlo-forecaster/
├── README.md
├── requirements.txt
├── .gitignore
├── config.yaml
├── data/
│   └── README.md
├── notebooks/
│   └── monte_carlo_exploration.ipynb
└── src/
    ├── __init__.py
    ├── data_loader.py
    ├── simulation.py
    ├── metrics.py
    └── main.py
```

## Getting Started

### Prerequisites
```bash
pip install -r requirements.txt
```

### Run Simulation
```bash
python -m src.main
```

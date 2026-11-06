import yaml
from src.data_loader import MarketDataLoader
from src.simulation import MonteCarloSimulator
from src.metrics import calculate_risk_metrics

def main():
    with open("config.yaml", "r") as f:
        config = yaml.safe_load(f)["simulation"]

    ticker = config["ticker"]
    print(f"Fetching historical data for {ticker}...")
    loader = MarketDataLoader(ticker=ticker, period=config["period"])
    prices = loader.fetch_data()
    log_returns = loader.get_log_returns(prices)
    last_price = float(prices.iloc[-1])

    print(f"Running {config['num_simulations']} Monte Carlo simulations for {config['forecast_days']} trading days...")
    simulator = MonteCarloSimulator(
        forecast_days=config["forecast_days"],
        num_simulations=config["num_simulations"],
        seed=config.get("random_seed", 42)
    )
    price_paths = simulator.run_simulation(last_price, log_returns)

    results = calculate_risk_metrics(price_paths, last_price, config["confidence_level"])

    print("
================ FORECAST RESULTS ================")
    print(f"Ticker Symbol:               {ticker}")
    print(f"Current Stock Price:         ${results['current_price']:.2f}")
    print(f"1-Year Median Target Price:  ${results['median_target']:.2f}")
    print(f"1-Year Mean Target Price:    ${results['mean_target']:.2f}")
    print(f"95% Confidence Interval:     [${results['lower_bound']:.2f} - ${results['upper_bound']:.2f}]")
    print(f"95% 1-Year Value at Risk:    ${results['var_95']:.2f}")
    print(f"95% Conditional VaR (CVaR):  ${results['cvar_95']:.2f}")
    print("==================================================
")

if __name__ == "__main__":
    main()

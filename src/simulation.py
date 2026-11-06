import numpy as np
import pandas as pd

class MonteCarloSimulator:
    def __init__(self, forecast_days: int = 252, num_simulations: int = 10000, seed: int = None):
        self.forecast_days = forecast_days
        self.num_simulations = num_simulations
        if seed is not None:
            np.random.seed(seed)

    def run_simulation(self, last_price: float, log_returns: pd.Series) -> np.ndarray:
        """Runs Geometric Brownian Motion (GBM) Monte Carlo simulation."""
        mu = log_returns.mean()
        var = log_returns.var()
        sigma = log_returns.std()
        
        # Calculate daily drift (adjusted for volatility drag)
        drift = mu - (0.5 * var)
        
        # Generate random normal shocks (days x simulations)
        daily_shocks = np.random.normal(0, 1, (self.forecast_days, self.num_simulations))
        daily_returns = np.exp(drift + sigma * daily_shocks)
        
        # Construct price trajectories
        price_paths = np.zeros_like(daily_returns)
        price_paths[0] = last_price
        
        for t in range(1, self.forecast_days):
            price_paths[t] = price_paths[t - 1] * daily_returns[t]
            
        return price_paths

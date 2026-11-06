import numpy as np

def calculate_risk_metrics(price_paths: np.ndarray, last_price: float, confidence_level: float = 0.95) -> dict:
    """Calculates key statistical and risk metrics from final terminal prices."""
    terminal_prices = price_paths[-1]
    
    alpha = (1.0 - confidence_level) * 100
    p_lower = np.percentile(terminal_prices, alpha)
    p_upper = np.percentile(terminal_prices, 100 - alpha)
    
    # Value at Risk (VaR) and Expected Shortfall (CVaR)
    simulated_returns = (terminal_prices - last_price) / last_price
    var_threshold = np.percentile(simulated_returns, alpha)
    cvar = simulated_returns[simulated_returns <= var_threshold].mean()
    
    return {
        "current_price": last_price,
        "mean_target": float(np.mean(terminal_prices)),
        "median_target": float(np.median(terminal_prices)),
        "lower_bound": float(p_lower),
        "upper_bound": float(p_upper),
        "var_95": float(-var_threshold * last_price),
        "cvar_95": float(-cvar * last_price)
    }

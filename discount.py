def apply_discount(price, percent):
    """Return the price after taking `percent` % off."""
    if percent < 0 or percent > 100:
        raise ValueError("percent must be between 0 and 100")
    return price - price * percent / 100

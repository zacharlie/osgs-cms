def str_to_bool(s: str) -> bool:
    """Return bool for whether the provided string is truthy or falsy."""
    s = str(s)
    if s.lower() in ["true", "1", "t", "y", "yes", "on", "positive"]:
        return True
    if s.lower() in ["false", "0", "f", "n", "no", "off", "negative"]:
        return False
    else:
        return None

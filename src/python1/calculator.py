def add(a: float, b: float) -> float:
    """Add two numbers.

    Args:
        a: First number.
        b: Second number.
    Returns:
        The sum of a and b.
    """
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a.

    Args:
        a: Number to subtract from.
        b: Number to subtract.
    Returns:
        The difference a - b.
    """
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers.

    Args:
        a: First factor.
        b: Second factor.
    Returns:
        The product of a and b.
    """
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Args:
        a: Dividend.
        b: Divisor; must not be zero.
    Returns:
        Quotient as a float.
    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

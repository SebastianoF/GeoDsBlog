import numpy as np
from logger_custom_formatter import get_logger

logger = get_logger(__file__)


def special_division(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        if a == 0:
            logger.warning("Zero numerator and denominator found. Returning zero")
            return 0
        if a > 0:
            logger.warning("Zero denominator found. Returning + infinity")
            return np.inf
        else:
            logger.warning("Zero denominator found. Returning - infinity")
            return -1 * np.inf

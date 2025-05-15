import logging

def setup_logger(name: str = None, level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger(name)

    if not logger.handlers:
        # Установка уровня логирования
        numeric_level = getattr(logging, level.upper(), logging.INFO)
        logger.setLevel(numeric_level)

        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

        handler = logging.StreamHandler()
        handler.setFormatter(formatter)

        logger.addHandler(handler)

    return logger
import logging
from pathlib import Path

# Create logs directory if it doesn't exist
Path("logs").mkdir(parents=True, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler(),
    ],
)

# Create the application logger
logger = logging.getLogger("enterprise_etl")


def get_logger():
    """
    Returns the configured application logger.
    """
    return logger
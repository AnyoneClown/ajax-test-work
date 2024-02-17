import logging
import sys

logger = logging
logger.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] : [%(levelname)8s]: %(message)s",
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler(sys.stdout),
    ],
)

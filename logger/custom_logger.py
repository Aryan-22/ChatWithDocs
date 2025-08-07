import os
import logging
from datetime import datetime

class CustomLogger:
    def __init__(self):
        self.logs_dir = os.path.join(os.getcwd(), "logs")
        os.makedirs(self.logs_dir, exist_ok=True)

        LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
        LOG_FILE_PATH = os.path.join(self.logs_dir, LOG_FILE)

        logging.basicConfig(
            filename=LOG_FILE_PATH,
            format="[%(asctime)s] - %(levelname)s %(name)s (line:%(lineno)d)- %(message)s",
            level=logging.INFO
        )

    def get_logger(self, name=__file__):
        return logging.getLogger(os.path.basename(name))


if __name__ == "__main__":
    custom_logger = CustomLogger()
    logger = custom_logger.get_logger(__file__)
    logger.info("Custom logger is initialized")

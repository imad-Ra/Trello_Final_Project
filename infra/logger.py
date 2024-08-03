import logging


class Logger:
    logging.basicConfig(filename="../logger.log",
                        level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")

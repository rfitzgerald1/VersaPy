from logging_config import logger

def main():
    logger.info("Application started.")
    logger.warning("This is a warning.")
    logger.error("This is an error.")

if __name__ == "__main__":
    main()

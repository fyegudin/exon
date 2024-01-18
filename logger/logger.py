import logging

# Create a logger
logger = logging.getLogger(__name__)

# Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
logger.setLevel(logging.DEBUG)

# Create a file handler and set the logging level for the file
file_handler = logging.FileHandler('example.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler and set the logging level for the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and add it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)


# Example usage
def example_function():
    try:
        result = 1 / 0
    except Exception as e:
        logger.exception("An error occurred: %s", str(e))



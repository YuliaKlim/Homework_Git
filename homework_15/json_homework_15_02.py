import json
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("json_login")

file_handler = logging.FileHandler('json_homework_15.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def json_valid_or_not(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            json.load(file)
        return True
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
        return False
    except json.JSONDecodeError as e:
        logger.error(f"File error in {file_path}: {e}")
        return False

if json_valid_or_not('login.json'):
    logger.info("JSON 'login' is valid")
else:
    logger.error("JSON 'login' is not valid")




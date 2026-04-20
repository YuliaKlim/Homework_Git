import xml.etree.ElementTree as ET
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger("xml_login")

file_handler = logging.FileHandler('xml_homework_15.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

def find_timingExbytes_incoming(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    for group in root.findall('group'):
        number = group.find('number')
        if number is not None:
            logger.info(f"Number: {number.text}")
        else:
            logger.info(f"Number not found")

        timing_exbytes = group.find('timingExbytes')
        if timing_exbytes is not None:
            incoming = timing_exbytes.find('incoming')
            if incoming is not None:
                logger.info(f"Incoming timing: {incoming.text}")
            else:
                logger.info(f"Incoming timing: Not found")
        else:
            logger.info(f"timingExbytes: not found")

find_timingExbytes_incoming('groups.xml')
logger.info('Search completed')
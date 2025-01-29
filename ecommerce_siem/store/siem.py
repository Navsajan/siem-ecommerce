import logging
import os

log_dir = 'logs'
log_file_path = os.path.join(log_dir, 'siem.log')

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger('siem')
handler = logging.FileHandler(log_file_path)
formatter = logging.Formatter('%(asctime)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_event(event):
    logger.info(event)

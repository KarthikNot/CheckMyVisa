import logging
import os
from datetime import datetime
from from_root import from_root

log_file_name = f"{datetime.now().strftime('%Y_%m_%d__%H_%M_%S_')}.log"
logs_dir = 'logs'
logs_path = os.path.join(from_root(), logs_dir, log_file_name)

os.makedirs(logs_dir, exist_ok=True)

logging.basicConfig(
    filename = logs_path,
    level = logging.DEBUG,
    format = '%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
)
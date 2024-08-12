import logging
import os
import sys
from datetime import datetime

# Define the log file name based on the current date and time
log_file = f"log_{datetime.now().strftime('%m_%d_%Y_%H-%M-%S')}.log"

logs_path=os.path.join(os.getcwd(),"logs",log_file)
os.makedirs(logs_path,exist_ok=True)
log_file_path = os.path.join(logs_path,log_file)

logging.basicConfig(
    filename=log_file_path ,
    format='[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)



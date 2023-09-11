import os
import sys
from src.mlProject.exception import CustomException
from src.mlProject.logger import logging
import pandas as pd
from dataclasses import dataclass



@dataclass
class DataIngestionConfig:
    train_data_path:str = os.path.join('artifacts', 'train.csv')
    test_data_path:str = os.path.join('artifacts', 'test.csv')
    raw_data_path:str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()


    def initate_data_ingestion(self):
        try:
            # Reading Code
            logging.info("Reading from mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

        except Exception as e:
            raise CustomException(e, sys)
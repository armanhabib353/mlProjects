import os
import sys
from src.mlProject.exception import CustomException
from src.mlProject.logger import logging
import pandas as pd
from dataclasses import dataclass
from src.mlProject.utils import read_sql_data
from sklearn.model_selection import train_test_split



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
            df = read_sql_data() # this is from utils.py data
            logging.info("Reading Completed mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index_label=False, header=True)
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index_label=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index_label=False, header=True)

            logging.info("Data ingestion is completed")
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)
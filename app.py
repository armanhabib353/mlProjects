from src.mlProject.logger import logging
from src.mlProject.exception import CustomException
import sys


if __name__=="__main__":
     logging.info("The execution has started")

     try:
          a = 1/0
     except Exception as e:
          raise CustomException(e, sys)
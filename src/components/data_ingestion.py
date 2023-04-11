import os
import sys #for system error 
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass #used to create variables inside classes without using constructors and when there is no functions we can use it


## initialize the data ingestion configuration
# a class which will contain all the path of the data

@dataclass
class DataIngestionconfig:
    train_data_path:str=os.path.join('artifacts',"train.csv")
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

# create a class for data ingestion

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionconfig()

    def initiate_data_ingestion(self):
        logging.info('Data ingestion methods Starts')
        try:
            df=pd.read_csv('notebook/data/gemstone.csv') # ./ is to go to home dir
            logging.info("Dataset read as pandas dataFrame")
            os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info("Train test split")
            train_set,test_set=train_test_split(df,test_size=0.30)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info('Ingestion of data is completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )


        except Exception as e:
            logging.info('Exception occured at Data Ingestion Stage ')
            raise CustomException(e,sys)
        

# run data ingestion

if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()




        


import sys
import pandas as pd
import numpy as np
from typing import Optional
from CheckMyVisa.logger import logging
from CheckMyVisa.constants import DATABASE_NAME
from CheckMyVisa.exception import CheckMyVisaException
from CheckMyVisa.configuration.mongo_connection import MongoDBClient



class VisaData:
    """
    This class help to export entire mongo db record as pandas dataframe
    """

    def __init__(self):
        """
        """
        try:
            self.mongo_client = MongoDBClient(database_name = DATABASE_NAME)
        except Exception as e:
            logging.error(CheckMyVisaException(e,sys))
        

    def export_collection_as_dataframe(self, collection_name : str, database_name : Optional[str] = None)->pd.DataFrame:
        """
        Exports an entire MongoDB collection as a pandas DataFrame.

        Args:
            collection_name (str): The name of the collection to export.
            database_name (Optional[str]): The name of the database. Defaults to None, using the initialized database.

        Returns:
            pd.DataFrame: A DataFrame containing the collection data.
        """
        try:
            if database_name is None:
                collection = self.mongo_client.database[collection_name]
            else:
                collection = self.mongo_client[database_name][collection_name]

            df = pd.DataFrame(list(collection.find()))
            if "_id" in df.columns.to_list():
                df = df.drop(columns=["_id"], axis=1)
            df.replace({"na":np.nan},inplace=True)
            return df
        except Exception as e:
            logging.error(CheckMyVisaException(e,sys))
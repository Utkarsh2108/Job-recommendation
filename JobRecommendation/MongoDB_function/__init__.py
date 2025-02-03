from JobRecommendation.config import client
import pandas as pd
from  JobRecommendation.exception import jobException
import sys
import os,io,time,datetime



def get_collection_as_dataframe(file_path: str) -> pd.DataFrame:
    """
    Description: This function returns the data from a CSV file as a Pandas DataFrame.
    =========================================================
    Params:
    file_path: Path to the CSV file
    =========================================================
    Returns:
    Pandas DataFrame of the CSV file content
    """
    try:
        # Read the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        return df
    except Exception as e:
        raise Exception(f"Error while reading data from CSV: {e}")




import csv
import os

def resume_store(data, file_path: str):
    """
    Store the data in a CSV file.

    Args:
        data (dict): Data to be stored.
        file_path (str): Path to the CSV file.
    """
    try:
        # Check if the file already exists
        file_exists = os.path.isfile(file_path)

        # Open the file in append mode and write data
        with open(file_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())

            # Write the header if the file does not exist
            if not file_exists:
                writer.writeheader()

            # Write the data
            writer.writerow(data)

    except Exception as e:
        raise Exception(f"Error while storing data in CSV: {e}")

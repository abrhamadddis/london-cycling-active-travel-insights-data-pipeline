from google.cloud import storage
import dlt
import pandas as pd
from io import StringIO
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def load_csv_to_bigquery(bucket_name, directory):
    """
    Loads all CSV files from a specified directory in a Google Cloud Storage bucket
    into a BigQuery table using the dlt pipeline.

    Args:
        bucket_name (str): The name of the Google Cloud Storage bucket.
        directory (str): The directory path within the bucket to look for CSV files.
    """
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=directory)

    # Initialize your dlt pipeline
    pipeline = dlt.pipeline(
        pipeline_name="data-ingestion-pipeline",
        destination='bigquery',
        dataset_name="cycle_dataset"
    )
    for blob in blobs:
        if not blob.name.endswith('.csv'):
            print(f"Skipping non-CSV file: {blob.name}")
            continue
        print(f"Processing file: {blob.name}")
        data = blob.download_as_text()
        df = pd.read_csv(StringIO(data))
        load_info = pipeline.run(df, table_name="raw_cycle_data", write_disposition="append", schema_contract="evolve")
        print(f"Loaded data from {blob.name} into BigQuery.")

if __name__ == "__main__":
    # Get bucket name and directory from environment variables
    bucket_name = os.getenv("BUCKET_NAME")
    directory = os.getenv("DIRECTORY")

    if not bucket_name or not directory:
        print("Error: BUCKET_NAME or DIRECTORY environment variables are not set.")
    else:
        load_csv_to_bigquery(bucket_name, directory)
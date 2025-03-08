import os,sys,numpy as np, pandas as pd

TARGET_COLUMN="Result"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="NetworkData.csv"
TRAIN_FILE_NAME:str="train.csv"
TEST_FILE_NAME:str="test.csv"
DATA_INGESTION_COLLECTION_NAME:str="NetworkData"
DATA_INGESTION_DATABASE_NAME:str="KA837"
DATA_INGESTION_DIR_NAME:str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_NAME:str="feature_store"
DATA_INGESTION_INGESTED_DIR:str="INGESTED"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION:float=0.2
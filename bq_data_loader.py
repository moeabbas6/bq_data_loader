#!/usr/bin/env python3

import time
import os
import uuid
from google.cloud import bigquery
import pandas as pd
from datetime import datetime

client = bigquery.Client()

source_file_name = os.path.basename(__file__)

job_id = str(uuid.uuid4())

sql_statements = [
    "YOUR_SQL_COMMAND_1_HERE;",
    "YOUR_SQL_COMMAND_2_HERE;",
    "YOUR_SQL_COMMAND_3_HERE;"
]

data = []

total_start_time = time.time()

for sql_command in sql_statements:
    start_time = time.time()
    query_job = client.query(sql_command)
    query_job.result()
    elapsed_time = time.time() - start_time
    _loaded_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    statement_id = str(uuid.uuid4())

    data.append({
        'job_id': job_id,
        'statement_id': statement_id,
        'source_file': source_file_name,
        'sql_statement': sql_command.strip(),
        'elapsed_time_seconds': round(elapsed_time, 2),
        '_loaded_at': _loaded_at
    })

    print(f"Executed: {sql_command}")
    print(f"Elapsed Time: {elapsed_time:.2f} seconds\n")

df = pd.DataFrame(data)

bq_table_id = "YOUR_BIGQUERY_TABLE_ID_HERE"

job = client.load_table_from_dataframe(df, bq_table_id)

job.result()

total_elapsed_time = time.time() - total_start_time

print(f"Total Elapsed Time for all SQL commands and DataFrame load: {total_elapsed_time:.2f} seconds")

print("All SQL commands executed and data appended to BigQuery table successfully.")
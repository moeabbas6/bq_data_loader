
# BigQuery Data Loader

`bq_data_loader.py` is a Python script designed to execute a batch of SQL commands on Google BigQuery, track execution times, and log the results into a specified BigQuery table for auditing and monitoring purposes.

## Features

- Execute multiple SQL commands in BigQuery.
- Log execution details, including elapsed time, for each SQL statement.
- Track the execution using unique job and statement IDs.
- Automatically log the results into a specified BigQuery table.
- Fully configurable for various SQL commands and output destinations.

## Requirements

- Python 3.6+
- Google Cloud BigQuery client library (`google-cloud-bigquery`)
- Pandas (`pandas`)
- PyArrow (`pyarrow`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/bq_data_loader.git
   cd bq_data_loader
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

   **Note:** Ensure you have the `google-cloud-bigquery`, `pandas`, and `pyarrow` libraries installed.

4. Set up your Google Cloud credentials:

   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account-file.json"
   ```

5. Make the Script Executable:

   ```bash
   chmod +x bq_data_loader.py
   ```

## Usage

1. Customize the script by editing the following sections in `bq_data_loader.py`:
   - **SQL Statements:** Modify the `sql_statements` list to include your SQL commands.
   - **BigQuery Table ID:** Set the `bq_table_id` variable to the table where you want to log the results.

   Example:

   ```python
   sql_statements = [
       "YOUR_SQL_COMMAND_1_HERE;",
       "YOUR_SQL_COMMAND_2_HERE;",
       "YOUR_SQL_COMMAND_3_HERE;"
   ]

   bq_table_id = "your_project.your_dataset.your_table"
   ```

2. Run the script:

   ```bash
   ./bq_data_loader.py
   ```

3. The script will execute each SQL command, log the execution details, and append the results to your specified BigQuery table. The total execution time will be printed in the terminal.

## Example

Here is an example of how you might configure the script:

```python
sql_statements = [
    "CREATE OR REPLACE TABLE `project.dataset.customers` AS (SELECT * FROM `project.dataset.customers_v`);",
    "CREATE OR REPLACE TABLE `project.dataset.orders` AS (SELECT * FROM `project.dataset.orders_v`);"
]

bq_table_id = "project.dataset.execution_logs"
```

## Contributing

Feel free to open an issue or submit a pull request if you have any improvements or suggestions!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

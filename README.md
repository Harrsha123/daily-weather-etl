Daily Weather ETL Project
📝 Overview
This project is a fully automated, modular ETL (Extract, Transform, Load) pipeline built in Python. It fetches the daily weather forecast for College Park, MD from the Open-Meteo API, cleans and processes the data using Pandas, and saves the output to a CSV file.

The entire process is designed to be run automatically on a daily schedule, with the resulting data pushed to this GitHub repository to create a daily log of weather forecasts.

✨ Features
Modular Design: The ETL logic is separated into distinct scripts for extraction (extract.py), transformation (transform.py), and loading (load.py), making the code clean and easy to maintain.

Automated Execution: A main pipeline.py script orchestrates the entire ETL flow from start to finish.

Git Automation: Includes a shell script (run_and_commit.sh) that runs the pipeline and then automatically adds, commits, and pushes the new data file to GitHub.

Data Enrichment: The transformation step adds valuable calculated columns, such as the daily temperature range.

Cleanliness: Automatically handles the creation and deletion of intermediate files.

🛠️ Technologies Used
Python

Pandas: For all data manipulation and transformation.

Requests: For fetching data from the web API.

Git & GitHub: For version control and automated data logging.

Cron (or Task Scheduler): For scheduling the daily execution of the pipeline.


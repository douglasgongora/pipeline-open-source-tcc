import argparse
import sys
import subprocess
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_script(script_name):
    subprocess.run(["python3", script_name], check=True)

def run_soda_scan_schema():
    try:
        result = subprocess.run(
            [
                "soda",
                "scan",
                "-d",
                "conn_postgres",
                "-c",
                "./contracts/configuration.yml",
                "./contracts/checks.yml",
            ],
            capture_output=True,
            text=True,
        )
        print("STDOUT:")
        print(result.stdout)
        print("STDERR:")
        print(result.stderr)

        # If the command was successful (exit code 0), return True
        return result.returncode == 0

    except subprocess.CalledProcessError as e:
        logging.error(f"Soda scan failed: {e}")
        return False

if __name__ == "__main__":
    if run_soda_scan_schema():
        # Call to run the diff tables validation
        run_script("extract_csv.py")
        run_script("extract_db.py")
        run_script("load.py")
    else:
        logging.error("ETL process skipped due to Soda scan failure.")

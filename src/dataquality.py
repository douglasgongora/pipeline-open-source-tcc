import argparse
import sys
import subprocess

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

        # Verificar o código de retorno do processo
        if result.returncode != 0:
            print(f"Command failed with return code {result.returncode}", file=sys.stderr)

    except subprocess.CalledProcessError as e:
        print(f"Error running soda scan: {e}", file=sys.stderr)
        sys.exit(1)

run_soda_scan_schema()
#!/usr/bin/env python3

import pandas as pd
import argparse
import os
from datetime import datetime

VERSION = "1.0"

def main():
    # -----------------------------
    # CLI Argument Parser
    # -----------------------------
    parser = argparse.ArgumentParser(
        description="Convert JIRA Excel to Worktop Format"
    )

    parser.add_argument("--input", help="Path to JIRA Excel file")
    parser.add_argument("--output", help="Output file path (optional)")
    parser.add_argument("--version", action="store_true")

    args = parser.parse_args()

    # -----------------------------
    # Handle Version
    # -----------------------------
    if args.version:
        print(f"Worktop Formatter Version: {VERSION}")
        return

    # -----------------------------
    # Validate Input
    # -----------------------------
    if not args.input:
        print("❌ Error: --input is required")
        return

    jira_file = args.input

    if not os.path.exists(jira_file):
        raise FileNotFoundError(f"Input file does not exist: {jira_file}")

    # -----------------------------
    # Output File Handling
    # -----------------------------
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    if args.output:
        output_file = args.output
    else:
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        output_file = os.path.join(
            downloads_folder,
            f"formatted_worktop_output_{timestamp}.xlsx"
        )

    # -----------------------------
    # Read Excel
    # -----------------------------
    df_jira = pd.read_excel(jira_file)

    # -----------------------------
    # Validate Columns
    # -----------------------------
    required_columns = ["Issue key", "Summary", "Description"]

    missing_cols = [col for col in required_columns if col not in df_jira.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in JIRA file: {missing_cols}")

    # -----------------------------
    # Transform
    # -----------------------------
    df_output = pd.DataFrame()

    df_output["user_story_id"] = df_jira["Issue key"]
    df_output["user_story_title"] = df_jira["Summary"]
    df_output["description"] = df_jira["Description"]

    df_output["datasource_project_name"] = "Timely Quote User Stories"
    df_output["work_item_type"] = "story"

    # -----------------------------
    # Save Output
    # -----------------------------
    df_output.to_excel(output_file, index=False, engine="openpyxl")

    print(f"\n✅ File created successfully:\n{output_file}")


# ✅ THIS LINE IS VERY IMPORTANT
if __name__ == "__main__":
    main()
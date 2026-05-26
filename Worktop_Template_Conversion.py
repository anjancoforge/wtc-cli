import pandas as pd
from datetime import datetime

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# -----------------------------
# Input file paths
# -----------------------------
jira_file = r"C:\Users\Anjani.Chejarla\Downloads\JIRA User Stories.xlsx"
output_file = f"formatted_worktop_output_{timestamp}.xlsx"

# -----------------------------
# Read JIRA Excel
# -----------------------------
df_jira = pd.read_excel(jira_file)

# -----------------------------
# Validate required columns
# -----------------------------
required_columns = ["Issue key", "Summary", "Description"]

missing_cols = [col for col in required_columns if col not in df_jira.columns]
if missing_cols:
    raise ValueError(f"Missing columns in JIRA file: {missing_cols}")

# -----------------------------
# Create formatted dataframe
# -----------------------------
df_output = pd.DataFrame()

df_output["user_story_id"] = df_jira["Issue key"]
df_output["user_story_title"] = df_jira["Summary"]
df_output["description"] = df_jira["Description"]

# Static values
df_output["datasource_project_name"] = "Timely Quote User Stories"
df_output["work_item_type"] = "story"

# -----------------------------
# Save to Excel
# -----------------------------
df_output.to_excel(output_file, index=False, engine="openpyxl")

print(f"✅ File successfully created: {output_file}")
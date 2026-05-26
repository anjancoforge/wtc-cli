from wtc.main import convert
import pandas as pd
import os

def test_convert(tmp_path):
    file = tmp_path / "input.xlsx"

    df = pd.DataFrame({
        "Issue key": ["ABC-1"],
        "Summary": ["Test"],
        "Description": ["Desc"]
    })

    df.to_excel(file, index=False)

    output = convert(str(file))
    assert os.path.exists(output)
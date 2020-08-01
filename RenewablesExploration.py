import pandas as pd
import numpy as np

filename="bp-stats-review-2020-all-data.xlsx"
# Load, Clean, Rename, Fillna, Dropna, Reset index
#All pages are formatted the same so we can use same execution for each page we read through pandas
RenCon_df = pd.read_excel(filename, sheet_name= "Renewables Consumption - EJ", header=2)[1:-9].rename(columns={"Exajoules (input-equivalent)": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country")
RenGen_df=pd.read_excel(filename, sheet_name="Renewables Power - Twh", header=2)[1:-9].rename(columns={"Terawatt-hours": "Country"}).dropna(axis="index", how="all").fillna(0).fillna(0).set_index("Country")

import pandas as pd
import numpy as np

filename="bp-stats-review-2020-all-data.xlsx"
# Load, Clean, Rename, Fillna, Dropna, Reset index
#All pages are formatted the same so we can use same execution for each page we read through pandas
RenCon_df = pd.read_excel(filename, sheet_name= "Renewables Consumption - EJ", header=2)[1:-9].rename(columns={"Exajoules (input-equivalent)": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country")
RenGen_df=pd.read_excel(filename, sheet_name="Renewables Power - Twh", header=2)[1:-9].rename(columns={"Terawatt-hours": "Country"}).dropna(axis="index", how="all").fillna(0).fillna(0).set_index("Country")


GenBySource_df = pd.read_excel(filename, sheet_name="Renewables Generation by source", header=0).dropna(axis="index", how="all").fillna(0).fillna(0)
GenBySource_df.to_csv("RenewablesGenerationBySource.csv")

SolarConsumptionDF = pd.read_excel(filename, sheet_name= "Solar Consumption - EJ", header=2)[1:-9].rename(columns={"Exajoules (input-equivalent)": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country").drop(["2019.1", "2008-18", "2019.2", "Unnamed: 59","Unnamed: 60"], axis=1)
SolarConsumptionDF.to_csv("SolarConsumption.csv")

WindConsumptionDF = pd.read_excel(filename, sheet_name= "Wind Consumption - EJ", header=2)[1:-9].rename(columns={"Exajoules (input-equivalent)": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country").drop(["2019.1", "2008-18", "2019.2", "Unnamed: 59","Unnamed: 60"], axis=1)
WindConsumptionDF.to_csv("WindConsumption.csv")

SolarGenerationDF = pd.read_excel(filename, sheet_name= "Solar Generation - TWh", header=2)[1:-9].rename(columns={"Terawatt-hours": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country").drop(["2019.1", "2008-18", "2019.2", "Unnamed: 59","Unnamed: 60"], axis=1)
SolarGenerationDF.to_csv("SolarGeneration.csv")

WindGenerationDF = pd.read_excel(filename, sheet_name= "Wind Generation -TWh", header=2)[1:-9].rename(columns={"Terawatt-hours": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country").drop(["2019.1", "2008-18", "2019.2", "Unnamed: 59","Unnamed: 60"], axis=1)
WindGenerationDF.to_csv("WindGeneration.csv")

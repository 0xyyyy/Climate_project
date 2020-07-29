import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load, Clean, Rename, Fillna, Dropna, Reset index
RenCon_df = pd.read_excel("bp-stats-review-2020-all-data.xlsx", sheet_name= "Renewables Consumption - EJ", header=2 )[1:-9].rename(columns={"Exajoules (input-equivalent)": "Country"}).dropna(axis="index", how="all").fillna(0).set_index("Country")

# Take out Regional values from csv rowsLittle more cleaning
TotalRegion_df=RenCon_df[RenCon_df.index.str.startswith("Total")]
TotalRegion_df.index.name = "Region"
RegionalPlotData=TotalRegion_df.drop(["2019.2", "2008-18", "2019.1"], axis=1)
RegionalPlotData


# Plotting Regional Time Series Data
Transposed=RegionalPlotData.transpose().drop(index=["Unnamed: 59", "Unnamed: 60"]) #Transpose for spaghetti plot data maniuplation

# Convert values to arrays for matplotlib intake
x=np.asarray(Transposed.index)
y=np.asarray(Transposed.values)
# For each Region(column) plot a separate line based on the numpy arrays, format plot
for column in RegionalPlotData:
    plt.plot(x, y, marker='', linewidth=1, alpha=0.9, label=column)
    plt.title("Renewable Energy Consumption Through The Years")
    plt.xlabel("Years")
    plt.ylabel("Consumption (Exajoules)")
    plt.legend(Transposed.columns)

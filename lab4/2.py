import pandas as pd


df = pd.read_csv("countries_population.csv")


number_columns = ["Population", "Population Growth", "Growth Rate (%)"]

for column in number_columns:
    country_mean = df.groupby("Country")[column].transform("mean")
    df[column] = df[column].fillna(country_mean)

print('Количество NaN', df.isna().sum())

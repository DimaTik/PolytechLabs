import pandas as pd


df = pd.read_csv("countries_population.csv")

nan_count = df.isna().sum()
print(nan_count)
print()

max_nan_column = nan_count.idxmax()
max_nan_value = nan_count.max()

print(max_nan_column, "-", max_nan_value)

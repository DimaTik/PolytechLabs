import pandas as pd


df = pd.read_csv("countries_population.csv")


last_year = int(df["Year"].max())
first_year_10 = last_year - 9

last_10_growth_rows = []

for country in df["Country"].unique():
    one_country = df[df["Country"] == country]
    start_row = one_country[one_country["Year"] == first_year_10]
    end_row = one_country[one_country["Year"] == last_year]

    if len(start_row) > 0 and len(end_row) > 0:
        start_population = start_row.iloc[0]["Population"]
        end_population = end_row.iloc[0]["Population"]
        growth_percent = (end_population - start_population) / start_population * 100
        last_10_growth_rows.append([country, growth_percent])

last_10_growth_df = pd.DataFrame(last_10_growth_rows)
last_10_growth_df.columns = ["Country", "Growth Percent"]
last_10_growth_df = last_10_growth_df.sort_values("Growth Percent", ascending=False)

print(last_10_growth_df.head(3))
print()

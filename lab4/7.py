import pandas as pd


df = pd.read_csv("countries_population.csv")

best_country = ""
best_start_year = 0
best_end_year = 0
best_growth = 0

for country in df["Country"].unique():
    one_country = df[df["Country"] == country]
    one_country = one_country.sort_values("Year")
    years = one_country["Year"].tolist()
    populations = one_country["Population"].tolist()

    for i in range(0, len(years) - 2):
        growth = populations[i + 2] - populations[i]

        if growth > best_growth:
            best_growth = growth
            best_country = country
            best_start_year = int(years[i])
            best_end_year = int(years[i + 2])

print(best_country, best_start_year, "-", best_end_year, int(best_growth))
print()

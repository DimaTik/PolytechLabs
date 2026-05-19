import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("countries_population.csv")

min_decline_rows = []

for country in df["Country"].unique():
    one_country = df[df["Country"] == country]
    min_index = one_country["Growth Rate (%)"].idxmin()
    min_row = one_country.loc[min_index]
    min_decline_rows.append(min_row)

min_decline_df = pd.DataFrame(min_decline_rows)
year_count = min_decline_df["Year"].value_counts()
decline_year = int(year_count.idxmax())

print(decline_year)

decline_countries = min_decline_df[min_decline_df["Year"] == decline_year]
decline_country_names = decline_countries["Country"].tolist()

start_year = decline_year - 10
end_year = decline_year + 10

plt.figure(figsize=(12, 6))

for country in decline_country_names:
    one_country = df[df["Country"] == country]
    one_country = one_country[one_country["Year"] >= start_year]
    one_country = one_country[one_country["Year"] <= end_year]
    plt.plot(one_country["Year"], one_country["Growth Rate (%)"], label=country)

plt.xlabel("Год")
plt.ylabel("Прирост населения, %")
plt.title("Страны с максимальной убылью около " + str(decline_year) + " года")
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()

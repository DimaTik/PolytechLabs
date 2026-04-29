import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("countries_population.csv")

countries_a = df[df["Country"].str.startswith("A")]
countries_a_2000 = countries_a[countries_a["Year"] == 2000]

max_population_index = countries_a_2000["Population"].idxmax()
min_population_index = countries_a_2000["Population"].idxmin()

max_population_country = countries_a_2000.loc[max_population_index, "Country"]
min_population_country = countries_a_2000.loc[min_population_index, "Country"]

print("Наибольшее население в 2000 году:", max_population_country)
print("Наименьшее население в 2000 году:", min_population_country)
print()

max_country_data = df[df["Country"] == max_population_country]
max_country_data = max_country_data[max_country_data["Year"] >= 1995]
max_country_data = max_country_data[max_country_data["Year"] <= 2005]

min_country_data = df[df["Country"] == min_population_country]
min_country_data = min_country_data[min_country_data["Year"] >= 1995]
min_country_data = min_country_data[min_country_data["Year"] <= 2005]

plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(
    max_country_data["Year"],
    max_country_data["Population"],
    label=max_population_country,
)
plt.xlabel("Год")
plt.ylabel("Население")
plt.title("Наибольшее население среди A")
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(
    min_country_data["Year"],
    min_country_data["Population"],
    label=min_population_country,
    color="orange",
)
plt.xlabel("Год")
plt.ylabel("Население")
plt.title("Наименьшее население среди A")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

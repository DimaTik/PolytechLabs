import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("countries_population.csv")

data_2007 = df[df["Year"] == 2007]
data_2007 = data_2007.sort_values("Population", ascending=False)
top_5_2007 = data_2007.head(5)

world_population_2007 = data_2007["Population"].sum()

top_5_names = top_5_2007["Country"]
top_5_parts = top_5_2007["Population"] / world_population_2007 * 100

for country, part in zip(top_5_names, top_5_parts):
    print(country, "-", round(part, 2), "%")
print()

plt.figure(figsize=(8, 8))
plt.pie(top_5_parts, labels=top_5_names, autopct="%1.1f%%")
plt.title("Доля населения пяти самых населенных стран в 2007 году")
plt.tight_layout()
plt.show()

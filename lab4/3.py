import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("countries_population.csv")


df["Abs Growth Rate (%)"] = df["Growth Rate (%)"].abs()
max_growth_index = df["Abs Growth Rate (%)"].idxmax()
max_growth_row = df.loc[max_growth_index]

max_growth_country = max_growth_row["Country"]
max_growth_year = int(max_growth_row["Year"])
max_growth_value = max_growth_row["Growth Rate (%)"]

print(max_growth_country, max_growth_year, max_growth_value)

country_data = df[df["Country"] == max_growth_country]

plt.figure(figsize=(10, 5))
plt.plot(
    country_data["Year"],
    country_data["Growth Rate (%)"],
    color="green",
    label=max_growth_country,
)
plt.xlabel("Год")
plt.ylabel("Прирост населения, %")
plt.title("Динамика прироста населения: " + max_growth_country)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

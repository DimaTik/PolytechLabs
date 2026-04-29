import os

import pandas as pd
import matplotlib.pyplot as plt


# Читаем данные из файла.
df = pd.read_csv("../lab4/countries_population.csv")

# Создаем папку для графиков, если ее еще нет.
plots_folder = "plots"

if not os.path.exists(plots_folder):
    os.mkdir(plots_folder)


print("Первые строки таблицы:")
print(df.head())
print()


# 1. Считаем количество NAN в каждом столбце.
print("1. Количество NAN в каждом столбце:")
nan_count = df.isna().sum()
print(nan_count)
print()

max_nan_column = nan_count.idxmax()
max_nan_value = nan_count.max()

print("Столбец с самым большим количеством NAN:")
print(max_nan_column, "-", max_nan_value)
print()


# 2. Заполняем NAN средним значением по стране.
# Заполняем только числовые столбцы, потому что среднее считается по числам.
number_columns = ["Population", "Population Growth", "Growth Rate (%)"]

for column in number_columns:
    country_mean = df.groupby("Country")[column].transform("mean")
    df[column] = df[column].fillna(country_mean)

print("2. Количество NAN после заполнения:")
print(df.isna().sum())
print()


# В таблице есть строки не только по странам, но и по группам стран.
# Для заданий про страны убираем такие общие группы.
not_countries = [
    "Arab World",
    "Caribbean small states",
    "Central Europe and the Baltics",
    "Early-demographic dividend",
    "East Asia & Pacific",
    "East Asia & Pacific (IDA & IBRD countries)",
    "East Asia & Pacific (excluding high income)",
    "Euro area",
    "Europe & Central Asia",
    "Europe & Central Asia (IDA & IBRD countries)",
    "Europe & Central Asia (excluding high income)",
    "European Union",
    "Fragile and conflict affected situations",
    "Heavily indebted poor countries (HIPC)",
    "High income",
    "IBRD only",
    "IDA & IBRD total",
    "IDA blend",
    "IDA only",
    "IDA total",
    "Late-demographic dividend",
    "Latin America & Caribbean",
    "Latin America & Caribbean (excluding high income)",
    "Latin America & the Caribbean (IDA & IBRD countries)",
    "Least developed countries: UN classification",
    "Low & middle income",
    "Low income",
    "Lower middle income",
    "Middle East & North Africa",
    "Middle East & North Africa (IDA & IBRD countries)",
    "Middle East & North Africa (excluding high income)",
    "Middle income",
    "North America",
    "OECD members",
    "Other small states",
    "Pacific island small states",
    "Post-demographic dividend",
    "Pre-demographic dividend",
    "Small states",
    "South Asia",
    "South Asia (IDA & IBRD)",
    "Sub-Saharan Africa",
    "Sub-Saharan Africa (IDA & IBRD countries)",
    "Sub-Saharan Africa (excluding high income)",
    "Upper middle income",
    "World",
]


# 3. Страна с самым большим годовым приростом или убылью в процентах.
df["Abs Growth Rate (%)"] = df["Growth Rate (%)"].abs()
countries_df = df[~df["Country"].isin(not_countries)]

max_growth_index = countries_df["Abs Growth Rate (%)"].idxmax()
max_growth_row = countries_df.loc[max_growth_index]

max_growth_country = max_growth_row["Country"]
max_growth_year = int(max_growth_row["Year"])
max_growth_value = max_growth_row["Growth Rate (%)"]

print("3. Самый большой годовой прирост или убыль в процентах:")
print(max_growth_country, max_growth_year, round(max_growth_value, 2), "%")
print()

country_data = df[df["Country"] == max_growth_country]

plt.figure(figsize=(10, 5))
plt.plot(
    country_data["Year"],
    country_data["Growth Rate (%)"],
    color="green",
    linestyle="--",
    label=max_growth_country,
)
plt.xlabel("Год")
plt.ylabel("Прирост населения, %")
plt.title("Динамика прироста населения: " + max_growth_country)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plots_folder, "task_3_growth_rate.png"))


# 4. Среди стран на букву A ищем максимум и минимум населения за 2000 год.
countries_a = countries_df[countries_df["Country"].str.startswith("A")]
countries_a_2000 = countries_a[countries_a["Year"] == 2000]

max_population_index = countries_a_2000["Population"].idxmax()
min_population_index = countries_a_2000["Population"].idxmin()

max_population_country = countries_a_2000.loc[max_population_index, "Country"]
min_population_country = countries_a_2000.loc[min_population_index, "Country"]

print("4. Страны на букву A:")
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
plt.savefig(os.path.join(plots_folder, "task_4_countries_a.png"))


# 5. Доля населения пяти самых населенных стран в 2007 году.
data_2007 = countries_df[countries_df["Year"] == 2007]
data_2007 = data_2007.sort_values("Population", ascending=False)
top_5_2007 = data_2007.head(5)

world_population_2007 = data_2007["Population"].sum()

top_5_names = top_5_2007["Country"]
top_5_parts = top_5_2007["Population"] / world_population_2007 * 100

print("5. Доли пяти самых населенных стран в 2007 году:")
for country, part in zip(top_5_names, top_5_parts):
    print(country, "-", round(part, 2), "%")
print()

plt.figure(figsize=(8, 8))
plt.pie(top_5_parts, labels=top_5_names, autopct="%1.1f%%")
plt.title("Доля населения пяти самых населенных стран в 2007 году")
plt.tight_layout()
plt.savefig(os.path.join(plots_folder, "task_5_top_5_2007.png"))


# 6. Год, когда у наибольшего количества стран была максимальная убыль.
# Для каждой страны берем год с минимальным процентом прироста.
min_decline_rows = []

for country in df["Country"].unique():
    one_country = countries_df[countries_df["Country"] == country]

    if len(one_country) == 0:
        continue

    min_index = one_country["Growth Rate (%)"].idxmin()
    min_row = one_country.loc[min_index]
    min_decline_rows.append(min_row)

min_decline_df = pd.DataFrame(min_decline_rows)
year_count = min_decline_df["Year"].value_counts()
decline_year = int(year_count.idxmax())

print("6. Год, когда у наибольшего количества стран была максимальная убыль:")
print(decline_year)
print()

decline_countries = min_decline_df[min_decline_df["Year"] == decline_year]
decline_country_names = decline_countries["Country"].tolist()

start_year = decline_year - 10
end_year = decline_year + 10

plt.figure(figsize=(12, 6))

for country in decline_country_names:
    one_country = countries_df[countries_df["Country"] == country]
    one_country = one_country[one_country["Year"] >= start_year]
    one_country = one_country[one_country["Year"] <= end_year]
    plt.plot(one_country["Year"], one_country["Growth Rate (%)"], label=country)

plt.xlabel("Год")
plt.ylabel("Прирост населения, %")
plt.title("Страны с максимальной убылью около " + str(decline_year) + " года")
plt.legend(fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plots_folder, "task_6_decline_year.png"))


# 7. Страна и окно в 3 года с самым большим ростом населения.
best_country = ""
best_start_year = 0
best_end_year = 0
best_growth = 0

for country in countries_df["Country"].unique():
    one_country = countries_df[countries_df["Country"] == country]
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

print("7. Самый большой рост населения за окно в 3 года:")
print(best_country, best_start_year, "-", best_end_year, int(best_growth))
print()


# Вариант 1.
# 2.1. Три страны с максимальным приростом населения в процентах за последние 10 лет.
last_year = int(countries_df["Year"].max())
first_year_10 = last_year - 9

last_10_growth_rows = []

for country in countries_df["Country"].unique():
    one_country = countries_df[countries_df["Country"] == country]
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

print("Вариант 1. 2.1. Три страны с максимальным приростом за последние 10 лет:")
print(last_10_growth_df.head(3))
print()


# Вариант 1.
# 2.2. Три страны с максимальной убылью населения в абсолютных значениях.
last_10_loss_df = last_10_growth_df.sort_values("Growth Percent", ascending=True)

print("Вариант 1. 2.2. Три страны с максимальной убылью за последние 10 лет:")
print(last_10_loss_df.head(3))
print()


# Вариант 2.
# 2.1. Нестабильность считаем как стандартное отклонение темпов роста.
first_year_20 = last_year - 19
last_20 = countries_df[countries_df["Year"] >= first_year_20]
unstable = last_20.groupby("Country")["Growth Rate (%)"].std()
unstable = unstable.sort_values(ascending=False)

print("Вариант 2. 2.1. Самые нестабильные темпы роста за последние 20 лет:")
print(unstable.head(5))
print()


# Вариант 2.
# 2.2. Разница в приросте населения между Китаем и Индией.
china = countries_df[countries_df["Country"] == "China"]
india = countries_df[countries_df["Country"] == "India"]

china_india = pd.merge(
    china[["Year", "Growth Rate (%)"]],
    india[["Year", "Growth Rate (%)"]],
    on="Year",
    suffixes=(" China", " India"),
)

china_india["Difference"] = (
    china_india["Growth Rate (%) China"] - china_india["Growth Rate (%) India"]
).abs()

china_india = china_india.sort_values("Difference", ascending=False)

print("Вариант 2. 2.2. Годы с наибольшей разницей между Китаем и Индией:")
print(china_india.head(5))
print()

plt.figure(figsize=(10, 5))
plt.plot(china["Year"], china["Growth Rate (%)"], label="China")
plt.plot(india["Year"], india["Growth Rate (%)"], label="India")
plt.xlabel("Год")
plt.ylabel("Прирост населения, %")
plt.title("Сравнение темпов роста населения Китая и Индии")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig(os.path.join(plots_folder, "variant_2_china_india.png"))


# Общий вывод.
print("Вывод:")
print("В разных странах динамика населения отличается.")
print("В странах с быстрым ростом населения прирост обычно держится положительным.")
print("В некоторых странах бывают периоды убыли, которые хорошо видны по отрицательным значениям.")
print("Самые населенные страны дают большую часть населения мира.")
print("Сравнение Китая и Индии показывает, что даже у крупных стран темпы роста могут сильно различаться.")


plt.show()

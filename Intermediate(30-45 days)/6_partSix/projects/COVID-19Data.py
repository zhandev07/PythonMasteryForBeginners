from matplotlib import pyplot as plt
import requests
import pandas as pd

url = "https://api.covid19api.com/summary"
response = requests.get(url)
covid_data = response.json()["Countries"]
df = pd.DataFrame(covid_data)
print("Data Snapshot:\n", df.head())

# Select relevant columns and clean
df = df[["Country", "TotalConfirmed", "TotalDeaths", "TotalRecovered", "Date"]]
df.dropna(inplace=True)  # Remove rows with missing values
df["Date"] = pd.to_datetime(df["Date"]).dt.date  # Convert Date to datetime
print("Cleaned Data Snapshot:\n", df.head())

# Plot top 10 countries by confirmed cases
top_countries = df.nlargest(10, "TotalConfirmed")
plt.barh(top_countries["Country"], top_countries["TotalConfirmed"], color="purple")
plt.xlabel("Total Confirmed Cases")
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.show()
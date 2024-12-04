from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the Wikipedia page
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"
driver.get(url)

# Locate the table and extract data
table = driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/table[1]')
rows = table.find_elements(By.TAG_NAME, 'tr')

data = []
for row in rows:
    cols = row.find_elements(By.TAG_NAME, 'td')
    cols = [col.text.strip() for col in cols]
    if cols:
        data.append(cols)

# Close the browser
driver.quit()

# Inspect the data for mismatched rows
max_columns = max(len(row) for row in data)
print(f"Max columns in data: {max_columns}")

# Adjust columns dynamically
columns = ["Rank", "Country/Territory", "Population", "Percentage of World", "Date", "Source"]
if len(columns) < max_columns:
    columns.extend([f"Extra_{i}" for i in range(len(columns), max_columns)])

# Convert to DataFrame
df = pd.DataFrame(data, columns=columns[:len(data[0])])

# Save to CSV
df.to_csv('countries_population.csv', index=False)

# Display the DataFrame
print(df)
print(df.head())

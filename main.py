import pandas as pd
import sqlite3

# Extract
data = {
    "id": [1, 2, 3, 3],
    "name": ["Navitha", "Nancy", None, "Naina"],
    "salary": [70000, 80000, 75000, 75000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Transform (clean data)
df = df.drop_duplicates()
df = df.dropna()

print("\nCleaned Data:")
print(df)

# Load
conn = sqlite3.connect("employees.db")
df.to_sql("employees", conn, if_exists="replace", index=False)

# Validate
result = pd.read_sql("SELECT * FROM employees", conn)
print("\nData from DB:")
print(result)

conn.close()

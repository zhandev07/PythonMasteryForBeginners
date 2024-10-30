# import pandas as pd

# # Sample dataset with missing values
# data = {
#     "Name": ["Alice", "Bob", None, "David", "Eve"],
#     "Age": [24, None, 22, 19, None],
#     "Score": [88, 92, None, 77, 85]
# }
# df = pd.DataFrame(data)

# # Fill missing names with "Unknown" and age with the mean age
# df["Name"].fillna("Unknown", inplace=True)
# df["Age"].fillna(df["Age"].mean(), inplace=True)
# df.dropna(subset=["Score"], inplace=True)  # Drop rows where Score is missing

# print("Cleaned DataFrame:\n", df)

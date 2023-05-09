# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# pd.set_option("display.max_rows", 1000)
# pd.set_option("display.max_columns", 1000)
# pd.set_option("display.width", 1000)

# Load the dataset into a DataFrame
df = pd.read_csv("2017_Yellow_Taxi_Trip_Data.csv")

# Print the first 10 rows of the DataFrame
print(df.head(10))

# Print information about the DataFrame, including column data types and number of non-null values
print(df.info())

# Print descriptive statistics of the DataFrame, including count, mean, std, min, max, and quartiles
print(df.describe())

# Sort the DataFrame by the "trip_distance" column in descending order
print(df.sort_values(by=["trip_distance"], ascending=False))

# Sort the DataFrame by the "total_amount" column in descending order, and print the top 20 and bottom 20 rows
df_sort_total_amount = df.sort_values(by=["total_amount"], ascending=False)
print(df_sort_total_amount.head(20))
print(df_sort_total_amount.tail(20))

# Print the counts of unique values in the "payment_type" column
print(df["payment_type"].value_counts())

# Compute the average tip amount for credit card payments, and print the result
avg_cc_tip = df[df["payment_type"] == 1]["tip_amount"].mean()
print("Average cc tip: ", avg_cc_tip)

# Compute the average tip amount for cash payments, and print the result
avg_cash_tip = df[df["payment_type"] == 2]["tip_amount"].mean()
print("Average cash tip: ", avg_cash_tip)

# Print the counts of unique values in the "vendorID" column
print(df["VendorID"].value_counts())

# Print the mean total amount for each vendor
print(df.groupby(["VendorID"]).mean(numeric_only=True)[["total_amount"]])

# Filter the data for credit card payments only
credit_card_only = df[df["payment_type"] == 1]

# Print unique values in passenger count column for credit card payments only
print(credit_card_only["passenger_count"].value_counts())

# Calculate the average tip amount for each passenger count (credit card payments only)
print(
    credit_card_only.groupby(["passenger_count"]).mean(numeric_only=True)[
        ["tip_amount"]
    ]
)

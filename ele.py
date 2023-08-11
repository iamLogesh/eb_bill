import streamlit as st
import pandas as pd
import datetime
import os

# Define the cost per unit
cost_per_unit = 6

# Streamlit app title
st.title("Electric Bill Calculator")

# Input the number of units
units = st.number_input("Enter the number of units:", min_value=0, step=1, value=0)

# Calculate the total cost
total_cost = cost_per_unit * units

# Display the total cost
st.write(f"Total cost for {units} units: {total_cost}")

# Define the file path
csv_file_path = "electric_bill_data.csv"

# Save data to CSV
if st.button("Save to CSV"):
    # Get current date and time
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create a DataFrame
    data = {'Date': [current_datetime], 'Units': [units], 'Total Cost': [total_cost]}
    df = pd.DataFrame(data)

    # Append to the CSV file or create it if it doesn't exist
    if os.path.exists(csv_file_path):
        df.to_csv(csv_file_path, mode='a', index=False, header=False)
    else:
        df.to_csv(csv_file_path, index=False)

    st.success(f"Data saved to {csv_file_path}")

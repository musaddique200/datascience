import pandas as pd

# I made two simple DataFrames with IDs and some data.
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Name': ['Alice', 'Bob', 'Charlie']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Age': [25, 30, 35]
})

# I’m merging the DataFrames on the 'ID' column.
merged_df = pd.merge(df1, df2, on='ID')

# Now, I’m reshaping the merged data to show names and ages.
reshaped_df = merged_df.set_index('Name')

print("Merged DataFrame:")
print(merged_df)

print("\nReshaped DataFrame:")
print(reshaped_df)

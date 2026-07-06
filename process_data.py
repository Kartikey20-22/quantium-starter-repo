import pandas as pd
import glob
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_files = glob.glob(os.path.join(script_dir, 'data', '*.csv'))

print(f"Found files: {csv_files}")

dataframes = []

for file in csv_files:
    print(f"\nProcessing: {file}")
    df = pd.read_csv(file)

    # Filter Pink Morsel
    df = df[df['product'].str.contains('pink morsel', case=False, na=False)]

    # Remove $ from price and convert to float
    df['price'] = df['price'].str.replace('$', '', regex=False).astype(float)

    # Calculate sales
    df['Sales'] = df['quantity'] * df['price']

    # Keep only required columns
    df = df[['Sales', 'date', 'region']]
    df.columns = ['Sales', 'Date', 'Region']

    dataframes.append(df)

# Combine all
final_df = pd.concat(dataframes, ignore_index=True)

# Save output
output_path = os.path.join(script_dir, 'formatted_output.csv')
final_df.to_csv(output_path, index=False)

print(f"\n✅ Done! Total rows: {len(final_df)}")
print(final_df.head())
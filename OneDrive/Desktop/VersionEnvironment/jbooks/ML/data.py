import pandas as pd
import numpy as np
import os

# Set random seed for consistent data generation
np.random.seed(42)
n_rows = 200

# Unique options for categorical columns
property_types = ['Apartment', 'Villa', 'Townhouse', 'Duplex', 'Penthouse', 'Studio']
locations = ['Downtown', 'Suburbs', 'Beachfront', 'Financial District', 'Uptown', 'Green Valley']
statuses = ['Available', 'Pending', 'Sold', 'Under Offer']

# Construct the synthetic real estate dataframe
data = {
    'Property_ID': [f'PROP-{i:03d}' for i in range(1, n_rows + 1)],
    'Type': np.random.choice(property_types, n_rows),
    'Area_SqFt': np.random.randint(500, 5000, n_rows),
    'Bedrooms': np.random.randint(1, 7, n_rows),
    'Bathrooms': np.random.randint(1, 6, n_rows),
    'Price_USD': np.random.randint(100000, 3500000, n_rows),
    'Location': np.random.choice(locations, n_rows),
    'Year_Built': np.random.randint(1990, 2026, n_rows),
    'Status': np.random.choice(statuses, n_rows),
    'Agent_ID': [f'AGT-{np.random.randint(101, 116)}' for _ in range(n_rows)]
}

df = pd.DataFrame(data)

# Export data directly to a CSV file
output_filename = 'real_estate_properties.csv'
df.to_csv(output_filename, index=False)

print(f"Success! Created '{output_filename}' with {df.shape[0]} rows and {df.shape[1]} columns.")

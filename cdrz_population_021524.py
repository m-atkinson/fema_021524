import pandas as pd

# Define the path to the data files
path = "/path/to/your/data/"  # Modify this path to your data directory

# Load the first data file (NRI Table Census Tracts)
# Data retrieved from FEMA in February 2024
nri_file = 'NRI_Table_CensusTracts.csv'
df_nri = pd.read_csv(path + nri_file)

# Load the second data file (FEMA Community Disaster Resilience Zones)
cdrz_file = 'FEMA_Community_Disaster_Resilience_Zones_1769773669159817233.csv'
df_cdrz = pd.read_csv(path + cdrz_file)

# Merge the two dataframes on NRI_ID
merged_df = df_cdrz.merge(df_nri[['NRI_ID', 'POPULATION']], left_on='NRI ID', right_on='NRI_ID', how='left').drop('NRI_ID', axis=1)

# Calculate and print the total population living in Community Disaster Resilience Zones (CDRZs)
total_population = merged_df['POPULATION'].sum()
print(f"Total Population in CDRZs: {total_population}")
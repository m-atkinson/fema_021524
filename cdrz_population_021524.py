import pandas as pd
# path to data
path = "/path/to/your/data/"  # Modify this path to your data directory
path = "/Users/matthewatkinson/Desktop/dsci/"  # Modify this path to your data directory

# Load the first file (NRI Table Census Tracts)
# Data retrieved from FEMA in February 2024
nri_file = 'NRI_Table_CensusTracts.csv'
df_nri = pd.read_csv(path + nri_file)
# Load the second file (FEMA Community Disaster Resilience Zones)
cdrz_file = 'FEMA_Community_Disaster_Resilience_Zones_1769773669159817233.csv'
df_cdrz = pd.read_csv(path + cdrz_file)

# Merge the two dataframes on NRI_ID
merged_df = df_cdrz.merge(df_nri[['NRI_ID', 'POPULATION']], left_on='NRI ID', right_on='NRI_ID', how='left').drop('NRI_ID', axis=1)
# %% Population in CDRZ and Number of Counties

# Calculate and print the total population living in Community Disaster Resilience Zones (CDRZs)
total_population = merged_df['POPULATION'].sum()
print(f"Total Population in CDRZs: {total_population}")

# Calculate and print number counties in CDRZs
number_counties = merged_df['County'].nunique()
print(f"Number of Counties: {number_counties}")








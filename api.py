import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
import pandas as pd

# Base URL for the API query
base_url = "https://osdr.nasa.gov/osdr/data/search"
params = {
    "ffield": "organism",
    "fvalue": "Mus%20musculus",
    "ffield": "Study Assay Technology Type",
    "fvalue": "RNA%20Sequencing",
    "size": 100,
}

# Function to fetch results for a specific page
def fetch_page(start_index):
    params['from'] = start_index
    response = requests.get(base_url, params=params).json()
    return response['hits']['hits']

# Initial request 
initial_response = requests.get(base_url, params=params).json()
total_hits = initial_response['hits']['total']
total_pages = (total_hits + params['size'] - 1) // params['size']

results = []


# Use ThreadPoolExecutor to fetch pages concurrently
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(fetch_page, page * params['size']): page for page in range(total_pages)}
    
    for future in as_completed(futures):
        hits = future.result()
        for hit in hits:
            accession = hit['_source'].get('Accession')
            index = hit['_index']
            if accession:
                results.append({'Accession': accession, 'Index': index})



# Create a DataFrame from the results
df_optimized = pd.DataFrame(results)
print("Optimized Version DataFrame:")
print(df_optimized.describe())

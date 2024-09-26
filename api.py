import requests

#My query ----- Not from repo
url = f"https://osdr.nasa.gov/osdr/data/search?ffield=organism&fvalue=Mus%20musculus&ffield=Study%20Assay%20Technology%20Type&fvalue=RNA%20Sequencing"
#Note ffield and the corresponding ffvalue (used for filtering)


response = requests.get(url).json() #for getting json

#looping through json and get the OSDs
accession_ids = []

for hit in response['hits']['hits']:
    accession = hit['_source'].get('Accession')
    if accession:
        accession_ids.append(accession)

# Print the Accession IDs
print(accession_ids)

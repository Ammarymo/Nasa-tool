import requests
import json

"""
https://osdr.nasa.gov/osdr/data/osd/files/{OSD_STUDY_IDs}/?page={CURRENT_PAGE_NUMBER}&size={RESULTS_PER_PAGE}?all_files={ALL_FILES}
"""

#url = f"https://osdr.nasa.gov/bio/repo/search?q=mouse%20AND%20RNA-seq%20AND%20spaceflight&data_source=cgene"
url = f"https://osdr.nasa.gov/osdr/data/search?ffield=organism&fvalue=Mus%20musculus&ffield=Study%20Assay%20Technology%20Type&fvalue=RNA%20Sequencing"

filters = {"api_key":"Aw9D8rwi4j2aRhFPrGNVKYEiqozSYUaDdRb45Miq"}


response = requests.get(url).json()

accession_ids = []
for hit in response['hits']['hits']:
    accession = hit['_source'].get('Accession')
    if accession:
        accession_ids.append(accession)

# Print the Accession IDs
print(accession_ids)
#!/usr/bin/python3
# cerner_2^5_2020 / Cerner_2-5_2020 / Cerner_2_to_5_2020
import csv
import json
import requests
from pathlib import Path

# should grab most results but can be updated
search_parameter = 'cerner_2-5_2020'
github_api = 'https://api.github.com/search/repositories?q='
search_url = github_api + search_parameter
header = {'Accept': 'application/vnd.github.mercy-preview+json'}
delimiter_for_csv = ','  # splits the csv file with a comma
output_file = '2_5_Coding_Competition_Entries.csv'  # output file name

# pulls the data from GitHub
r = requests.get(search_url, headers=header).json()

# creates a new csv file
with open(output_file, 'w', newline='') as file:
    results = csv.writer(file, delimiter=delimiter_for_csv)
    results.writerow(['Entry', 'User', 'Repo Name', 'Link', 'Last Updated'])
    entry = 1
    # loops through all repos found for the 4 columns desired
    for repo in sorted(r['items'], key=lambda x: x['updated_at'], reverse=True):
        results.writerow([entry, repo['owner']['login'],
                          repo['name'], repo['html_url'], repo['updated_at']])
        entry += 1

print('All Done!')
print('File:', Path(output_file).absolute())

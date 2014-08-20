__author__ = 'maximk'

import json
import os

import authors_clustering

path_json = '/home/maximk/Work/metagenomics/metagenomics_papers.json'

if os.path.isfile(path_json):
    papers = json.load(open(path_json, 'r'))

authors = [paper['authors'] for paper in papers]
authors_list = authors_clustering.get_authors_list(authors)
authors_rating = authors_clustering.get_authors_ratings(authors, authors_list)

print('\n'.join(authors_list))
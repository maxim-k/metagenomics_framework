__author__ = 'maximk'

import json
import os

import authors_clustering

path_json = '/home/maximk/Work/metagenomics/metagenomics_papers.json'

papers = []
if os.path.isfile(path_json):
    papers = json.load(open(path_json, 'r'))

authors = [paper['authors'] for paper in papers]
authors_list = authors_clustering.get_authors_list(authors)
authors_rating = authors_clustering.get_authors_ratings(authors, authors_list)
adjacency_matrix = authors_clustering.get_adjacency_matrix(authors, authors_list)

path_adjacency = '/home/maximk/Work/metagenomics/authors_adjacency_matrix.json'
with open(path_adjacency, 'w') as adjacency_matrix_file:
    json.dump(adjacency_matrix, adjacency_matrix_file)

print('\n'.join('%s\t%s' % (key, value) for key, value in authors_rating.items()))

__author__ = 'maximk'

import json
import os

import authors_clustering
import keywords_processing
import abstracts_processing

path_json = '/home/maximk/Work/metagenomics/mendeley.json'

papers = []
if os.path.isfile(path_json):
    papers = json.load(open(path_json, 'r'))

authors = [paper['authors'] for paper in papers]
authors_list = authors_clustering.get_authors_list(authors)
authors_rating = authors_clustering.get_authors_ratings(authors, authors_list)
adjacency_matrix = authors_clustering.get_adjacency_matrix(authors, authors_list)

# path_adjacency = '/home/maximk/Work/metagenomics/authors_adjacency_matrix.json'
# with open(path_adjacency, 'w') as adjacency_matrix_file:
#     json.dump(adjacency_matrix, adjacency_matrix_file)

#print('\n'.join('%s\t%s' % (key, value) for key, value in authors_rating.items()))

keywords = [paper.get('keywords', '') for paper in papers]
keywords_list = keywords_processing.get_keywords_list(keywords)
keywords_rating = keywords_processing.get_keywords_ratings(keywords, keywords_list)
#print('\n'.join('%s\t%s' % (key, value) for key, value in keywords_rating.items()))

abstracts = [paper.get('abstract', '') for paper in papers]
abstracts_list = abstracts_processing.get_abstracts_list(abstracts)
conclusions = abstracts_processing.conclusioning(abstracts_list)
# print(conclusions)
counts = abstracts_processing.count_pairs(conclusions)
with open('/home/maximk/Work/metagenomics/conclusions_triplets_counts.tsv', 'w') as pairs_counts:
    pairs_counts.write('\n'.join(['%s\t%s' % (key, value) for key, value in counts.items()]))
#
# conclusions = open('/home/maximk/Work/metagenomics/abstract_conclusion_phrases.txt', 'r').read().lower().split(sep='\n')
# print(abstracts_processing.get_abstracts_conclusions(abstracts_list, conclusions), len(abstracts_list))
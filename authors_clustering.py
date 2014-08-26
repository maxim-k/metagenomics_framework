__author__ = 'maximk'

from collections import OrderedDict


def get_authors_list(authors_dict):
    """
    Get authors from Mendeley JSON; remove duplicates.
    """
    authors_list = set()
    for paper_authors in authors_dict:
        authors_list.update(set('%s %s' % (author['first_name'], author['last_name']) for author in paper_authors))
    authors_list = sorted(list(authors_list))
    return authors_list


def get_authors_ratings(authors_dict, authors_list):
    """
    Get number of author's papers
    """
    authors_rating = dict.fromkeys(authors_list, 0)
    for paper_authors in authors_dict:
        for author in paper_authors:
            author = '%s %s' % (author['first_name'], author['last_name'])
            authors_rating[author] += 1

    authors_rating = OrderedDict(sorted(authors_rating.items(), key=lambda t: t[1], reverse=True))
    return authors_rating


def get_adjacency_matrix(authors_dict, authors_list):
    """
    Get weighted adjacency matrix for authors from each paper
    """
    adjacency_list = dict()
    for author_key in authors_list:
        adjacency_list[author_key] = {}

    for paper_authors in authors_dict:
        for author in paper_authors:
            author = '%s %s' % (author['first_name'], author['last_name'])
            for co_author in paper_authors:
                co_author = '%s %s' % (co_author['first_name'], co_author['last_name'])
                if author != co_author:
                    if co_author in adjacency_list[author].keys():
                        adjacency_list[author][co_author] += 1
                    else:
                        adjacency_list[author][co_author] = 1
    return adjacency_list


def main():
    return None


if __name__ == '__main__':
    main()
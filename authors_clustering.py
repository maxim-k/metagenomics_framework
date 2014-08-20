__author__ = 'maximk'


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
            author_name = '%s %s' % (author['first_name'], author['last_name'])
            authors_rating[author_name] += 1
    return authors_rating


def main():
    return None

if __name__ == '__main__':
    main()
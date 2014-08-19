__author__ = 'maximk'



def get_authors_list(authors_dict):
    authors_list = set()
    for paper_authors in authors_dict:
        authors_list.update(set('%s %s' % (author['first_name'], author['last_name']) for author in paper_authors))
    authors_list = sorted(list(authors_list))
    return authors_list


def main():
    return None

if __name__ == '__main__':
    main()
__author__ = 'maximk'

from collections import OrderedDict

def get_keywords_list(authors_dict):
    keywords_list = []
    return keywords_list


def get_keywords_ratings(keywords_dict, keywords_list):
    keywords_rating = dict.fromkeys(keywords_list, 0)
    for paper_keywords in keywords_dict:
        for keyword in paper_keywords:
            keyword = '%s %s' % (keyword['first_name'], keyword['last_name'])
            keywords_rating[keyword] += 1

    keywords_rating = OrderedDict(sorted(keywords_rating.items(), key=lambda t: t[1], reverse=True))

    return keywords_rating


def main():
    return None

if __name__ == '__main__':
    main()
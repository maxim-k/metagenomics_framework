__author__ = 'maximk'

from collections import OrderedDict


def get_abstracts_list(abstracts_dict):
    """
    Get abstracts from Mendeley JSON; remove duplicates.
    """
    abstracts_list = set()
    for paper_abstract in abstracts_dict:
        abstracts_list.update({paper_abstract.lower()})
    abstracts_list = sorted(list(abstracts_list))
    return abstracts_list


def get_abstracts_conclusions(abstracts_list, conclusions_list):
    count_s = 0
    for conclusion in conclusions_list:
        count = 0
        for abstract in abstracts_list:
            if conclusion in abstract:
                count += 1
                count_s += 1
        print(conclusion, count)
    return count_s


def count_pairs(abstracts_list):
    abstracts_list = ' '.join(abstracts_list).replace('.', '').replace(',', '').lower().split()
    pairs = ['%s %s %s' % (abstracts_list[pos], abstracts_list[pos+1], abstracts_list[pos+2]) for pos in range(len(abstracts_list)-2)]
    pairs_set = set(pairs)
    pairs_dict = dict((pair, pairs.count(pair)) for pair in pairs_set)
    pairs_dict = OrderedDict(sorted(pairs_dict.items(), key=lambda t: t[1], reverse=True))
    return pairs_dict


def main():
    return None


if __name__ == '__main__':
    main()
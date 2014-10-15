__author__ = 'maximk'

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


def main():
    return None


if __name__ == '__main__':
    main()
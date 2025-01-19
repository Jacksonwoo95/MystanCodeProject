"""
File: babynames.py
Name: 吳禹
--------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import sys


def add_data_for_name(name_data, year, rank, name):
    """
    Adds the given year and rank to the associated name in the name_data dict.

    Input:
        name_data (dict): dict holding baby name data
        year (str): the year of the data entry to add
        rank (str): the rank of the data entry to add
        name (str): the name of the data entry to add

    Output:
        This function modifies the name_data dict to store the provided
        name, year, and rank. This function does not return any value.
    """
    if name not in name_data:
        # add new_name
        name_data[name] = {year: rank}
    else:
        # 名字已存在name_data{}裡
        # 檢查year是否在name_data[][year]裡
        if year in name_data[name]:
            old_rank = int(name_data[name][year])
            new_rank = int(rank)
            if new_rank < old_rank:
                name_data[name][year] = rank
        else:
            # year 不在 name_data[name]裡
            name_data[name][year] = rank


def add_file(name_data, filename):
    """
    Reads the information from the specified file and populates the name_data
    dict with the data found in the file.

    Input:
        name_data (dict): dict holding baby name data
        filename (str): name of the file holding baby name data

    Output:
        This function modifies the name_data dict to store information from
        the provided file name. This function does not return any value.
    """
    with open(filename, 'r') as f:
        year = ""
        for line in f:
            tokens = line.split(',')
            # test
            print('tokens test: ', tokens)
            if len(tokens) == 1:
                year = str(tokens[0].strip())
                # test
                print("year test :", year)
            elif len(tokens) == 3:
                rank = str(tokens[0].strip())
                name1 = str(tokens[1].strip())
                name2 = str(tokens[2].strip())
                # test
                print('rank:name1:name2 test: ', rank, name1, name2)

                add_data_for_name(name_data, year, rank, name1)
                add_data_for_name(name_data, year, rank, name2)


def read_files(filenames):
    """
    Reads the data from all files specified in the provided list
    into a single name_data dict and then returns that dict.

    Input:
        filenames (List[str]): a list of filenames containing baby name data

    Returns:
        name_data (dict): the dict storing all baby name data in a structured manner
    """
    name_data = {}
    for filename in filenames:
        add_file(name_data, filename)

    return name_data


def search_names(name_data, target):
    """
    Given a name_data dict that stores baby name information and a target string,
    returns a list of all names in the dict that contain the target string. This
    function should be case-insensitive with respect to the target string.

    Input:
        name_data (dict): a dict containing baby name data organized by name
        target (str): a string to look for in the names contained within name_data

    Returns:
        matching_names (List[str]): a list of all names from name_data that contain
                                    the target string
    """
    names = []
    target_low = str(target).lower()
    for name in name_data:
        name_low = str(name).lower()
        # 取name片段文字
        for i in range(len(name_low)-len(target_low)+1):
            s = name_low[i:i+len(target_low)]
            if s == target_low:
                names.append(name)

    return names


def print_names(name_data):
    """
    (provided, DO NOT MODIFY)
    Given a name_data dict, print out all its data, one name per line.
    The names are printed in alphabetical order,
    with the corresponding years data displayed in increasing order.

    Input:
        name_data (dict): a dict containing baby name data organized by name
    Returns:
        This function does not return anything
    """
    for key, value in sorted(name_data.items()):
        print(key, sorted(value.items()))


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    print('args test: ', args)
    # Two command line forms
    # 1. file1 file2 file3 ..
    # 2. -search target file1 file2 file3 ..

    # Assume no search, so list of filenames to read
    # is the args list
    filenames = args
    print('filenames test: ', filenames)

    # Check if we are doing search, set target variable
    target = ''
    if len(args) >= 2 and args[0] == '-search':
        target = args[1]
        filenames = args[2:]  # Update filenames to skip first 2
        print('target test: ', target)
        print('filenames in len(args) >= 2 and args[0] == -search test: ', filenames)

    # Read in all the filenames: baby-1990.txt, baby-2000.txt, ...
    names = read_files(filenames)  # names = {}

    # Either we do a search or just print everything.
    if len(target) > 0:
        search_results = search_names(names, target)
        for name in search_results:
            print(name)
    else:
        print_names(names)


if __name__ == '__main__':
    main()

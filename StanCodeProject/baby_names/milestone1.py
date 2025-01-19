"""
File: milestone1.py
Name: 
-----------------------
This file tests the milestone 1 for
our babyname.py project
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
        print(f'add new name{name, name_data[name]}')
    else:
        # 名字已存在name_data{}裡
        # 檢查year是否在name_data[][year]裡
        if year in name_data[name]:
            old_rank = int(name_data[name][year])
            new_rank = int(rank)
            if new_rank < old_rank:
                name_data[name][year] = rank
                # test
                # print(f'change rank {name, year, name_data[name][year]}: {old_rank} -> {new_rank}')
            # else:
                # test
                # print(f'No change rank, {name, name_data[name]} ')
        else:
            # year 不在 name_data[name]裡
            name_data[name][year] = rank
            # test
            # print(f'add new year{name, name_data[name]}')


# ------------- DO NOT EDIT THE CODE BELOW THIS LINE ---------------- #


def test1():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')
    print('--------------------test1----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test2():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2000', '104', 'Kylie')
    print('--------------------test2----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test3():
    name_data = {'Kylie': {'2010': '57'}, 'Sammy': {'1980': '451', '1990': '200'}, 'Kate': {'2000': '100'}}
    add_data_for_name(name_data, '1990', '900', 'Sammy')
    add_data_for_name(name_data, '2010', '400', 'Kylie')
    add_data_for_name(name_data, '2000', '20', 'Kate')
    print('-------------------test3-----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def test4():
    name_data = {'Kylie': {'2010': '57'}, 'Nick': {'2010': '37'}}
    add_data_for_name(name_data, '2010', '208', 'Kate')  # add new_name
    add_data_for_name(name_data, '2000', '108', 'Kate')  # add new_year
    add_data_for_name(name_data, '1990', '200', 'Sammy')  # add new_name
    add_data_for_name(name_data, '1990', '90', 'Sammy')  # change rank
    add_data_for_name(name_data, '2000', '104', 'Kylie')  # add new_year
    print('--------------------test4----------------------')
    print(str(name_data))
    print('-----------------------------------------------')


def main():
    args = sys.argv[1:]
    if len(args) == 1 and args[0] == 'test1':
        test1()
    elif len(args) == 1 and args[0] == 'test2':
        test2()
    elif len(args) == 1 and args[0] == 'test3':
        test3()
    elif len(args) == 1 and args[0] == 'test4':
        test4()


if __name__ == "__main__":
    main()

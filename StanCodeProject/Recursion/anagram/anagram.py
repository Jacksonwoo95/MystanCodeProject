"""
File: anagram.py
Name:
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    TODO:
    """
    d_lst = read_dictionary()
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        print('Searching...')
        start = time.time()
        ####################
        anagram_lst = find_anagrams(word)  # 取anagram list
        correct_anagram(anagram_lst, d_lst)
        ####################
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def read_dictionary():
    d_list = []  # dictionary in d_list

    # read file
    with open(FILE, 'r') as f:
        for line in f:
            token = line.strip()
            d_list.append(token)
    ####################
    # /test/
    # print(d_dict)
    ####################
    return d_list


def find_anagrams(s):
    """
    :param s:
    :return:
    """
    s_list = []
    current_lst = []  # anagram list
    # ans = ''
    for ch in s:
        s_list.append(ch)
    find_anagrams_helper(s_list, len(s_list), current_lst, "")

    ####################
    # /test/
    # print(f'{len(current_lst)} anagrams: {current_lst}')
    # print(s_list)
    ####################

    return current_lst


def find_anagrams_helper(s_list, s_len, current_lst, ans):
    if len(s_list) != 0:
        for i in range(len(s_list)):
            # choose
            ch = s_list[i]  # 取出字母
            ans += ch  # 加入字串
            s_list.pop(i)

            # explore
            find_anagrams_helper(s_list, s_len, current_lst, ans)

            # un-choose
            ans = ans[:-1]
            s_list.insert(i, ch)

    else:
        if ans not in current_lst:
            current_lst.append(ans)


def has_prefix(sub_s, d_lst):
    """
    :param sub_s: sub_string
    :param d_lst:
    :return:
    """
    for word in d_lst:
        if word.startswith(sub_s):
            return True

    return False  # 如果全部沒找到才 return False

    ####################
    # /test/
    # d_list = ['abc', 'good', 'book', 'dog', 'xyz']
    # for word in d_list:
    #     if word.startswith(sub_s):
    #         print("T")
    #         return True
    # print('F')
    # return False
    ####################


def correct_anagram(ana_lst, d_lst):
    """
    :param ana_lst: anagram list
    :param d_lst: dictionary list
    """
    c_ana_lst = []  # correct_anagram_lst : 有在 d_lst 裡 anagram 才存入
    for ans in ana_lst:
        if early_stop_search(ans, d_lst):
            c_ana_lst.append(ans)
            print(c_ana_lst[-1])  # 印出c_ana_lst最後一個
            print('Searching...')
    print(f'{len(c_ana_lst)} anagrams: {c_ana_lst}')


def early_stop_search(ans, d_lst):
    if ans in d_lst:
        return True
    return False


if __name__ == '__main__':
    main()


####################
# /test/
# if __name__ == '__main__':
#     find_anagrams('abc')
#     # has_prefix('app')
#     # has_prefix('do')
#     has_prefix('god')
#     has_prefix('goo')
#     d_list = read_dictionary()
#     print(len(d_list))
####################

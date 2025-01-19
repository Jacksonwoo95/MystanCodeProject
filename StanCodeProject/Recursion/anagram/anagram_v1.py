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
    # d_lst = read_dictionary()
    print('Welcome to stanCode ''Anagram Generator'' (or -1 to quit)')
    while True:
        word = input("Find anagrams for: ")
        if word == EXIT:
            break
        print('Searching...')
        start = time.time()
        ####################
        sub_d_list = sub_dictionary(word)
        anagram_lst = find_anagrams(word)  # 取anagram list
        correct_anagram(anagram_lst, sub_d_list)
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


def sub_dictionary(s):
    s_lst = []
    d_lst = read_dictionary()
    sub_d_lst = []
    i_index = -1

    for ch in s:
        if ch not in s_lst:
            s_lst.append(ch)

    for ch in s_lst:
        for i in range(len(d_lst)):
            if i_index == -1:  # 還沒找到目標
                if d_lst[i][0] == ch:
                    # i_index 為0，取第一筆i值
                    i_index = i
                    sub_d_lst.append(d_lst[i])
                    d_lst.pop(i)
            else:  # 找到第一筆以後
                if d_lst[i_index][0] == ch:
                    sub_d_lst.append(d_lst[i_index])
                    d_lst.pop(i_index)
                else:
                    i_index += 1

        # print(len(sub_d_lst))
        # 跑完一回圈後， i_index 重置
        i_index = -1

    return sub_d_lst

    ####################
    # /test/
    # print(len(d_lst))
    # print(len(sub_d_lst))
    ####################


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


def has_prefix(sub_s):
    """
    :param sub_s:
    :return:
    """
    d_list = read_dictionary()
    for word in d_list:
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
            print(c_ana_lst[-1])
            print('Searching...')
    print(f'{len(c_ana_lst)} anagrams: {c_ana_lst}')


def early_stop_search(ans, d_lst):
    if ans in d_lst:
        return True
    return False


def test_sub_dictionary():
    s = ['abc', 'bca', 'bac', 'aab', 'bab', 'aca']
    i_index = -1
    for i in range(len(s)):
        if i_index == -1:  # 還沒找到目標
            if s[i][0] == 'a':
                # i_index 為0，取第一筆i值
                i_index = i
                s.pop(i)
        else:  # 找到第一筆以後
            if s[i_index][0] == 'a':
                s.pop(i_index)
            else:
                i_index += 1
    print(s)


if __name__ == '__main__':
    main()


####################
# /test/
# if __name__ == '__main__':
# #     find_anagrams('abc')
#
# #     # has_prefix('app')
#
# #     # has_prefix('do')
# #     has_prefix('god')
# #     has_prefix('goo')
# #     sub_dictionary('aabbcc', [])
# #     test_sub_dictionary()
#     d_llst = read_dictionary()
#     sub_dictionary('contains')
####################

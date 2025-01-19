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
    can_count = False
    i_start = 0
    i_end = 0

    for ch in s:
        if ch not in s_lst:
            s_lst.append(ch)
    s_lst.sort()

    for ch in s_lst:
        for i in range(i_end, len(d_lst)):
            # 只取 字母開頭有包含在s裡 長度＝s
            if not can_count:
                if d_lst[i][0] == ch and len(d_lst[i]) == len(s):
                    # i_index 為0，取第一筆i值
                    i_start = i
                    can_count = True
            else:
                if d_lst[i][0] != ch or len(d_lst[i]) != len(s):
                    i_end = i
                    sub_d_lst += d_lst[i_start:i_end]
                    can_count = False

    return sub_d_lst

    ####################
    # /test/
    # print(s_lst)
    # print(len(d_lst))
    # print(sub_d_lst)
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
    current_lst.sort()

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
    search_index = 0
    for ans in ana_lst:
        for i in range(search_index, len(d_lst)):
            if ans == d_lst[i]:
                search_index = i
                c_ana_lst.append(ans)
                print(c_ana_lst[-1])
                print('Searching...')
    print(f'{len(c_ana_lst)} anagrams: {c_ana_lst}')


# if __name__ == '__main__':
#     main()


####################
# /test/
if __name__ == '__main__':
#     ana = find_anagrams('contains')
#     print(ana)
#     print(len(ana))
#
    d_lst = read_dictionary()
    print(len(d_lst))

    sub_d_lst = sub_dictionary('contains')
    print(sub_d_lst)
    print(len(sub_d_lst))

####################

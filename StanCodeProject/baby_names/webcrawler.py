"""
File: webcrawler.py
Name: 吳禹
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10905209
Female Number: 7949058
---------------------------
2000s
Male Number: 12979118
Female Number: 9210073
---------------------------
1990s
Male Number: 14146775
Female Number: 10644698
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names'+year+'.html'

        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")

        # ----- Write your code below this line ----- #
        # init male and female total
        male_total = 0
        female_total = 0

        table = soup.find("table", {"class": "t-stripe"})
        # print(table)
        raw_trs = table.find_all('tr')[1:]
        # print(raw_trs)
        for raw_tr in raw_trs:
            data_cols = raw_tr.find_all('td')
            if len(data_cols) == 5:
                data_info = []
                for data_col in data_cols:
                    text = data_col.text
                    # print(text)
                    data_info.append(text)
                # print(data_info)

                # calculate
                male_num = str_to_int(data_info[2])  # do str_manipulation
                male_total += int(male_num)
                # print(male_num)
                female_num = str_to_int(data_info[4])
                female_total += int(female_num)
        print(f'Male Numbers: {male_total}')
        print(f'Female Numbers: {female_total}')


def str_to_int(s):
    ans = ''
    for ch in s:
        if ch.isdigit():
            ans += ch
    return ans


if __name__ == '__main__':
    main()

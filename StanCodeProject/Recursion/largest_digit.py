"""
File: largest_digit.py
Name:吳禹
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: only int
	:return: biggest one
	"""
	if n < 0:
		n = -n
	if n < 10:
		return n
	else:
		n_end = n % 10
		if (n // 10) % 10 > n_end:
			return find_largest_digit((n // 10))
		else:
			return find_largest_digit(n // 100 * 10 + n_end)


if __name__ == '__main__':
	main()

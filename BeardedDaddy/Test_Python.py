def get_even(numbers):
	even_nums = [num for num in numbers if not num % 2]
	return even_nums


get_even([1, 2, 3, 4, 5, 6])
def get_answer(key, dict):
	return dict[key.lower()]


if __name__ == '__main__':
	my_dict = {"name":"me", "voice":"laud"}
	print(get_answer("voice", my_dict))


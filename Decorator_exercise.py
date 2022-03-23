last_arg = None

# the decorator
def last_call(function):
	"""Last call is A decorator that will check if arg matches the last one"""
	# the inner of the decorator
	def wrapped(*args):
		global last_arg
		if last_arg != args[0]:
			ret_val = function(*args)
		else:
			ret_val = f'I already told you the answer is {func(*args)}'
		last_arg = args[0]
		return ret_val
	return wrapped


@last_call
def func(x):
	return x * 2

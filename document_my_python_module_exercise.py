from importlib import import_module
from inspect import getmembers, isfunction


def document_my_python_file(module_name):
	"""
	:param module_name: python module
	:return: creates an html with documentation of the module
	"""
	try:
		# importing the module with import_module from importlib
		mymodule = import_module(module_name)
		# getting the list of tuples with functions_name, function_instance
		list_of_func = getmembers(mymodule, isfunction)

		for func in list_of_func:
			# Name of the function with its documentation.
			#  doc from the __doc__ of the function instance
			doc_func = f'{func[0]}:\n\t {func[1].__doc__}\n'
			# opening/creating if needed, html file with doc_func
			html_file = open(f'{module_name}_doc.html', 'a')
			#  adding the str doc_func to our file
			html_file.write(doc_func)

		html_file.close()
	# simple catch for ModuleNotFoundError exception
	except ModuleNotFoundError:
		print(f'{module_name} Does not Exist')


document_my_python_file('Decorator_exercise')

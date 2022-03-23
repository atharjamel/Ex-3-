class List:

	def __init__(self, list1):
		self.list1 = list1

	def __getitem__(self, *items):
		sub_list = self.list1.copy()

		for i in items:
			if type(i) == int:
				return sub_list[i]

			for j in i:
				sub_list = sub_list[j]

		return sub_list

mylist = List(
	[
		[
			[1, 3, 5], [8, 5, 6], [7, 1, 6]
		],
		[
			[1, 43, 15], [238, 51, 46], [437, 11, 26]
		]
	]
)

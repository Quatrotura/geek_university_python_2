from sys import argv

def show_sales(argv):
	"""This function return sales amounts"""
	trash, *sales_idx = argv

	with open('bakery.csv', 'r', encoding = 'utf-8') as f:		
		if len(argv) == 1:			
			for line in f:
				print(line.rstrip())		
			exit(0)

		for i in range(int(sales_idx[0])-1):
			f.readline()

		if len(sales_idx) == 1:
			for line in f:
				print(line.rstrip())		
		elif len(sales_idx) == 2:
			lines_req = int(sales_idx[1]) - int(sales_idx[0]) + 1
			for i in range(lines_req):
				print(f.readline().rstrip())
		else:
			print("You've entered something wrong! Try again.")
			exit(1)
			
show_sales(argv)
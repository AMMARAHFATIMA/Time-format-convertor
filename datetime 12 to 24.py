from datetime import datetime

def convert24(time):
	# %I is for 12hrs clock %p is fo PM or AM
	t = datetime.strptime(time, '%I:%M:%S %p')
	return t.strftime('%H:%M:%S')

print(convert24('08:12:47 PM')) 

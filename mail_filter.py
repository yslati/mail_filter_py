file = input("enter mailist: ")
try:
	mail_file = open(file, "r")
except FileNotFoundError as err:
	print(err)
	quit()
if not mail_file.readable():
	print("wrong mail file")
else:
	domain = input("enter domain name: ")
	result_file = open(domain+".txt", "w")
	result_file.writelines("-------------------- " +domain+ " --------------------\n\n")
	for line in mail_file.readlines():
		if domain in line:
			result_file.writelines(line)
			result_file.writelines(">>>>>>>>>>>>>>>>>>>> Dolfine <<<<<<<<<<<<<<<<<<<<\n")
		else:
			continue
mail_file.close()
result_file.close()

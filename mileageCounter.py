#The purpose of this program is to record daily mileage for Amazon Flex,
#and enter the information into a text file for tax filing.
import sys
from math import ceil

def get_mileage_info():

	global date
	global mileageStart
	global mileageEnd
	global averageMPG

	print("Enter today's date (mm/dd/yyyy): ")
	date = input()

	print("Enter mileage at the beginning of your shift: ")
	mileageStart = input()

	print("Enter mileage at the end of your shift: ")
	mileageEnd = input()

	print("Enter average MPG at the end of your shift: ")
	averageMPG = input()

	need_gas()

def need_gas():
	global amountOfGas
	global costOfGas

	print("Did you need to stop for gas? (y/n)")
	stoppedForGas = input().lower()
	if (stoppedForGas == 'y'):
		print("Enter the amount of gas pumped (gallons): ")
		amountOfGas = input()
		print("Enter the cost of gas pumped (dollars): ")
		costOfGas = input()
		print_mileage_info()
	elif(stoppedForGas == 'n'):
		amountOfGas = 0
		costOfGas = 0
		print_mileage_info()
	else:
		print("Invalid selection. Try again.")
		need_gas()

def print_mileage_info():
	global mileageToday
	global approxGallonsUsed
	global amountOfGas
	global gallonsRounded

	print("")
	print("Mileage Start: " +str(mileageStart))
	print("Mileage End: " +str(mileageEnd))
	print("Average MPG: " +str(averageMPG))

	mileageToday = int(mileageEnd) - int(mileageStart)
	print("Mileage Today: " + str(mileageToday))

	approxGallonsUsed = int(mileageToday) / int(averageMPG)
	gallonsRounded = ceil(approxGallonsUsed*100) / 100
	print("Approximate gallons of gas used: " + str(gallonsRounded))

	print("Amount of gas pumped: " +str(amountOfGas)+ " gallon(s)")
	print("Cost of gas pumped: " +str(costOfGas)+ " dollar(s)")
	append_mileage_sheet()

def append_mileage_sheet():
	print("")
	print("Is all this information correct? (y/n)")
	isCorrect = input()
	if (isCorrect == 'y' or 'Y'):
		mileageFile = open('FlexMileageSheet.txt','a')
		mileageFile.write("Mileage report for " +str(date)+ ":\n\n")
		mileageFile.write("Mileage Start: " +mileageStart+ "\n")
		mileageFile.write("Mileage End: " +mileageEnd+ "\n")
		mileageFile.write("Average MPG: " +averageMPG+ "\n")
		mileageFile.write("Mileage Today: " +str(mileageToday)+ "\n")
		mileageFile.write("Approximate gallons of gas used: " +str(gallonsRounded)+ "\n")
		mileageFile.write("Amount of gas pumped: " +str(amountOfGas)+ " gallons\n")
		mileageFile.write("Cost of gas pumped: " +str(costOfGas)+ " dollar(s)\n")
		mileageFile.write('---------------END---------------\n')
		mileageFile.close()
		print("Information successfully recorded!")
		quit()
	if (isCorrect == 'n' or 'N'):
		get_mileage_info()
	else:
		print("Invalid selection. Try again.")
		append_mileage_sheet()

get_mileage_info()

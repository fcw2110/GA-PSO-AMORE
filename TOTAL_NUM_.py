
# Import information about species and reaction types
# from the Python file 'data.py'

from _UTILITIES import BREAK_DOWN_RXN
help(BREAK_DOWN_RXN)
import numpy as np
import shutil

# Import necessary libraries

import os

def TOTAL_NUM_PRODS(OLD_FILE_NAME):

	"""
	This function reads the file named OLD_FILE_NAME, and
	extracts the number of product(s) per reaction in the mechanism
	"""

	# Copy file
	
	shutil.copyfile(OLD_FILE_NAME + '.txt', OLD_FILE_NAME + '_copy.txt')

	# Read the data in the previous reaction mechanism file

	with open(OLD_FILE_NAME + '_copy.txt') as f:
	    data = f.readlines()

	# Split the data before, and after the hypothesized mechanism

	dataBeforeMyHypothesizedMechanism = data[:6] # lines 1 to 6
	HypothesizedMechanism = data[6:156] # lines 7 to 156
	dataAfterMyHypothesizedMechanism = data[156:] # lines 157 to the end

	# Group the hypothesized mechanism on the basis of the spaces between each 5-line reaction

	from itertools import groupby
	MechanismList = list(list(g) for _, g in groupby(HypothesizedMechanism, key='\n'.__ne__))
	
	# Remove the 1 and 2 linespaces in the original reaction mechanism file

	# Returns each 5-line reaction as a separate individual of the list 'Mechanism'

	Mechanism = []
	for ele in MechanismList:
		if ''.join(ele).isspace() == True:
			pass
		else:
			Mechanism.append(ele)

	# Obtain the number of reactions in the mechanism

	NUM_RXNS = len(Mechanism)

	# Obtain the number of products in the total mechanism

	TOTAL_NUM_PRODS = []
	# ALL_PRDCTS_ = []

	for NUM_RXN in range(NUM_RXNS):

		PREV_RXN = Mechanism[NUM_RXN]

		_, _, _, PRDCTS, _ = BREAK_DOWN_RXN(PREV_RXN)

		TOTAL_NUM_PRODS.append(len(PRDCTS))

		# ALL_PRDCTS_.append(PRDCTS)

	# ALL_PRDCTS = [item for sublist in ALL_PRDCTS_ for item in sublist]

	# replace .txt file to .m file

	os.replace(OLD_FILE_NAME + '_copy.txt', OLD_FILE_NAME + '.txt')
	
	return TOTAL_NUM_PRODS


def TOTAL_NUM_RXTS(OLD_FILE_NAME):

	"""
	This function reads the file named OLD_FILE_NAME, and
	extracts the number of reactant(s) per reaction in the mechanism
	"""

	# Copy file
	
	shutil.copyfile(OLD_FILE_NAME + '.txt', OLD_FILE_NAME + '_copy.txt')

	# Read the data in the previous reaction mechanism file

	with open(OLD_FILE_NAME + '_copy.txt') as f:
	    data = f.readlines()

	# Split the data before, and after the hypothesized mechanism

	dataBeforeMyHypothesizedMechanism = data[:6] # lines 1 to 6
	HypothesizedMechanism = data[6:156] # lines 7 to 156
	dataAfterMyHypothesizedMechanism = data[156:] # lines 157 to the end

	# Group the hypothesized mechanism on the basis of the spaces between each 5-line reaction

	from itertools import groupby
	MechanismList = list(list(g) for _, g in groupby(HypothesizedMechanism, key='\n'.__ne__))
	
	# Remove the 1 and 2 linespaces in the original reaction mechanism file

	unwanted_spaces = [['\n'], ['\n', '\n']]

	# Returns each 5-line reaction as a separate individual of the list 'Mechanism'

	Mechanism = [ele for ele in MechanismList if ele not in unwanted_spaces]

	# Obtain the number of reactions in the mechanism

	NUM_RXNS = len(Mechanism)

	# Obtain the number of reactants in the total mechanism

	TOTAL_NUM_RXTS = []

	for NUM_RXN in range(NUM_RXNS):

		PREV_RXN = Mechanism[NUM_RXN]

		_, RXTS, _, _, _ = BREAK_DOWN_RXN(PREV_RXN)

		TOTAL_NUM_RXTS.append(len(RXTS))

	# replace .txt file to .m file

	os.replace(OLD_FILE_NAME + '_copy.txt', OLD_FILE_NAME + '.m')

	return TOTAL_NUM_RXTS


def ALL_PRODS_LIST(OLD_FILE_NAME):

	"""
	This function reads the file named OLD_FILE_NAME, and
	extracts the number of product(s) per reaction in the mechanism
	"""

	# Copy file
	
	shutil.copyfile(OLD_FILE_NAME + '.txt', OLD_FILE_NAME + '_copy.txt')

	# Read the data in the previous reaction mechanism file

	with open(OLD_FILE_NAME + '_copy.txt') as f:
	    data = f.readlines()

	# Split the data before, and after the hypothesized mechanism

	dataBeforeMyHypothesizedMechanism = data[:6] # lines 1 to 6
	HypothesizedMechanism = data[6:156] # lines 7 to 156
	dataAfterMyHypothesizedMechanism = data[156:] # lines 157 to the end

	# Group the hypothesized mechanism on the basis of the spaces between each 5-line reaction

	from itertools import groupby
	MechanismList = list(list(g) for _, g in groupby(HypothesizedMechanism, key='\n'.__ne__))
	
	# Remove the 1 and 2 linespaces in the original reaction mechanism file

	unwanted_spaces = [['\n'], ['\n', '\n']]

	# Returns each 5-line reaction as a separate individual of the list 'Mechanism'

	Mechanism = [ele for ele in MechanismList if ele not in unwanted_spaces]

	# Obtain the number of reactions in the mechanism

	NUM_RXNS = len(Mechanism)

	# Obtain the number of products in the total mechanism

	TOTAL_NUM_PRODS = []
	ALL_PRDCTS_ = []

	for NUM_RXN in range(NUM_RXNS):

		PREV_RXN = Mechanism[NUM_RXN]

		_, RXTS, RXN_TYPE, PRDCTS, _ = BREAK_DOWN_RXN(PREV_RXN)

		TOTAL_NUM_PRODS.append(len(PRDCTS))

		ALL_PRDCTS_.append(PRDCTS)

	ALL_PRDCTS = [item for sublist in ALL_PRDCTS_ for item in sublist]

	# replace .txt file to .m file

	os.replace(OLD_FILE_NAME + '_copy.txt', OLD_FILE_NAME + '.txt')

	# Now find out the indexes where the most important species occur:
	# 	1. NO2
	#	2. NO
	# 	3. HO2
	# 	4. HO

	indices_of_important_products = [index + 1 for index in range(sum(
			TOTAL_NUM_PRODS)) if ALL_PRDCTS[index] in ['NO2', 'HO2']]

	return indices_of_important_products


# TOTALED_NUM_RXTS = TOTAL_NUM_RXTS(OLD_FILE_NAME)

TOTALED_NUM_PRODS = TOTAL_NUM_PRODS(OLD_FILE_NAME)

# ALL_PRODS = ALL_PRODS_LIST(OLD_FILE_NAME)










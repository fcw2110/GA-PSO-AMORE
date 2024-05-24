
# Import information about species and reaction types
# from the Python file 'data.py'

from _DATA import SPECIES, RXN_TYPES
from _UTILITIES import GEN_NEW_RXN, BREAK_DOWN_RXN, BREAK_DOWN_RXN_FOR_RATE, TOTAL_NUM_PRODS, WRITE_RXN_wRATEPARAM, TOTAL_NUM_PRODS

# Import necessary libraries

import os, shutil
import numpy as np
import random as rd
import pyuac

def RATE_PARAMETERS(ALL_PARAMS_, OLD_FILE_NAME):

	# Copy file
	
	shutil.copyfile(OLD_FILE_NAME + '.m', OLD_FILE_NAME + '_copy.m')

	# Read the data in the previous reaction mechanism file

	with open(OLD_FILE_NAME + '_copy.m') as f:
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

	_, TOTAL_NUM_PRODS_, _, _, _, _ = TOTAL_NUM_PRODS(OLD_FILE_NAME)

	#########

	cumsum_of_TOTAL_NUM_PRODS = np.cumsum(TOTAL_NUM_PRODS_)
	
	stoichparms = ALL_PARAMS_[:cumsum_of_TOTAL_NUM_PRODS[-1]]
	rateparms = ALL_PARAMS_[cumsum_of_TOTAL_NUM_PRODS[-1]:]

	

	STOICH_PARAMS = np.split(ary=stoichparms,
						indices_or_sections=cumsum_of_TOTAL_NUM_PRODS)[:-1]
	for NUM_RXN in range(NUM_RXNS):
		PREV_RXN = Mechanism[NUM_RXN]
		_, RXTS, RXN_TYPE, RXN_RATE, PRDCTS, _ = BREAK_DOWN_RXN_FOR_RATE(PREV_RXN)
		NEW_RXN_wSTOICHIOMETRY = WRITE_RXN_wRATEPARAM(RXTS=RXTS, RXN_TYPE=RXN_TYPE, RXN_RATE=RXN_RATE,
				PRDCTS=PRDCTS, RATE_PARAM=rateparms[NUM_RXN], PRDCT_STOICHS=STOICH_PARAMS[NUM_RXN])

		Mechanism[NUM_RXN] = NEW_RXN_wSTOICHIOMETRY

	# Prepare the list of lines for writing to the new renamed file
	OurNewMechanism = []
	counter = 0
	for i in MechanismList:

		#if i == ['\n', '\n'] or i == ['\n']: # Uncomment this when doing any GA-AMORE mechanism
		if ''.join(i).isspace() == True: # Comment this when doing any AMORE (e.g., v1/v2 mechanism)
			OurNewMechanism.append(i)
		else:
			OurNewMechanism.append(Mechanism[counter])
			counter += 1

	OurNewMechanism = [x for xs in OurNewMechanism for x in xs]

	# Write to .txt file

	with open(OLD_FILE_NAME + '_copy.m', 'w') as f:

		for line in dataBeforeMyHypothesizedMechanism:
			f.write(line)
		for line in OurNewMechanism:
			f.write(line)
		for line in dataAfterMyHypothesizedMechanism:
			f.write(line)

	# Rename .txt file to .m file

	# os.rename(OLD_FILE_NAME + '.txt', NEW_FILE_NAME + '.m')
	
	os.replace(OLD_FILE_NAME + '_copy.m', OLD_FILE_NAME + '.m')

	pass


# RATE_PARAMETERIZED = RATE_PARAMETERS(OLD_FILE_NAME, NEW_FILE_NAME, ALL_RATE_PARAMS_)

# RATE_PARAMETERIZED = RATE_PARAMETERS(np.ones(97 + 22), 'AMORE_10_1')

def main():
    RATE_PARAMETERIZED = RATE_PARAMETERS(ALL_PARAMS_, OLD_FILE_NAME)
    # The window will disappear as soon as the program exits!
    input("Press enter to close the window. >")

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()  # Already an admin here.










# Import information about species and reaction types
# from the Python file 'data.py'

from _DATA import REACTANTS, SPECIES, RXN_TYPES

# Import necessary libraries

import os, re
import random as rd
import collections
import itertools

def GEN_NEW_RXTS(NUM_RXTS):

	"""
	This function generates a list of new reactants, given:
		1. NUM_RXTS – the number of reactants

	Returns: 	list of new reactants, reaction type, and
				set of atoms of the reactants.

	"""

	# Initialize the list of reactants, and the reaction type
	
	RXTS = []
	RXN_TYPE = None

	# Case 1: If we have ONLY 1 reactant

	if NUM_RXTS == 1:
		RANDOM_DRAW_1 = rd.randint(1, 2) # Can take either 1 or 2
		if RANDOM_DRAW_1 == 1:
			RXN_TYPE = 'plain'
			
			# # Create the list of acceptable options for reactant 1 by
			# # removing the 'ISOP', as no reaction would be possible
			# # with 'ISOP' as the only reactant
			# available_organics_for_rxt1 = list(ORGANICS.values())
			# available_organics_for_rxt1.remove('ISOP')
			
			available_organics_for_rxt1 = ['ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']

			# Choose from the list of organic species
			RXTS.append(rd.choice(available_organics_for_rxt1))
		else:
			RXN_TYPE = 'photo'
			
			available_organics_for_rxt1 = ['ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']

			# Choose from the list of organic species
			RXTS.append(rd.choice(available_organics_for_rxt1))

	# Case 2: If we have EXACTLY 2 reactants

	else:
		NUM_RXTS == 2
		RANDOM_DRAW_2 = rd.randint(3, 10)

		if RANDOM_DRAW_2 == 3:
			RXN_TYPE = 'OH'
			RXTS.append('OH')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		elif RANDOM_DRAW_2 == 4:
			RXN_TYPE = 'NO'
			RXTS.append('NO')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		elif RANDOM_DRAW_2 == 5:
			RXN_TYPE = 'NO2'
			RXTS.append('NO2')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		elif RANDOM_DRAW_2 == 6:
			RXN_TYPE = 'NO3'
			RXTS.append('NO3')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		elif RANDOM_DRAW_2 == 7:
			RXN_TYPE = 'HO2'
			RXTS.append('HO2')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		elif RANDOM_DRAW_2 == 8:
			RXN_TYPE = 'O3'
			RXTS.append('O3')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		#elif RANDOM_DRAW_2 == 9:
		#	RXN_TYPE = 'O2'
		#	RXTS.append('O2')
		
		elif RANDOM_DRAW_2 == 9:
			RXN_TYPE = 'CH3OO'
			RXTS.append('CH3OO')
			
			# for second reactant
			available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN']
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)
			
		else:
			RXN_TYPE = 'double'

			# Since first reactant is always organic
			RXT1 = rd.choice(['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2',
					'IPN', 'IPC', 'IHN'])
			RXTS.append(RXT1)

			# Create the list of acceptable options for reactant 2 by
			# removing the first reactant, in order to avoid repetition
			available_organics_for_rxt2 = ['CH3CO3', 'CH3OO']
			#available_organics_for_rxt2.remove(RXT1)

			# Choose reactant 2 from the list of acceptable options
			RXT2 = rd.choice(available_organics_for_rxt2)
			RXTS.append(RXT2)

	# print(RXTS)

	#if RXN_TYPE in ['double', 'plain', 'photo']:
	#	pass
	#else:
		# Since second reactant is always organic

	#	available_organics_for_rxt2 = ['ISOP', 'ISOPOO', 'ISOPOOH', 'INO2', 'IPN', 'IPC', 'IHN', 'CH3OO', 'CH3CO3']

		# Check if RXT1 is in the available_organics_for_rxt2
		# It is possible for RXT1 to not be in available_organics_for_rxt2
		# because RXT1 is not necessarily organic always. It could be inorganic

	#	if RXTS[0] in available_organics_for_rxt2:
	#		available_organics_for_rxt2.remove(RXTS[0])
	#	else:
	#		pass

	#	RXT2 = rd.choice(available_organics_for_rxt2)
	#	RXTS.append(RXT2)

	# Calculate the set of atoms of the reactant(s)

	temp_RXT_atoms = []
	for RXT in RXTS:
		temp_RXT_atoms.append(REACTANTS[RXT][0]) # set of atoms for each reactant

	RXT_ATOMS = set([x for xs in temp_RXT_atoms for x in xs])

	return RXTS, RXN_TYPE, RXT_ATOMS


def GEN_NEW_PRDCTS(RXTS, RXT_ATOMS, MAX_NUM_PRDCTS):

	"""
	This function generates a list of products, on the basis of
	the list of reactants provided, 
	WITH NO REGARD TO THE ATOM SET OF THE REACTANTS
	Given:
		1. RXTS – list of reactant(s)
		2. RXT_ATOMS – set of atoms of the reactant(s)
		3. MAX_NUM_PRDCTS – the maximum number of products that
							can be generated in a new reaction

	Returns: list of product(s), set of atoms of the product(s)
	"""

	# Create pool of all species

	all_species = list(SPECIES.keys())

	# Remove the reactant(s) from the pool of all species
	# in order to create the list of options for products

	for RXT in RXTS:
		if RXT in all_species:
			all_species.remove(RXT)
		else:
			pass

	# Remove the species which have atoms which
	# are not a subset of the reactant(s)

	permitted_species = all_species
	for speci in all_species:
		set_of_speci_atoms = set(SPECIES[speci][0])
		if set_of_speci_atoms.issubset(RXT_ATOMS):
			pass
		else:
			permitted_species.remove(speci)

	PRDCTS = []
	NUM_PRDCTS = rd.choice(range(1, MAX_NUM_PRDCTS))

	# Check for the case when the number of permitted
	# species is more than the number of products

	if len(permitted_species) >= NUM_PRDCTS:

		# Iterate for as many number of products desired
		for NUM_PRDCT in range(NUM_PRDCTS):

			# Choose a product from the list of permitted species
			choice_of_prdct = rd.choice(permitted_species)

			# Add to the list of products
			PRDCTS.append(choice_of_prdct)

			# Remove the product chosen to avoid repetition
			permitted_species.remove(choice_of_prdct)
	else:

		# Iterate for as many number of permitted species
		for NUM_PERMITTED_SPECI in permitted_species:

			# Choose a product from the list of permitted species
			choice_of_prdct = rd.choice(permitted_species)

			# Add to the list of products
			PRDCTS.append(choice_of_prdct)

			# Remove the product chosen to avoid repetition
			permitted_species.remove(choice_of_prdct)

	# Calculate the set of atoms of the product(s)

	temp_PRDCT_atoms = []
	for PRDCT in PRDCTS:
		temp_PRDCT_atoms.append(SPECIES[PRDCT][0]) # set of atoms for each product

	PRDCT_ATOMS = set([x for xs in temp_PRDCT_atoms for x in xs])

	return PRDCTS, PRDCT_ATOMS


def WRITE_RXN(RXTS, RXN_TYPE, PRDCTS):

	# Create reaction string from the final reactants and products

	RXN = ''

	for RXT in RXTS:
		RXN += RXT + ' + '
	RXN = RXN[:-3] + ' = '

	for PRDCT in PRDCTS:
		RXN += PRDCT + ' + '
	RXN = RXN[:-3]

	## Let us now create the 5-line reaction

	# –––> Line 1
	DEFAULT = 'i=i+1;\n'

	# –––> Line 2
	RXN_STRING = "Rnames{i} = " + '\'' + RXN + '\'' + ';\n'

	# –––> Line 3
	RXN_RATE = 'k(:,i) = ' + RXN_TYPES[RXN_TYPE] + ';\n'

	# –––> Line 4
	RXT_SPECIFICATIONS = ''
	for RXT, NUM_RXT in zip(RXTS, range(1, len(RXTS) + 1)):
		RXT_SPECIFICATIONS = RXT_SPECIFICATIONS + 'Gstr{i,' + str(
							NUM_RXT) + '}' + ' = ' + '\'' + RXT + '\'; '

	# –––> Line 5
	RXN_STOICHIOMETRY = '\n'
	for RXT in RXTS:
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + RXT + '(i)=' + 'f' + RXT + '(i)-1.0; '
	for PRDCT in PRDCTS:
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + PRDCT + '(i)=' + 'f' + PRDCT + '(i)+1.0;'

	return [DEFAULT, RXN_STRING, RXN_RATE, RXT_SPECIFICATIONS, RXN_STOICHIOMETRY + '\n']


def GEN_NEW_RXN(NUM_RXTS, MAX_NUM_PRDCTS):

	"""
	This function generates a new reaction, given:
		1. NUM_RXTS – the number of reactants
		2. MAX_NUM_PRDCTS – the maximum number of products that
							can be generated in a new reaction

	Returns: a new 5-line reaction.

	"""

	# We assert that the number of reactants is either 1 or 2
	# More reactants are not permitted at this time

	assert (NUM_RXTS == 1) or (NUM_RXTS == 2), 'Only 1 or 2 reactants allowed'

	# We assert that the number of products
	# is within the user-specified range

	assert MAX_NUM_PRDCTS > 0 , 'Invalid number of maximum products'

	# Obtain random reactant(s) from the 'GEN_NEW_RXTS' function

	RXTS, RXN_TYPE, RXT_ATOMS = GEN_NEW_RXTS(NUM_RXTS=NUM_RXTS)

	# Obtain new product(s) from the 'GEN_NEW_PRDCTS' function

	PRDCTS, PRDCT_ATOMS = GEN_NEW_PRDCTS(RXTS=RXTS, RXT_ATOMS=RXT_ATOMS,
							MAX_NUM_PRDCTS=MAX_NUM_PRDCTS)

	# If the set of atoms of product(s) is not the same as atoms of reactant(s)
	# Generate new products repeatedly till the two sets are the same

	while PRDCT_ATOMS != RXT_ATOMS:

		PRDCTS, PRDCT_ATOMS = GEN_NEW_PRDCTS(RXTS=RXTS, RXT_ATOMS=RXT_ATOMS,
							MAX_NUM_PRDCTS=MAX_NUM_PRDCTS)

		if PRDCT_ATOMS == RXT_ATOMS:
			break

	NEW_RXN = WRITE_RXN(RXTS=RXTS, RXN_TYPE=RXN_TYPE, PRDCTS=PRDCTS)

	return NEW_RXN


def BREAK_DOWN_RXN(FIVE_LINE_RXN):

	"""
	This function breaks down the 5-line reaction into:
		DEFAULT – the first line of every 5-line reaction
		RXTS – Reactant(s)
		RXN_TYPE – Reaction type
		PRDCTS – Product(s)
		PRDCT_STOICHS – Product stoichiometry (if applicable)
	"""

	## 1. Let us obtain the default

	DEFAULT = FIVE_LINE_RXN[0]
	
	

	## 2. & 4. Let us obtain the reactant(s) & product(s)

	temp_RXN = FIVE_LINE_RXN[1].lstrip()
	temp_RXN = temp_RXN[13:-3]
	
	

	# Split into reactant(s) & product(s) based on '='

	temp_rxts, temp_prdcts = temp_RXN.split('=')

	# Remove the spaces – from ' ' to ''
	temp_rxts = ''.join(temp_rxts).replace(' ', '')

	# Split reactant(s) & product(s) based on '+'
	temp_rxts = temp_rxts.split('+')

	# Obtain the cleaned reactant(s)
	RXTS = []
	for temp_rxt in temp_rxts:
		RXTS.append(temp_rxt.lstrip('0123456789.-* '))
		
	# print(RXTS)

	#3. Obtain reaction rate

	RXN_TYPE = None
	
	if len(temp_rxts) == 1:
		RXN_TYPE = rd.choice(['photo', 'plain'])
	elif len(temp_rxts) == 2 and 'O3' in temp_rxts:
		RXN_TYPE = 'O3'
	elif len(temp_rxts) == 2 and 'O2' in temp_rxts:
		RXN_TYPE = 'O2'
	elif len(temp_rxts) == 2 and 'HO2' in temp_rxts:
		RXN_TYPE = 'HO2'
	elif len(temp_rxts) == 2 and 'NO3' in temp_rxts:
		RXN_TYPE = 'NO3'
	elif len(temp_rxts) == 2 and 'NO2' in temp_rxts:
		RXN_TYPE = 'NO2'
	elif len(temp_rxts) == 2 and 'NO' in temp_rxts:
		RXN_TYPE = 'NO'
	elif len(temp_rxts) == 2 and 'CH3OO' in temp_rxts:
		RXN_TYPE = 'CH3OO'
	elif len(temp_rxts) == 2 and 'HO' in temp_rxts:
		RXN_TYPE = 'OH'
	else:
		RXN_TYPE = 'double'

	RXN_RATE = FIVE_LINE_RXN[2]

	## 4. Obtain product(s)

	# Remove the spaces – from ' ' to ''
	temp_prdcts = ''.join(temp_prdcts).replace(' ', '')

	# Split product(s) based on '+'
	temp_prdcts = temp_prdcts.split('+')
	
	# Obtain the cleaned product(s)
	PRDCTS = []
	for temp_prdct in temp_prdcts:
		PRDCTS.append(temp_prdct.lstrip('0123456789.-* '))

	## 5. Product stoichiometry

	PRDCT_STOICHS = []

	# print(temp_prdcts)

	# # Looping over every product
	# for temp_prdct in temp_prdcts:

	# 	temp_stoichiometric_coeff = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", temp_prdct)

	# 	if len(temp_stoichiometric_coeff) == 0:
	# 		temp_stoichiometric_coeff = 1
	# 	else:
	# 		try:
	# 			temp_stoichiometric_coeff = temp_stoichiometric_coeff[0]
	# 		except:
	# 			temp_stoichiometric_coeff = 1
		
	# 	_stoichiometric_coeff = temp_stoichiometric_coeff

	# 	# print(_stoichiometric_coeff)

	# 	PRDCT_STOICHS.append(float(_stoichiometric_coeff))

	return [DEFAULT, RXTS, RXN_RATE, PRDCTS, PRDCT_STOICHS]


def BREAK_DOWN_RXN_FOR_RATE(FIVE_LINE_RXN):

	"""
	This function breaks down the 5-line reaction into:
		DEFAULT – the first line of every 5-line reaction
		RXTS – Reactant(s)
		RXN_TYPE – Reaction type
		PRDCTS – Product(s)
		PRDCT_STOICHS – Product stoichiometry (if applicable)
	"""

	## 1. Let us obtain the default

	DEFAULT = FIVE_LINE_RXN[0]
	
	#print(DEFAULT)

	## 2. & 4. Let us obtain the reactant(s) & product(s)

	temp_RXN = FIVE_LINE_RXN[1].lstrip()
	temp_RXN = temp_RXN[13:-3]
	


	# Split into reactant(s) & product(s) based on '='
	temp_rxts, temp_prdcts = temp_RXN.split('=')
	
	#print(temp_rxts, temp_prdcts)

	# Remove the spaces – from ' ' to ''
	temp_rxts = ''.join(temp_rxts).replace(' ', '')

	# Split reactant(s) & product(s) based on '+'
	temp_rxts = temp_rxts.split('+')

	# Obtain the cleaned reactant(s)
	RXTS = []
	for temp_rxt in temp_rxts:
		RXTS.append(temp_rxt.lstrip('0123456789.-* '))
		
	#print(RXTS)

	#3. Obtain reaction rate

	RXN_TYPE = None
	#if len(temp_rxts) == 1 and temp_rxts[0] != 'ISOP':
	#if len(temp_rxts) == 1:
	#	RXN_TYPE = rd.choice(['photo', 'plain'])
	#elif len(temp_rxts) == 2 and len(list(set(temp_rxts).intersection(set())))==1:
	#	RXN_TYPE_CHOICES = list(set(temp_rxts).intersection(set()))[0]
	#else:
	#	RXN_TYPE = 'double'
	#RXN_TYPE = RXN_TYPES_INV[FIVE_LINE_RXN[2][9:-2]]
	
	if len(temp_rxts) == 1:
		RXN_TYPE = rd.choice(['photo', 'plain'])
	elif len(temp_rxts) == 2 and 'O3' in temp_rxts:
		RXN_TYPE = 'O3'
	elif len(temp_rxts) == 2 and 'O2' in temp_rxts:
		RXN_TYPE = 'O2'
	elif len(temp_rxts) == 2 and 'HO2' in temp_rxts:
		RXN_TYPE = 'HO2'
	elif len(temp_rxts) == 2 and 'NO3' in temp_rxts:
		RXN_TYPE = 'NO3'
	elif len(temp_rxts) == 2 and 'NO2' in temp_rxts:
		RXN_TYPE = 'NO2'
	elif len(temp_rxts) == 2 and 'NO' in temp_rxts:
		RXN_TYPE = 'NO'
	elif len(temp_rxts) == 2 and 'CH3OO' in temp_rxts:
		RXN_TYPE = 'CH3OO'
	elif len(temp_rxts) == 2 and 'OH' in temp_rxts:
		RXN_TYPE = 'OH'
	else:
		RXN_TYPE = 'double'

	RXN_RATE = FIVE_LINE_RXN[2].partition(';')[0]

	## 4. Obtain product(s)

	# Remove the spaces – from ' ' to ''
	temp_prdcts = ''.join(temp_prdcts).replace(' ', '')

	# Split product(s) based on '+'
	temp_prdcts = temp_prdcts.split('+')
	
	# Obtain the cleaned product(s)
	PRDCTS = []
	for temp_prdct in temp_prdcts:
		PRDCTS.append(temp_prdct.lstrip('0123456789.-* '))

	## 5. Product stoichiometry

	PRDCT_STOICHS = []

	# Looping over every product
	for temp_prdct in temp_prdcts:

		temp_stoichiometric_coeff = re.findall(r"[-+]?(?:\d*\.\d+|\d+)", temp_prdct)
		
		_stoichiometric_coeff = temp_prdct.rpartition('*')[0]
		#print(temp_prdct, float(_stoichiometric_coeff))

		#if len(temp_stoichiometric_coeff) == 0:
		#	temp_stoichiometric_coeff = 1
		#else:
		#	temp_stoichiometric_coeff = temp_stoichiometric_coeff[0]
		
		#temp_stoichiometric_coeff = _stoichiometric_coeff

		PRDCT_STOICHS.append(float(_stoichiometric_coeff))
	
	return [DEFAULT, RXTS, RXN_TYPE, RXN_RATE, PRDCTS, PRDCT_STOICHS]


def WRITE_RXN_wSTOICH(RXTS, _RXN_RATE, PRDCTS, PRDCT_STOICHS):

	# Ensure that the product stoichiometric coefficients are valid

	assert len(list(PRDCT_STOICHS)) == len(PRDCTS), 'Stoichiometric coefficients are invalid'

	# Create reaction string from the final reactants and products

	RXN = ''

	for RXT in RXTS:
		RXN += RXT + ' + '
	RXN = RXN[:-3] + ' = '

	for PRDCT, PRDCT_STOICH in zip(PRDCTS, PRDCT_STOICHS):
		RXN += str(PRDCT_STOICH) + '*' + PRDCT + ' + '
	RXN = RXN[:-3]

	## Let us now create the 5-line reaction

	# –––> Line 1
	DEFAULT = 'i=i+1;\n'

	# –––> Line 2
	RXN_STRING = "Rnames{i} = " + '\'' + RXN + '\'' + ';\n'

	# –––> Line 3
	RXN_RATE = _RXN_RATE
	#'k(:,i) = ' + RXN_TYPES[RXN_TYPE] + ';\n'

	# –––> Line 4
	RXT_SPECIFICATIONS = ''
	for RXT, NUM_RXT in zip(RXTS, range(1, len(RXTS) + 1)):
		RXT_SPECIFICATIONS = RXT_SPECIFICATIONS + 'Gstr{i,' + str(
							NUM_RXT) + '}' + ' = ' + '\'' + RXT + '\'; '

	# –––> Line 5
	RXN_STOICHIOMETRY = '\n'
	for RXT in RXTS:
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + RXT +'(i)=' + 'f' + RXT + '(i)-1.0; '
	for PRDCT, PRDCT_STOICH in zip(PRDCTS, PRDCT_STOICHS):
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + PRDCT +'(i)=' + 'f' + PRDCT + '(i)+' + str(PRDCT_STOICH) + '; '

	return [DEFAULT, RXN_STRING, RXN_RATE, RXT_SPECIFICATIONS, RXN_STOICHIOMETRY + '\n']


def TOTAL_NUM_PRODS(OLD_FILE_NAME):

	"""
	This function reads the file named OLD_FILE_NAME, and
	extracts the number of products per reaction in the mechanism
	"""

	# Read the data in the previous reaction mechanism file

	with open(OLD_FILE_NAME + '.m') as f:
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

	TOTAL_NUM_RXTS = []
	TOTAL_NUM_PRODS = []
	ALL_RXTS_ = []
	ALL_PRDCTS_ = []

	for NUM_RXN in range(NUM_RXNS):

		PREV_RXN = Mechanism[NUM_RXN]

		_, RXTS, RXN_TYPE, PRDCTS, _ = BREAK_DOWN_RXN(PREV_RXN)

		ALL_RXTS_.append(RXTS)
		ALL_PRDCTS_.append(PRDCTS)

		TOTAL_NUM_RXTS.append(len(RXTS))
		TOTAL_NUM_PRODS.append(len(PRDCTS))

	ALL_PRDCTS = [item for sublist in ALL_PRDCTS_ for item in sublist]

	indices_of_important_products = [index for index in range(sum(
			TOTAL_NUM_PRODS)) if ALL_PRDCTS[index] in ['NO2', 'HO2']]

	return TOTAL_NUM_RXTS, TOTAL_NUM_PRODS, ALL_RXTS_, ALL_PRDCTS_, ALL_PRDCTS, indices_of_important_products


def WRITE_RXN_wRATEPARAM(RXTS, RXN_TYPE, RXN_RATE, PRDCTS, RATE_PARAM, PRDCT_STOICHS):

	# Ensure that the product stoichiometric coefficients are valid

	assert len(list(PRDCT_STOICHS)) == len(PRDCTS), 'Stoichiometric coefficients are invalid'
	
	# Create reaction string from the final reactants and products

	RXN = ''

	for RXT in RXTS:
		RXN += RXT + ' + '
	RXN = RXN[:-3] + ' = '

	for PRDCT, PRDCT_STOICH in zip(PRDCTS, PRDCT_STOICHS):
		RXN += str(PRDCT_STOICH) + '*' + PRDCT + ' + '
	RXN = RXN[:-3]
	
	## Let us now create the 5-line reaction

	# –––> Line 1
	DEFAULT = 'i=i+1;\n'

	# –––> Line 2
	RXN_STRING = "Rnames{i} = " + '\'' + RXN + '\'' + ';\n'
	
	# RXN_RATE = ''
	# # –––> Line 3
	# if RXN_TYPE == 'photo':
	# 	RXN_RATE = 'k(:,i) = ' + 'SUN.*' + str(RATE_PARAM) + '.*1E-7;\n'
	# elif RXN_TYPE == 'plain':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + '.*1E-5;\n'
	# elif RXN_TYPE == 'OH':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + '.*1E-11;\n'
	# elif RXN_TYPE == 'NO':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-12.*exp(-290./T)' + ';\n'
	# elif RXN_TYPE == 'NO2':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + '.*1E-12;\n'
	# elif RXN_TYPE == 'NO3':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-12;\n'
	# 	# RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-12.*exp(-450./T)' + ';\n'
	# elif RXN_TYPE == 'HO2':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-13.*exp(1300./T)' + ';\n'
	# elif RXN_TYPE == 'O2':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-13;\n'
	# elif RXN_TYPE == 'CH3OO':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-12;\n'
	# elif RXN_TYPE == 'O3':
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-14;\n'
	# 	# RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-14.*exp(-2000./T)' + ';\n'
	# else:
	# 	RXN_RATE = 'k(:,i) = ' + str(RATE_PARAM) + 'E-13;\n'

	_RXN_RATE_ = RXN_RATE + '.*' + str(RATE_PARAM) + ';'

	# –––> Line 4
	RXT_SPECIFICATIONS = ''
	for RXT, NUM_RXT in zip(RXTS, range(1, len(RXTS) + 1)):
		RXT_SPECIFICATIONS = RXT_SPECIFICATIONS + 'Gstr{i,' + str(
							NUM_RXT) + '}' + ' = ' + '\'' + RXT + '\'; '					
							
	# –––> Line 5
	RXN_STOICHIOMETRY = '\n'
	for RXT in RXTS:
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + RXT + '(i)=' + 'f' + RXT + '(i)-1.0; '
	for PRDCT, PRDCT_STOICH in zip(PRDCTS, PRDCT_STOICHS):
		RXN_STOICHIOMETRY = RXN_STOICHIOMETRY + 'f' + PRDCT + '(i)=' + 'f' + PRDCT + '(i)+' + str(PRDCT_STOICH) + ';'

	return [DEFAULT, RXN_STRING, _RXN_RATE_, RXT_SPECIFICATIONS, RXN_STOICHIOMETRY + '\n']
	

def EXTRACT_PRDCTS_RXTS(_FILE_NAME_):

	# Read the data in the previous reaction mechanism file

	with open(_FILE_NAME_ + '.txt') as f:
	    data = f.readlines()

	# Split the data before, and after the hypothesized mechanism

	dataBeforeMyHypothesizedMechanism = data[:6] # lines 1 to 6
	HypothesizedMechanism = data[6:156] # lines 7 to 156
	dataAfterMyHypothesizedMechanism = data[156:] # lines 157 to the end

	# dataBeforeMyHypothesizedMechanism = data[:6] # lines 1 to 6
	# HypothesizedMechanism = data[6:129] # lines 7 to 129
	# dataAfterMyHypothesizedMechanism = data[129:] # lines 130 to the end

	# Group the hypothesized mechanism on the basis of the spaces between each 5-line reaction

	from itertools import groupby
	MechanismList = list(list(g) for _, g in groupby(HypothesizedMechanism, key='\n'.__ne__))
	
	# Remove the 1 and 2 linespaces in the original reaction mechanism file

	unwanted_spaces = [['\n'], ['\n', '\n']]

	# Returns each 5-line reaction as a separate individual of the list 'Mechanism'

	Mechanism = [ele for ele in MechanismList if ele not in unwanted_spaces]

	ALL_RXTS = []
	ALL_PRDCTS = []

	for rxn in Mechanism:

		_, RXTS, _, PRDCTS, _ = BREAK_DOWN_RXN(rxn)

		ALL_RXTS.append(RXTS)
		ALL_PRDCTS.append(PRDCTS)

	return ALL_RXTS, ALL_PRDCTS


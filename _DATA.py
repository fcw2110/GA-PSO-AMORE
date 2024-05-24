
REACTANTS = {
	'ISOP': [['C', 'H', 'O'], 'ORGANIC'],
	'ISOPOO': [['C', 'H', 'O'], 'ORGANIC'],
	'ISOPOOH': [['C', 'H', 'O'], 'ORGANIC'],
	'INO2': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'IPN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'IHN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'IPC': [['C', 'H', 'O'], 'ORGANIC'],
	'CH3OO': [['C', 'H', 'O'], 'ORGANIC'],
	'CH3CO3': [['C', 'H', 'O'], 'ORGANIC'],
	'NO2': [['N', 'O'], 'INORGANIC'],
	'HO2': [['H', 'O'], 'INORGANIC'],
	'OH': [['H', 'O'], 'INORGANIC'],
	'NO': [['N', 'O'], 'INORGANIC'],
	'NO3': [['N', 'O'], 'INORGANIC'],
	'O3': [['O'], 'INORGANIC']
	}

SPECIES = {
	'OH': [['H', 'O'], 'INORGANIC'],
	'NO': [['N', 'O'], 'INORGANIC'],
	'NO2': [['N', 'O'], 'INORGANIC'],
	'NO3': [['N', 'O'], 'INORGANIC'],
	'O3': [['O'], 'INORGANIC'],
	'HO2': [['H', 'O'], 'INORGANIC'],
	'CH3OO': [['C', 'H', 'O'], 'ORGANIC'],
	#'ACO3': [['C', 'H', 'O'], 'ORGANIC'],
	'IEPOX': [['C', 'H', 'O'], 'ORGANIC'],
	'HCHO': [['C', 'H', 'O'], 'ORGANIC'],
	'GLYX': [['C', 'H', 'O'], 'ORGANIC'], # alternately GLY
	#'MGLY': [['C', 'H', 'O'], 'ORGANIC'],
	'MACR': [['C', 'H', 'O'], 'ORGANIC'],
	'ISOPN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'IPN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'ISOPOO': [['C', 'H', 'O'], 'ORGANIC'],
	'IHN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	'ISOPOOH': [['C', 'H', 'O'], 'ORGANIC'],
	'MVK': [['C', 'H', 'O'], 'ORGANIC'],
	'MACP': [['C', 'H', 'O'], 'ORGANIC'],
	'INO2': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	#'MOH': [['C', 'H', 'O'], 'ORGANIC'],
	#'ROH': [['C', 'H', 'O'], 'ORGANIC'],
	#'ALD': [['C', 'H', 'O'], 'ORGANIC'],
	'HNO3': [['H', 'N', 'O'], 'INORGANIC'],
	'IPC': [['C', 'H', 'O'], 'ORGANIC'],
	#'RCO3': [['C', 'H', 'O'], 'ORGANIC'],
	#'ETHP': [['C', 'H', 'O'], 'ORGANIC'],
	#'UALD': [['C', 'H', 'O'], 'ORGANIC'],
	#'KET': [['C', 'H', 'O'], 'ORGANIC'],
	#'UALP': [['C', 'H', 'O'], 'ORGANIC'],
	#'ACD': [['C', 'H', 'O'], 'ORGANIC'],
	# 'MVKP': [['C', 'H', 'O'], 'ORGANIC'],
	'ROCN2OXY8': [['C', 'H', 'O'], 'ORGANIC'],
	#'OP2': [['C', 'H', 'O'], 'ORGANIC'],
	#'OLT': [['C', 'H'], 'ORGANIC'],
	#'ELHOM': [['C', 'H', 'O'], 'ORGANIC'],
	#'HKET': [['C', 'H', 'O'], 'ORGANIC'],
	#'HOM': [['C', 'H', 'O'], 'ORGANIC'],
	#'ORA1': [['C', 'H', 'O'], 'ORGANIC'],
	#'ORA2': [['C', 'H', 'O'], 'ORGANIC'],
	'MPAN': [['C', 'H', 'O', 'N'], 'ORGANIC']
	}
	# 'O2': [['O'], 'INORGANIC']
	
	# 'HONO': [['H', 'N', 'O'], 'INORGANIC'],
	# 'PAN': [['C', 'H', 'O', 'N'], 'ORGANIC'],
	# 'CO2': [['C', 'O'], 'INORGANIC'],
	# 'H2O2': [['H', 'O'], 'INORGANIC'],
	# 'CO': [['C', 'O'], 'INORGANIC'],
	# 'H2O': [['H', 'O'], 'INORGANIC'],
	

RXN_TYPES = {
	'OH': '1.0E-10',
	'NO': '5E-12*exp(-290./T)',
	'NO2': '9.0E-12',
	'NO3': '6.3E-13', # 6.3E-13*exp(-450./T)
	'HO2': '2.64E-13*exp(1300./T)',
	'O3': '1.7E-17', # 1.7E-17*exp(-2000./T)
	'plain': '1.0E-05',
	'photo': 'SUN*1E-5',
	'O2': '1.0E-13',
	'CH3OO': '1.0E-12',
	'double': '2.0E-12'
}



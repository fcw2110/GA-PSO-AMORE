# GA-PSO-AMORE
Files:
- AMORE_10_1.txt: a f0am formatted txt file of the mechanism being optimized. All reactions to be optimized should be in the beginning, separated by at least 250 lines.
  
- AMORE_10_1_copy.m: a matlab script with the same contents as AMORE_10_1.txt
  
- Fitness_species_input_6_3_24: This script measured the mechanism fitness (closer to 0 is better) as defined in the paper. It requires inputs of the species to be measured in the reference and test mechanisms, along with the relative weighting of that species to the overall error, and whether or not consumption should be account for. Consumption is accounted for in species where the loss of that species needs to be tracked, such as OH loss by reaction with isoprene. Consumption can be ignored for species where loss is not important to the specific mechanism, for example formaldehyde loss is not relevant to the isoprene mechanism. Note that the reference mechanism and test mechanism can compare species with different names, or even groups of species to individual species. For example, in the AMORE mechanism, IEPOX is one lumped species, and in the full mechanism it is 3 species. The reference species list has ["ISOP1OH23O4OHt"; "ISOP1OH23O4OHc"; "ISOP1OH2OH34O"] in the same position that the test list has "IEPOX". In this case, the same of those three IEPOX species in the reference mechanism will be compared to the lumped IEPOX species in the test mechanism.

- GA_AMORE_RateParamOpt.m: This is the main PSO script which should be run to optimize the mechanism. The opts variable sets the optimization settings. 'SwarmSize' and 'MaxIterations' sets the number of particles in the swarm and the number of iterations that the optimization will run. 'Initial Points' can be used to add a seed particle, which must be the correct size.
The variable TOTAL_NUM_PRODS is the number of stiochiometric coefficients being changes and is calculated automatically. The number of rate constants must be added in manually and match the number of optimizable reactions in the mechanism.
The variable x is the result of the particle swarm optimization. The 3rd and 4th inputs to the particle swarm function are the upper and lower bounds for each parameter. Stoichoimetric coefficients take on the value of the parameter in the optimization, whereas rate constants are multiplied by the value in the optimization. In the example below, stoichiometric coefficients can range from 0 to 2 and rate constants can be 0.01 to 100 times their starting value. To hold the rate constants at the starting value, the range can be set from 1 to 1. 
  x = particleswarm(@(x)ErrorEval(x,S0), TOTAL_NUM_PRODS + 14, ...
    [ones(1, TOTAL_NUM_PRODS) * 0.0, ones(1, 14) * 0.01], ...
    [ones(1, TOTAL_NUM_PRODS) * 2, ones(1, 14) * 100], opts)
The output of this script will be the variable x, which contains the final optimized parameters. It should be saved and input into the script create_parametrized_mechanism_10_27, which will update the file AMORE_10_1_copy.m to contain the new optimized parameters.

- create_parametrized_mechanism_10_27.m: input the x variable into this script to update the AMORE_10_1_copy.m mechanism witht the new parameters. A duplicate can be saved for the optimized mechanism.

- multi_param_run_6_7_24.m: In this file, the mechanism error is measured for each condition in the samples file. The species from each mechanism should be listed along with the species weighting and whether or not consumption is taken into account.

- ref_mech_data_collect_6_7_24.m: In this file, the reference mechanism data is collected to be saved, since the reference mechanism data does not change with each iteration. The full mechanism file used here must match the one used in multi_param_run_6_7_24

- samples8.csv: This file contains the data for the concentrations of background gases and atmospheric parameters used. There are six conditions which were used in this work, but any number of conditions can be used, though more conditions will increase run time significantly.

- RATE_PARAMETER_OPT_3.py: This python script updates the AMORE_10_1.m file to reflect the current parameter set being measured.

- TOTAL_NUM.py: This python script calculates the number of tunable stoichiometric coefficients in a mechanism.

- _DATA.py: This file contains functions used in the above scripts.

- UTILITIES.py: This file contains functions used in the above script. 

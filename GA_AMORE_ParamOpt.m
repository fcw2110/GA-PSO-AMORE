
%% Step 1.
% Estimate the number of parameters to be optimized

% TOTALED_NUM_RXTS = pyrunfile("TOTAL_NUM_.py", ...
%     "TOTALED_NUM_RXTS", OLD_FILE_NAME="AMORE_10_1");
TOTALED_NUM_PRODS = pyrunfile("TOTAL_NUM_.py", ...
    "TOTALED_NUM_PRODS", OLD_FILE_NAME="AMORE_10_1");
% ALL_PRODS_LIST_IDXs = double(pyrunfile("TOTAL_NUM_.py", ...
%     "ALL_PRODS", OLD_FILE_NAME="AMORE_10_1"));

global TOTAL_NUM_PRODS

% TOTAL_NUM_RXTS = sum(double(TOTALED_NUM_RXTS));
% CUMSUM_NUM_RXTS = cumsum(double(TOTALED_NUM_RXTS));

TOTAL_NUM_PRODS = sum(double(TOTALED_NUM_PRODS));
CUMSUM_NUM_PRODS = cumsum(double(TOTALED_NUM_PRODS));

%% Step 2.
% Create function

opts = optimoptions('particleswarm','Display', ...
    'iter', 'SwarmSize', 50, 'MaxIterations', 100)%, 'MaxTime', 45000);
%x = particleswarm(@ErrorEval, length(ALL_PRODS_LIST_IDXs), ...
 %   ones(length(ALL_PRODS_LIST_IDXs), 1) * 0.01, ...
  %  ones(length(ALL_PRODS_LIST_IDXs), 1) * 2, opts)

global S0
% S0 = ref_mech_data_collect();
S0 = ref_mech_data_collect_10_18_23();

%mins = [0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.555; 0.045; 0.01; 0.01; 0.01; 0.01; 1; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 1; 0.01; 0.13; 0.01; 0.01; 0.01; 0.01; 0.01; 1; 0.01; 0.01; 0.01; 0.01; 0.01; 0.05; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.01; 0.13; 0.01; 0.01]

%maxs = [2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 0.555; 0.045; 2; 2; 2; 2; 1; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 1; 2; 0.13; 2; 2; 2; 2; 2; 1; 2; 2; 2; 2; 2; 0.05; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 2; 0.13; 2; 2]


%x = particleswarm(@(x)ErrorEval(x,S0), TOTAL_NUM_PRODS, ...
 %   mins, ...
  %  maxs, opts)
TOTAL_NUM_PRODS
x = particleswarm(@(x)ErrorEval(x,S0), TOTAL_NUM_PRODS, ...
    ones(TOTAL_NUM_PRODS, 1) * 0.01, ...
    ones(TOTAL_NUM_PRODS, 1) * 2., opts)

%% Step 3.
% Evaluate error

function [Error] = ErrorEval(x, S0)

    copyfile 'AMORE_10_1.txt' 'AMORE_10_1_copy.m';

    stoichparams_fixed = x;

    PARAMETERIZED = pyrunfile("PARAMETER_OPT.py", ...
    "PARAMETERIZED", ALL_STOICH_PARAMS_=stoichparams_fixed, OLD_FILE_NAME='AMORE_10_1_copy');

%     Error = multiparam_run_7_6_23("AMORE_10_1_copy", S0);
    Error = multiparam_run_8_24_23("AMORE_10_1_copy", S0);
    %disp(Error)
    delete('AMORE_10_1_copy.m');


end




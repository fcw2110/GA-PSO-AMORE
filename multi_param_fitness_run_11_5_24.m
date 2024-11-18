function [fitness] = multiparam_run_6_7_24(filename__, S0)
    S = [];
    samples = csvread('geo_dat_short.csv');
    Lm = 6;
    runs = filename__;
    Lr = length(runs);
    isopnit_noihn = ["ISOP1CO2N3OOH4OH"; "ISOP1CO2OOH3N4OH"; "ISOP1OH2OOH3N4CO"; "ISOP1OH2N3OOH4CO"; "ISOP1OH2N3CO4OH"; "ISOP1CO2N3OOH4OOH"; "ISOP1CO2OOH3N4OOH"; "ISOP1CO2OOH3OOH4N"; "ISOP1OOH2OOH3N4CO"; "ISOP1OOH2N3OOH4CO"; "ISOP1N2OOH3OOH4CO"; "ISOP1OOH23O3OH4N"; "ISOP1N2OOH34O4OH"; "ISOP1OH12O3OOH4N"; "ISOP1OH2OOH3OH4N"; "ISOP1OH2N3OH4OOH"; "ISOP1N2OH3OOH4OH"; "ISOP1OOH2OH3N4OH"; "ISOP1OH2OOH3N4OH"; "ISOP1OH2N3OOH4OH"; "ISOP1N2OOH3OH4CO"; "ISOP1CO2OH3OOH4N"; "ISOP1OOH2OH3CO4N"; "ISOP1N4R4OH"; "ISOP1OH1R4N"; "ISOP3OH3R4N"; "ISOP1OOH2R3CO4N"; "ISOP1OH2OH3N4CO"; "ISOP1CO2N3OH4OH"; "ISOP1OH2N3R4OH"; "ISOP1OH2N3OH4N"; "ISOP1OH2N3N4OH"; "ISOP1CO2N3OH4OOH"; "ISOP1OH2R3N4OH"; "ISOP1N2OH3N4OH"; "ISOP1OOH2OH3N4CO"; "ISOP1N2OOH"; "ISOP1N4OOH"; "ISOP3OOH4N"; "ISOP1OOH4N"; "ISOP3CO4N"; "ISOP1CO4N"; "ISOP1O4N"; "ISOP1N4CO"; "ISOP1N4O"; "ISOP1N2N"; "ISOP1N4N"; "ISOP3N4N"; "ISOP1N253O4OH"; "ISOP1N253N4OH"; "ISOP1N253OOH4OH"; "ISOP1N253CO4OH"; "ISOP1N253OH4OH"; "ISOP1N2OOH3R4OH"; "ISOP1N23O4OH"; "ISOP1N2OH3R4OOH"; "ISOP1N2OH34O"; "ISOP1N2R3OH4OOH"; "ISOP1OH2R3OOH4N"; "ISOP1OH23O4N"; "ISOP1OOH2R3OH4N"; "ISOP12O3OH4N"; "ISOP1OOH2OH3R4N"; "ISOP1N2OOH3N4OH"; "ISOP1N2OOH3OOH4OH"; "ISOP1N2OOH3OH4N"; "ISOP1N2OOH3OH4OOH"; "ISOP1N2OH3N4OOH"; "ISOP1N2OH3OOH4OOH"; "ISOP1N2N3OH4OOH"; "ISOP1OH2N3OOH4N"; "ISOP1OH2OOH3OOH4N"; "ISOP1N2OH3OOH4N"; "ISOP1OOH2OH3OOH4N"; "ISOP1OOH2N3OH4N"; "ISOP1OOH2OOH3OH4N"; "ISOP1OO2OOH3OH4N"; "ISOP1N2N3OOH4OH"; "ISOP1OH2OOH3N4N"; "ISOP1N23O4OH4R"; "ISOP1N23O4CO"; "ISOP1OH1R23O4N"; "ISOP1CO23O4N"; "ISOP1N2OH3CO4OOH"; "ISOP12O3OH3R4N"; "ISOP12O3CO4N"; "ISOP1N2OH3CO4N"; "ISOP1OH2OOH3CO4N"; "ISOP1N4R4CO"; "ISOP1N4CO4OOH"; "ISOP1N4CO4OH"; "ISOP1CO1R4N"; "ISOP1CO1OOH4N"; "ISOP1CO1OH4N"; "ISOP1N2R3OH4CO"; "ISOP1CO2OH3R4N"; "ISOP1N2OH3OOH4CO"; "ISOP1CO2OOH3OH4N"; "ISOP1N2R3OH4OH"; "ISOP1OH2OH3R4N"; "ISOP1N2OOH3OH4OH"; "ISOP1OH2OH3OOH4N"; "ISOP1N2OH3OH4OOH"; "ISOP1OOH2OH3OH4N"; "ISOP1OOH2OH3N4N"; "ISOP1OH2N3CO4N"; "ISOP1N2N3CO4OH"; "ISOP1OH2OH3N4N"; "ISOP1N2OH3OH4N"; "ISOP1N2N3OH4OH"; "ISOP1CO2N3OH4N"; "ISOP1N2OH3N4CO"; "ISOP1N4PAN"; "ISOP1PAN4N"; "ISOP1PAN4OH"; "ISOP1OH4PAN"];
    IEP  = 'ISOP1OH23O4OHt + ISOP1OH23O4OHc + ISOP1OH2OH34O';
    iep1 = ["ISOP1OH23O4OHt"; "ISOP1OH23O4OHc"; "ISOP1OH2OH34O"];
    species1 = {"OH"; "HO2"; "NO";"NO2";"NO3";"O3";"HCHO";"ISOP";["ISOP1OH23O4OHt"; "ISOP1OH23O4OHc"; "ISOP1OH2OH34O"];"MGLY";"GLYX";"CH3CO3";"CH3OO";"MACR"; "MVK"; isopnit_noihn};
    %species2 = {"OH"; "HO2"; "NO";"NO2";"NO3";"O3";"HCHO";"ISOP";["ISOP1OH23O4OHt"; "ISOP1OH23O4OHc"; "ISOP1OH2OH34O"];"MGLY";"GLYX";"CH3CO3";"CH3OO";"MACR"; "MVK"; isopnit_noihn};
    species2 = {"OH"; "HO2"; "NO";"NO2";"NO3";"O3";"HCHO";"ISOP";"IEPOX";"MGLY";"GLYX";"CH3CO3";"CH3OO";"MACR"; "MVK"; "ISOPN"};
    weights = [1;        1;   1;   1;    0;    1;    1;    0.5;    1;      0.5;   0.5;  0.8;    0.8;     0.5; 0.5; 0.8];
   

    %weights = [1;        1;   1;   1;    0;    1;    1;    0.5;    1;      0.5;   0.5;  0.8;    0.8;     0.5; 0.5; 0.8]/11.4;
    consumption = [1;   1;    1;    1;    1;   1;    0;     0;      0;     0;    0;      1;       1;     0;     0;       0];


    f = [];
    
    ChemFiles = {...
        'F0AM_isop_K_update(Met)';
        'F0AM_isop_J(Met,1)';
        runs;
        };
    for jj = 1:Lm
            %j = samples_to_read(jj)
            Met = {...
            %  		names       values          
            'P'         samples(jj,10)        ; %Pressure, mbar
    		'T'        samples(jj,9)               ; %Temperature, K
    		'RH'        0                ; %Relative Humidity, percent
    		'LFlux'     'ExampleLightFlux.txt'     ; %Text file for radiation spectrum
            'SUN'       samples(jj,8)             ;
    		'jcorr'     samples(jj,8)              ; %light attenuation factor
    		};
        InitConc = {...
%   		names       conc(ppb)           HoldMe
        	'O2'        210000000             1;
        	'ISOP'      samples(jj,1)         0;
        	'NO3'       samples(jj,7)         1;
    		'OH'        samples(jj,2)         1; %10^6 molecules per CCH0         0;
            'O3'        samples(jj,6)         1;
            'NO'        samples(jj,4)         1;
        	'HO2'       samples(jj,3)         1;
            'NO2'       samples(jj,5)         1;
            %'NO2'       0                     1;
        	};
        BkgdConc = {...
%   names           values
        'DEFAULT'       0;   %0 for all zeros, 1 to use InitConc
        };
        ModelOptions.Verbose       = 0;
        ModelOptions.EndPointsOnly = 0;
        ModelOptions.LinkSteps     = 0;
        ModelOptions.IntTime       = 200*3600;
        ModelOptions.SavePath      = 'ChamberExampleOutput.mat';
        ModelOptions.GoParallel    = 0;
        x = F0AM_ModelCore(Met,InitConc,ChemFiles,BkgdConc,ModelOptions);
        S = [S x];
    end
    fk = [];
    for j = 1:Lm
       fk = [fk Fitness_species_input_6_3_24(S0(j),S(j), species1, species2, weights, consumption)];
    end
    f = mean([f; fk]);
    fitness = f;




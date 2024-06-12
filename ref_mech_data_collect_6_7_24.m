function S0 = ref_mech_data_collect_6_7_24()
S0 = [];
samples = csvread('samples8.csv');
Lm = 6;
runs = ["caltech_ref_no_background_6_7_23"]; % this is the reference mechanism

Lr = length(runs);



for k = 1:Lr
    ChemFiles = {...
        'F0AM_isop_K_update(Met)';
        'F0AM_isop_J(Met,1)';
        runs(k);
        };
    for jj = 1:Lm
            %j = samples_to_read(jj)
            Met = {...
%  		names       values          
    		'P'         1000          ; %Pressure, mbar
    		'T'         292                ; %Temperature, K
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
            'NO'        samples(jj,5)         1;
        	'HO2'       samples(jj,3)         1;
            'CH3CO3'    samples(jj,9)         1;
            'CH3OO'     samples(jj,9)         1;
        	};
        BkgdConc = {...
%   names           values
        'DEFAULT'       0;   %0 for all zeros, 1 to use InitConc
        };

      
        ModelOptions.Verbose       = 3;
        ModelOptions.EndPointsOnly = 0;
        ModelOptions.LinkSteps     = 0;
        ModelOptions.IntTime       = 72*3600;
        ModelOptions.SavePath      = 'ChamberExampleOutput.mat';
        ModelOptions.GoParallel    = 0;
        x = F0AM_ModelCore(Met,InitConc,ChemFiles,BkgdConc,ModelOptions);
        S0 = [S0 x];
       
    end

end




function [E]=ErrorCalc8_lumped(reference,test,species1,species2)
step = 0.0000001;
max1 = max(reference.Time);
max2 = max(test.Time);
x = linspace(0+step,min(max1,max2)-step);
L1 = length(species1);
L2 = length(species2);
y_ref = [];
y_test = [];
for j=1:length(x)
    conc1 = 0;
    conc2 = 0;
    for i=1:L1
        conc1 = conc1 + Conc_Time(x(j),reference,species1{i});
    end
    for p=1:L2
        conc2 = conc2 + Conc_Time(x(j),test,species2{p});
    end
    y_ref = [y_ref, conc1];
    y_test = [y_test, conc2];
            
end
    
L3 = min(length(reference.Time),length(test.Time));
area_test = sum(y_test);
area_ref = sum(y_ref);
    %area_diff = sum(y_test-y_ref);
area_diff = sum(abs(y_test-y_ref));
area_max = sum(max(y_test,y_ref));
    
    
    
m1 = abs(area_test - area_ref)/(area_test + area_ref);%error integral 
m2 = area_diff/area_max; %incremental integral error
    %me = mean(Error2)
    %Error2 = [Error2 name]
%y_test = [y_test, Conc_Time(x(j),test,spec2)]; 
%E = [y_test; y_ref]
E = m2;

end

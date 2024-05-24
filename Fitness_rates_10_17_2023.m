function [Fitness]=Fitness_yield_5_31_23_neutralweighting(reference,test, iep1, iep2, isopn1, isopn2)
isop = ErrorCalc8_lumped(reference,test,"ISOP","ISOP");

isopn = ErrorCalc8_lumped(reference,test,isopn1,"ISOPN");


oh_ref_prod = TotalProdRate2('OH',reference);
oh_test_prod = TotalProdRate2('OH',test);
oh_ref_con = TotalConRate2('OH',reference);
oh_test_con = TotalConRate2('OH',test);
oh_ref_net = oh_ref_prod + oh_ref_con;
oh_test_net = oh_test_prod + oh_test_con;
%oh = abs(oh_ref_net/3.3)*abs(oh_ref_net-oh_test_net)/max((abs(oh_ref_net) + abs(oh_test_net)),1e-20);
oh = abs(oh_ref_net-oh_test_net)/max((abs(oh_ref_net) + abs(oh_test_net)),1e-20);


no_ref_prod = TotalProdRate2('NO',reference);
no_test_prod = TotalProdRate2('NO',test);
no_ref_con = TotalConRate2('NO',reference);
no_test_con = TotalConRate2('NO',test);
no_ref_net = no_ref_prod + no_ref_con;
no_test_net = no_test_prod + no_test_con;
%no = abs(no_ref_net/2.46)*abs(no_ref_net-no_test_net)/max((abs(no_ref_net) + abs(no_test_net)),1e-20);
no = abs(no_ref_net-no_test_net)/max((abs(no_ref_net) + abs(no_test_net)),1e-20);


no2_ref_prod = TotalProdRate2('NO2',reference);
no2_test_prod = TotalProdRate2('NO2',test);
no2_ref_con = TotalConRate2('NO2',reference);
no2_test_con = TotalConRate2('NO2',test);
no2_ref_net = no2_ref_prod + no2_ref_con;
no2_test_net = no2_test_prod + no2_test_con;
%no2 = abs(no2_ref_net/2.32)*abs(no2_ref_net-no2_test_net)/max((abs(no2_ref_net) + abs(no2_test_net)),1e-20);
no2 = abs(no2_ref_net-no2_test_net)/max((abs(no2_ref_net) + abs(no2_test_net)),1e-20);


o3_ref_prod = TotalProdRate2('O3',reference);
o3_test_prod = TotalProdRate2('O3',test);
o3_ref_con = TotalConRate2('O3',reference);
o3_test_con = TotalConRate2('O3',test);
o3_ref_net = o3_ref_prod + o3_ref_con;
o3_test_net = o3_test_prod + o3_test_con;
o3 = abs(o3_ref_net-o3_test_net)/max((abs(o3_ref_net) + abs(o3_test_net)),1e-20);

ho2_ref_prod = TotalProdRate2('HO2',reference);
ho2_test_prod = TotalProdRate2('HO2',test);
ho2_ref_con = TotalConRate2('HO2',reference);
ho2_test_con = TotalConRate2('HO2',test);
ho2_ref_net = ho2_ref_prod + ho2_ref_con;
ho2_test_net = ho2_test_prod + ho2_test_con;
%ho2 = abs(ho2_ref_net/2.42)*abs(ho2_ref_net-ho2_test_net)/max((abs(ho2_ref_net) + abs(ho2_test_net)),1e-20);
ho2 = abs(ho2_ref_net-ho2_test_net)/max((abs(ho2_ref_net) + abs(ho2_test_net)),1e-20);


mo2_ref_prod = TotalProdRate2('CH3OO',reference);
mo2_test_prod = TotalProdRate2('CH3OO',test);
mo2_ref_con = TotalConRate2('CH3OO',reference);
mo2_test_con = TotalConRate2('CH3OO',test);
mo2_ref_net = mo2_ref_prod + mo2_ref_con;
mo2_test_net = mo2_test_prod + mo2_test_con;
mo2 = abs(mo2_ref_net-mo2_test_net)/max((abs(mo2_ref_net) + abs(mo2_test_net)),1e-20);

aco3_ref_prod = TotalProdRate2('CH3CO3',reference);
aco3_test_prod = TotalProdRate2('CH3CO3',test);
aco3_ref_con = TotalConRate2('CH3CO3',reference);
aco3_test_con = TotalConRate2('CH3CO3',test);
aco3_ref_net = aco3_ref_prod + aco3_ref_con;
aco3_test_net = aco3_test_prod + aco3_test_con;
aco3 = abs(aco3_ref_net-aco3_test_net)/max((abs(aco3_ref_net) + abs(aco3_test_net)),1e-20);

iepox_ref_prod = 0;
%iepox_test_prod = 0;
liepox = length(iep1);
for i = 1:liepox
    iepox_ref_prod = iepox_ref_prod + TotalProdRate2(iep1(i),reference);
    %iepox_test_prod = iepox_test_prod + TotalProdRate2(iep1(i),test);
end
iepox_test_prod = TotalProdRate2('IEPOX',test);
%iepox = abs(iepox_ref_prod/0.52)*abs(iepox_ref_prod-iepox_test_prod)/max((iepox_ref_prod + iepox_test_prod),1e-20);
iepox = abs(iepox_ref_prod-iepox_test_prod)/max((iepox_ref_prod + iepox_test_prod),1e-20);


hcho_ref_prod = TotalProdRate2('HCHO',reference);
hcho_test_prod = TotalProdRate2('HCHO',test);
%hcho = abs(hcho_ref_prod/2.0)*abs(hcho_ref_prod-hcho_test_prod)/max((hcho_ref_prod + hcho_test_prod),1e-20);
hcho = abs(hcho_ref_prod-hcho_test_prod)/max((hcho_ref_prod + hcho_test_prod),1e-20);


mvk_ref_prod = TotalProdRate2('MVK',reference);
mvk_test_prod = TotalProdRate2('MVK',test);
%mvk = abs(mvk_ref_prod/1.26)*abs(mvk_ref_prod-mvk_test_prod)/max((mvk_ref_prod + mvk_test_prod),1e-20);
mvk = abs(mvk_ref_prod-mvk_test_prod)/max((mvk_ref_prod + mvk_test_prod),1e-20);


gly_ref_prod = TotalProdRate2('GLYX',reference);
gly_test_prod = TotalProdRate2('GLYX',test);
%gly = abs(gly_ref_prod/0.10)*abs(gly_ref_prod-gly_test_prod)/max((gly_ref_prod + gly_test_prod),1e-20);
gly = abs(gly_ref_prod-gly_test_prod)/max((gly_ref_prod + gly_test_prod),1e-20);

macr_ref_prod = TotalProdRate2('MACR',reference);
macr_test_prod = TotalProdRate2('MACR',test);
%macr = abs(macr_ref_prod/0.64)*abs(macr_ref_prod-macr_test_prod)/max((macr_ref_prod + macr_test_prod),1e-20);
macr = abs(macr_ref_prod-macr_test_prod)/max((macr_ref_prod + macr_test_prod),1e-20);


mgly_ref_prod = TotalProdRate2('MGLY',reference);
mgly_test_prod = TotalProdRate2('MGLY',test);
%mgly = abs(mgly_ref_prod/0.42)*abs(mgly_ref_prod-mgly_test_prod)/max((mgly_ref_prod + mgly_test_prod),1e-20);
mgly = abs(mgly_ref_prod-mgly_test_prod)/max((mgly_ref_prod + mgly_test_prod),1e-20);


%mpan_ref_prod = TotalProdRate2('MPAN',reference);
%mpan_test_prod = TotalProdRate2('MPAN',test);
%mpan = abs(mpan_ref_prod-mpan_test_prod)/max((mpan_ref_prod + mpan_test_prod),1e-20);

Fitness = (oh + ho2 + no + no2 + 0.5*isop + 1.0*hcho + o3 + iepox + 0.5*macr + 0.5*mvk + 0.5*gly + 0.5*mgly + 0.8*aco3 + 0.8*mo2 + 0.8*isopn)/11.4;
%Fitness = no2
%Fitness = [oh_ref_net; ho2_ref_net; no_ref_net; no2_ref_net; hcho_ref_prod; iepox_ref_prod; macr_ref_prod; mvk_ref_prod; gly_ref_prod; mgly_ref_prod]
%Fitness = [isop; no; no2; oh; ho2; o3; hcho; iepox; isopn; macr; mvk; gly; mgly]%; gly; mgly]
%Fitness = ["IEPOX",iepox; "NO",no; "NO2",no2; "HO",ho; "HO2",ho2; "NO3",no3; "ISOP",isop; "O3",o3; "PAN",pan; "HCHO",hcho; "MGLY",mgly;"GLY",gly;"ISOPN",isopn;"ACO3",aco3;"MO2",mo2]

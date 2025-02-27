from ocelot import * 
tws = Twiss()
tws.beta_x  = 37.54211739011395
tws.beta_y  = 51.01243050598847
tws.alpha_x = -0.9923633275136321
tws.alpha_y = 1.3038018698269638
tws.E = 14
# Drifts
d_1 = Drift(l=1.0, eid='D_1')
d_2 = Drift(l=11.39, eid='D_2')
d_3 = Drift(l=0.205, eid='D_3')
d_4 = Drift(l=0.14, eid='D_4')
d_5 = Drift(l=9.315, eid='D_5')
d_14 = Drift(l=17.095, eid='D_14')
d_15 = Drift(l=0.21045, eid='D_15')
d_16 = Drift(l=0.15545, eid='D_16')
d_17 = Drift(l=1.545, eid='D_17')
d_20 = Drift(l=9.06, eid='D_20')
d_21 = Drift(l=0.185, eid='D_21')
d_22 = Drift(l=0.182, eid='D_22')
d_23 = Drift(l=0.21845, eid='D_23')
d_24 = Drift(l=0.385465, eid='D_24')
d_25 = Drift(l=1.070165, eid='D_25')
d_26 = Drift(l=3.59515, eid='D_26')
d_27 = Drift(l=0.34515, eid='D_27')
d_28 = Drift(l=0.29015, eid='D_28')
d_29 = Drift(l=0.6718, eid='D_29')
d_30 = Drift(l=2.1168, eid='D_30')
d_33 = Drift(l=1.3218, eid='D_33')
d_34 = Drift(l=1.0768, eid='D_34')
d_35 = Drift(l=0.19, eid='D_35')
d_37 = Drift(l=0.370165, eid='D_37')
d_38 = Drift(l=0.875015, eid='D_38')
d_41 = Drift(l=9.835, eid='D_41')
d_47 = Drift(l=18.61, eid='D_47')
d_50 = Drift(l=21.065, eid='D_50')
d_62 = Drift(l=11.515, eid='D_62')
d_63 = Drift(l=7.87226, eid='D_63')
d_72 = Drift(l=9.676, eid='D_72')

# Quadrupoles
qe_2756_t5 = Quadrupole(l=0.24, k1=-0.21551678208333336, eid='QE.2756.T5')
qe_2766_t5 = Quadrupole(l=0.24, k1=0.12554847, eid='QE.2766.T5')
qe_2776_t5 = Quadrupole(l=0.24, k1=0.13321901208333334, eid='QE.2776.T5')
qe_2786_t5 = Quadrupole(l=0.24, k1=-0.21171532291666667, eid='QE.2786.T5')
qh_2804_t5 = Quadrupole(l=1.0291, k1=0.19652570644252262, eid='QH.2804.T5')
qh_2807_t5 = Quadrupole(l=1.0291, k1=-0.19652283169759988, eid='QH.2807.T5')
qh_2819_t5 = Quadrupole(l=1.0291, k1=0.29487967223787775, eid='QH.2819.T5')
qm_2824_t5 = Quadrupole(l=1.0597, k1=-0.2866762792299707, eid='QM.2824.T5')
qm_2829_t5 = Quadrupole(l=1.0597, k1=0.2878854605076908, eid='QM.2829.T5')
qm_2834_t5 = Quadrupole(l=1.0597, k1=-0.2866762792299707, eid='QM.2834.T5')
qm_2839_t5 = Quadrupole(l=1.0597, k1=0.2878854605076908, eid='QM.2839.T5')
qh_2844_t5 = Quadrupole(l=1.0291, k1=-0.2947601294334856, eid='QH.2844.T5')
qh_2855_t5 = Quadrupole(l=1.0291, k1=0.19652570644252262, eid='QH.2855.T5')
qh_2858_t5 = Quadrupole(l=1.0291, k1=-0.19652283169759988, eid='QH.2858.T5')
qe_2878_t5 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2878.T5')
qe_2900_t5 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2900.T5')
qe_2922_t5 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2922.T5')
qe_2943_t5 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2943.T5')
qe_2965_t5 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.2965.T5')
qe_2985_un2 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.2985.UN2')
qe_3007_un2 = Quadrupole(l=0.24, k1=0.19227955166666666, eid='QE.3007.UN2')
qe_3029_un2 = Quadrupole(l=0.24, k1=-0.19227955166666666, eid='QE.3029.UN2')

# SBends
be_2821_t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid='BE.2821.T5')
be_2841_t5 = SBend(l=2.5, angle=-0.0169497, e1=-0.00847485, e2=-0.00847485, eid='BE.2841.T5')

# Sextupoles
saox_2831_t5 = Sextupole(l=0.3164, k2=-16.23261694, eid='SAOX.2831.T5')
sao_2836_t5 = Sextupole(l=0.3164, k2=-5.755372945998736, eid='SAO.2836.T5')

# Hcors
cex_2766_t5 = Hcor(l=0.1, eid='CEX.2766.T5')
cex_2776_t5 = Hcor(l=0.1, eid='CEX.2776.T5')
chx_2805_t5 = Hcor(l=0.2, eid='CHX.2805.T5')
chx_2817_t5 = Hcor(l=0.2, eid='CHX.2817.T5')
chx_2830_t5 = Hcor(l=0.2, eid='CHX.2830.T5')
chx_2838_t5 = Hcor(l=0.2, eid='CHX.2838.T5')
chx_2856_t5 = Hcor(l=0.2, eid='CHX.2856.T5')
cex_2879_t5 = Hcor(l=0.1, eid='CEX.2879.T5')
cex_2922_t5 = Hcor(l=0.1, eid='CEX.2922.T5')
cex_2966_t5 = Hcor(l=0.1, eid='CEX.2966.T5')
cex_3007_un2 = Hcor(l=0.1, eid='CEX.3007.UN2')

# Vcors
cey_2756_t5 = Vcor(l=0.1, eid='CEY.2756.T5')
cey_2786_t5 = Vcor(l=0.1, eid='CEY.2786.T5')
chy_2808_t5 = Vcor(l=0.2, eid='CHY.2808.T5')
chy_2818_t5 = Vcor(l=0.2, eid='CHY.2818.T5')
chy_2835_t5 = Vcor(l=0.2, eid='CHY.2835.T5')
chy_2845_t5 = Vcor(l=0.2, eid='CHY.2845.T5')
chy_2859_t5 = Vcor(l=0.2, eid='CHY.2859.T5')
cey_2900_t5 = Vcor(l=0.1, eid='CEY.2900.T5')
cey_2944_t5 = Vcor(l=0.1, eid='CEY.2944.T5')
cey_2986_un2 = Vcor(l=0.1, eid='CEY.2986.UN2')
cey_3029_un2 = Vcor(l=0.1, eid='CEY.3029.UN2')

# Monitors
bpma_2756_t5 = Monitor(eid='BPMA.2756.T5')
bpma_2766_t5 = Monitor(eid='BPMA.2766.T5')
bpma_2776_t5 = Monitor(eid='BPMA.2776.T5')
bpma_2786_t5 = Monitor(eid='BPMA.2786.T5')
bpma_2804_t5 = Monitor(eid='BPMA.2804.T5')
bpma_2807_t5 = Monitor(eid='BPMA.2807.T5')
bpma_2818_t5 = Monitor(eid='BPMA.2818.T5')
bpma_2828_t5 = Monitor(eid='BPMA.2828.T5')
bpma_2833_t5 = Monitor(eid='BPMA.2833.T5')
bpma_2838_t5 = Monitor(eid='BPMA.2838.T5')
bpma_2843_t5 = Monitor(eid='BPMA.2843.T5')
bpma_2855_t5 = Monitor(eid='BPMA.2855.T5')
bpma_2858_t5 = Monitor(eid='BPMA.2858.T5')
bpma_2878_t5 = Monitor(eid='BPMA.2878.T5')
bpma_2900_t5 = Monitor(eid='BPMA.2900.T5')
bpma_2921_t5 = Monitor(eid='BPMA.2921.T5')
bpma_2943_t5 = Monitor(eid='BPMA.2943.T5')
bpma_2965_t5 = Monitor(eid='BPMA.2965.T5')
bpma_2985_un2 = Monitor(eid='BPMA.2985.UN2')
bpma_3007_un2 = Monitor(eid='BPMA.3007.UN2')
bpma_3028_un2 = Monitor(eid='BPMA.3028.UN2')

# Markers
tora_2744_t5 = Marker(eid='TORA.2744.T5')
tora_2977_t5 = Marker(eid='TORA.2977.T5')
ensec_3039_un2 = Marker(eid='ENSEC.3039.UN2')

# Lattice 
cell = (d_1, tora_2744_t5, d_2, bpma_2756_t5, d_3, qe_2756_t5, d_4, cey_2756_t5, d_5, 
bpma_2766_t5, d_3, qe_2766_t5, d_4, cex_2766_t5, d_5, bpma_2776_t5, d_3, qe_2776_t5, d_4, 
cex_2776_t5, d_5, bpma_2786_t5, d_3, qe_2786_t5, d_4, cey_2786_t5, d_14, bpma_2804_t5, d_15, 
qh_2804_t5, d_16, chx_2805_t5, d_17, bpma_2807_t5, d_15, qh_2807_t5, d_16, chy_2808_t5, d_20, 
chx_2817_t5, d_21, chy_2818_t5, d_22, bpma_2818_t5, d_23, qh_2819_t5, d_24, be_2821_t5, d_25, 
qm_2824_t5, d_26, bpma_2828_t5, d_27, qm_2829_t5, d_28, chx_2830_t5, d_29, saox_2831_t5, d_30, 
bpma_2833_t5, d_27, qm_2834_t5, d_28, chy_2835_t5, d_33, sao_2836_t5, d_34, chx_2838_t5, d_35, 
bpma_2838_t5, d_27, qm_2839_t5, d_37, be_2841_t5, d_38, bpma_2843_t5, d_15, qh_2844_t5, d_16, 
chy_2845_t5, d_41, bpma_2855_t5, d_15, qh_2855_t5, d_16, chx_2856_t5, d_17, bpma_2858_t5, d_15, 
qh_2858_t5, d_16, chy_2859_t5, d_47, bpma_2878_t5, d_3, qe_2878_t5, d_4, cex_2879_t5, d_50, 
bpma_2900_t5, d_3, qe_2900_t5, d_4, cey_2900_t5, d_50, bpma_2921_t5, d_3, qe_2922_t5, d_4, 
cex_2922_t5, d_50, bpma_2943_t5, d_3, qe_2943_t5, d_4, cey_2944_t5, d_50, bpma_2965_t5, d_3, 
qe_2965_t5, d_4, cex_2966_t5, d_62, tora_2977_t5, d_63, bpma_2985_un2, d_3, qe_2985_un2, d_4, 
cey_2986_un2, d_50, bpma_3007_un2, d_3, qe_3007_un2, d_4, cex_3007_un2, d_50, bpma_3028_un2, d_3, 
qe_3029_un2, d_4, cey_3029_un2, d_72, ensec_3039_un2)

# power supplies 

#  
qe_2756_t5.ps_id = 'QE.3.T5'
qe_2766_t5.ps_id = 'QE.4.T5'
qe_2776_t5.ps_id = 'QE.5.T5'
qe_2786_t5.ps_id = 'QE.6.T5'
qh_2804_t5.ps_id = 'QH.3.T5'
qh_2807_t5.ps_id = 'QH.4.T5'
qh_2819_t5.ps_id = 'QH.1.T5'
qm_2824_t5.ps_id = 'QM.2.T5'
qm_2829_t5.ps_id = 'QM.1.T5'
qm_2834_t5.ps_id = 'QM.2.T5'
qm_2839_t5.ps_id = 'QM.1.T5'
qh_2844_t5.ps_id = 'QH.2.T5'
qh_2855_t5.ps_id = 'QH.3.T5'
qh_2858_t5.ps_id = 'QH.4.T5'
qe_2878_t5.ps_id = 'QE.1.T5'
qe_2900_t5.ps_id = 'QE.2.T5'
qe_2922_t5.ps_id = 'QE.1.T5'
qe_2943_t5.ps_id = 'QE.2.T5'
qe_2965_t5.ps_id = 'QE.1.T5'
qe_2985_un2.ps_id = 'QE.2.UN2'
qe_3007_un2.ps_id = 'QE.1.UN2'
qe_3029_un2.ps_id = 'QE.2.UN2'

#  
saox_2831_t5.ps_id = 'SAOX.1.T5'
sao_2836_t5.ps_id = 'SAO.2.T5'

#  

#  

#  
be_2821_t5.ps_id = 'BE.1.T5'
be_2841_t5.ps_id = 'BE.1.T5'

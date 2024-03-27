#############################################################
########## General settings
#############################################################
# flag to be Tested
#cutpass80 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.967083,0.929117,0.726311)
#cutpass90 = '(( abs(probe_sc_eta) < 0.8 && probe_Ele_nonTrigMVA > %f ) ||  ( abs(probe_sc_eta) > 0.8 && abs(probe_sc_eta) < 1.479&& probe_Ele_nonTrigMVA > %f ) || ( abs(probe_sc_eta) > 1.479 && probe_Ele_nonTrigMVA > %f ) )' % (0.913286,0.805013,0.358969)

# flag to be Tested
flags = {
    'passingCutBasedVeto94XV2'    : '(passingCutBasedVeto94XV2   == 1)',
    'passingCutBasedLoose94XV2'   : '(passingCutBasedLoose94XV2  == 1)',
    'passingCutBasedMedium94XV2'  : '(passingCutBasedMedium94XV2 == 1)',
    'passingCutBasedTight94XV2'   : '(passingCutBasedTight94XV2  == 1)',
    'passingMVA94Xwp80isoV2' : '(passingMVA94Xwp80isoV2 == 1)',
    'passingMVA94Xwp90isoV2' : '(passingMVA94Xwp90isoV2 == 1)',
    'passingMVA94Xwp80noisoV2' : '(passingMVA94Xwp80noisoV2 == 1)',
    'passingMVA94Xwp90noisoV2' : '(passingMVA94Xwp90noisoV2 == 1)',
    'passingMVA94XwpLisoV2'    : '(passingMVA94XwpLisoV2 == 1)',
    'passingMVA94XwpLnoisoV2'  : '(passingMVA94XwpLnoisoV2 == 1)',
    'passingMVA94XwpHZZisoV2'  : '(passingMVA94XwpHZZisoV2 == 1)',
    'passingMVASummer18ULwpHZZ': '(passingMVASummer18ULwpHZZ == 1)',
    'passingMVASummer18ULwpHZZ_sipdzdxy' : '(passingMVASummer18ULwpHZZ == 1 && fabs(el_sip) < 4 && fabs(el_dz) < 1 && fabs(el_dxy) < 0.5)'
    }

baseOutDir = 'results/Run3_CD_V2/tnpEleID/'

#############################################################
########## samples definition  - preparing the samples
#############################################################
### samples are defined in etc/inputs/tnpSampleDef.py
### not: you can setup another sampleDef File in inputs
import etc.inputs.tnpSampleDef as tnpSamples
tnpTreeDir = 'tnpEleIDs'

samplesDef = {
    'data'   : tnpSamples.Run3['data_Run3C'].clone(),
    'mcNom'  : tnpSamples.Run3['DYto2E_powheg_preEE'].clone(),
    #'mcAlt'  : tnpSamples.Run3['DY_amcatnlo_postEE'].clone(),
    #'tagSel' : tnpSamples.Run3['DYto2E_powheg_postEE'].clone(),
}

## can add data sample easily
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3C'] )
samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3D'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3E'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3F'] )
#samplesDef['data'].add_sample( tnpSamples.Run3['data_Run3G'] )

## some sample-based cuts... general cuts defined here after
## require mcTruth on MC DY samples and additional cuts
## all the samples MUST have different names (i.e. sample.name must be different for all)
## if you need to use 2 times the same sample, then rename the second one
#samplesDef['data'  ].set_cut('run >= 273726')
samplesDef['data' ].set_tnpTree(tnpTreeDir)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_tnpTree(tnpTreeDir)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_tnpTree(tnpTreeDir)

if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_mcTruth()
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_mcTruth()
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_mcTruth()
#if not samplesDef['tagSel'] is None:
#    samplesDef['tagSel'].rename('mcAltSel_DY_madgraph')
#    samplesDef['tagSel'].set_cut('tag_Ele_pt > 37') #canceled non trig MVA cut


## set MC weight, can use several pileup rw for different data taking periods
#weightName = 'weights_data_Run2022_B-G.totWeight'
weightName = 'weights_data_Run2022_inclusive.totWeight'
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_weight(weightName)
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_weight(weightName)
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_weight(weightName)
if not samplesDef['mcNom' ] is None: samplesDef['mcNom' ].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')
#if not samplesDef['mcAlt' ] is None: samplesDef['mcAlt' ].set_puTree('/eos/cms/store/group/phys_egamma/swmukher/UL2017/PU_miniAOD/DY_amcatnloext_ele.pu.puTree.root')
#if not samplesDef['tagSel'] is None: samplesDef['tagSel'].set_puTree('/eos/cms/store/group/phys_egamma/ec/fmausolf/EGM_comm/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8/DYToEE_M-50_NNPDF31_TuneCP5_13p6TeV-powheg-pythia8_EleID_PhoID/221018_080249/0000/DY_powheg_ele.pu.puTree.root')

#############################################################
########## bining definition  [can be nD bining]
#############################################################
'''
biningDef = [
   { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5,-2.0,-1.566,-1.4442, -0.8, 0.0, 0.8, 1.4442, 1.566, 2.0, 2.5] },
   { 'var' : 'el_pt' , 'type': 'float', 'bins': [7,15,20,35,50,100,500] },
]
'''

'''
biningDef = [ 
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.0, -1.566, -0.8, 0, 0.8, 1.566, 2.0, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 15, 20, 35, 50, 100, 500] },
]
'''
biningDef = [ 
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, -2.0, -1.566, -0.8, 0, 0.8, 1.566, 2.0, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 15, 20, 35, 50, 100, 500] },
]
'''
biningDef = [ 
    { 'var' : 'el_sc_eta' , 'type': 'float', 'bins': [-2.5, 0, 2.5] },
    { 'var' : 'el_pt' , 'type': 'float', 'bins': [7, 35, 500] },
]
'''
#############################################################
########## Cuts definition for all samples
#############################################################
### cut
cutBase   = 'tag_Ele_pt > 30 && abs(tag_sc_eta) < 2.17 && el_q*tag_Ele_q < 0 && el_isGap==0'

'''
additionalCuts = { 
    0 : 'tag_Ele_pt > 50 && el_3charge == 1',
    1 : 'tag_Ele_pt > 50 && el_3charge == 1',
    2 : 'tag_Ele_pt > 50 && el_3charge == 1',
    3 : 'tag_Ele_pt > 50 && el_3charge == 1',
    4 : 'tag_Ele_pt > 50 && el_3charge == 1',
    5 : 'tag_Ele_pt > 50 && el_3charge == 1',
    6 : 'tag_Ele_pt > 50 && el_3charge == 1',
    7 : 'tag_Ele_pt > 50 && el_3charge == 1'
}
'''
additionalCuts = { 
    0 : 'tag_Ele_pt > 50',
    1 : 'tag_Ele_pt > 50',
    2 : 'tag_Ele_pt > 50',
    3 : 'tag_Ele_pt > 50',
    4 : 'tag_Ele_pt > 50',
    5 : 'tag_Ele_pt > 50',
    6 : 'tag_Ele_pt > 50',
    7 : 'tag_Ele_pt > 50'
}

#### or remove any additional cut (default)

#additionalCuts = None

#############################################################
########## fitting params to tune fit by hand if necessary
#############################################################
tnpParNomFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "acmsP[60.,50.,80.]","betaP[0.05,0.01,0.08]","gammaP[0.1, -2, 2]","peakP[90.0]",
    #"acmsF[60.,20.,80.]","betaF[0.05,0.01,0.08]","gammaF[0.1, -2, 2]","peakF[90.0]",
    #"acmsF[60.,20.,80.]","betaF[0.05,-0.2,0.2]","gammaF[0.1,-2,2]","peakF[90.0]",
    "{a0[-0.9,-1.5,-0.5],a1[0.2,0.,0.5],a2[0.,-0.5,0.5]}",
    #"{a0[-0.84,-1.2,-0.0],a1[0.324,0.2,0.4],a2[-0.088,-0.15,-0.0]}",
    #"{a0[-0.8,-0.9,-0.7],a1[0.273,0.2,0.35],a2[-0.054.,-0.05,-0.06]}",
    ]

tnpParAltSigFit = [
    #"meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.1,2.0]",
    "meanF[-0.0,-4.0,0.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,0.2,2.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.1,2.0]",
    "meanP[1.0,-4.0,0.0]","sigmaP[2.4,2.0,3.8]","alphaP[2.0,0.2,2.5]",'nP[3.0,1.0,6.0]',"sigmaP_2[2.011,1.0,3.0]","sosP[1,0.1,2.0]",
    #"meanF[0.97,0.7,1.3]","sigmaF[0.67,0.5,1.0]","alphaF[-0.67,-0.4,-0.3]",'nF[0.975,0.7,1.3]',"sigmaF_2[1.928,1.6,2.5]","sosF[1.902,1.8,2.0]",
    #"meanF[1.0,0.5,1.5]","sigmaF[1.25,1.0,1.5]","alphaF[-1.0,-3.0,0.0]",'nF[1.0,0.0,6.0]',"sigmaF_2[2.15,1.8,2.4]","sosF[1.403]",
    #"acmsP[60.,50.,150.]","betaP[0.04,-0.01,0.06]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
    #"acmsP[60.,50.,75.]","betaP[0.05,0.0,0.11]","gammaP[0.22,0.0,0.3]","peakP[90.0]",
    "acmsP[60.,50.,150.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.001, 1]","peakP[90.0]",
    #"acmsF[60.,50.,75.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.008, 1]","peakF[90.0]",
    #"acmsF[85,70.,100.]","betaF[0.05,0.0,0.1]","gammaF[0.1, 0.001, 1]","peakF[90.0]",
    #"acmsF[150.0,100.0,200.0]","betaF[0.1,0.02,0.2]","gammaF[0.1, 0.001, 1]","peakF[90.0]",
    #"acmsF[106,100,150]","betaF[0.164,0.0,0.2]","gammaF[0.019,0.0,1]","peakF[90.0]",
    "{a0[-0.84,-2.2,-0.0],a1[0.324,0.2,0.4],a2[-0.088,-0.15,-0.0]}",
    #"{a0[-0.731,-0.74,-0.72],a1[0.27,0.26,0.28],a2[-0.046,-0.05,-0.04]}",
    ]

tnpParAltSigFit_addGaus = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[1,0.7,6.0]","alphaP[2.0,1.2,3.5]" ,'nP[3,-5,5]',"sigmaP_2[1.5,0.5,6.0]","sosP[1,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[2,0.7,6.0]","alphaF[2.0,1.2,3.5]",'nF[3,-5,5]',"sigmaF_2[2.0,0.5,6.0]","sosF[1,0.5,5.0]",
    "meanGF[80.0,70.0,100.0]","sigmaGF[15,5.0,125.0]",
    "acmsP[60.,50.,75.]","betaP[0.04,0.01,0.06]","gammaP[0.1, 0.005, 1]","peakP[90.0]",
    "acmsF[60.,50.,85.]","betaF[0.04,0.01,0.06]","gammaF[0.1, 0.005, 1]","peakF[90.0]",
    ]
         
tnpParAltBkgFit = [
    "meanP[-0.0,-5.0,5.0]","sigmaP[0.9,0.5,5.0]",
    "meanF[-0.0,-5.0,5.0]","sigmaF[0.9,0.5,5.0]",
    "alphaP[0.,-5.,5.]",
    #"alphaF[0.,-5.,5.]",
    #"{a0[0.15,0.002,0.3],a1[15,13,20],a2[38,18,48]}",
    "a0[1.87,1.7,7.5]","a1[14.7,13.7,15.7]","a2[30,28,62]" #the best combination
    #"a0[0.01,0.005,0.0.03]","a1[125,50,100]","a2[40,35,45]"
    ]

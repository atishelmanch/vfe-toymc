//
// MultiFit amplitude reconstruction
// To run:
// > g++ -o Example07.multifit.exe Example07.multifit.cc PulseChiSqSNNLS.cc -std=c++11 `root-config --cflags --glibs`
// > ./Example07.multifit.exe
//

#include <iostream>
#include "PulseChiSqSNNLS.h"
#include "Pulse.h"

#include "TTree.h"
#include "TF1.h"
#include "TProfile.h"
#include "TH2.h"
#include "TFile.h"


void run(
    std::string in_file_name, std::string out_file_name){
 
  std::cout << " run ..." << std::endl;
 
  std::cout << " in_file_name = " << in_file_name << std::endl;
  TFile *input_file = new TFile(in_file_name.c_str());

  
  int NSAMPLES;
  float NFREQ;
  std::string *wf_name = new std::string;
  
  std::vector<double>* samples = new std::vector<double>;
  double amplitudeTruth;
  TTree *tree = (TTree*) input_file->Get("Samples");
  tree->SetBranchAddress("amplitudeTruth",      &amplitudeTruth);
  tree->SetBranchAddress("samples",             &samples);
  tree->SetBranchAddress("nSmpl",             &NSAMPLES);
  tree->SetBranchAddress("nFreq",             &NFREQ);
  tree->SetBranchAddress("WFNAME",             &wf_name);
 
  int nentries = tree->GetEntries();
  tree->GetEntry(0);
 
  std::cout << " nentries = " << nentries << std::endl;
  std::cout << " NSAMPLES = " << NSAMPLES << std::endl;
  std::cout << " amplitudeTruth = " << amplitudeTruth << std::endl;
  std::cout << " Test line. You've made it to this point." << std::endl;
  std::cout << " wf_name = " << wf_name << std::endl;
  std::cout << " You've made it past wf_name " << std::endl;
  int IDSTART = 7*25;
 
  int WFLENGTH = 500*4; //---- step 1/4 ns in waveform
 
  if (( IDSTART + NSAMPLES * NFREQ ) > 500 ) {
    WFLENGTH = (IDSTART + NSAMPLES * NFREQ)*4 + 100;
  }
 
  std::cout << " WFLENGTH = " << WFLENGTH << std::endl;
  std::cout << " NFREQ    = " << NFREQ << std::endl;
 
 
  Pulse pSh;
  pSh.SetNSAMPLES (NSAMPLES);
  pSh.SetNFREQ (NFREQ);
  pSh.SetWFLENGTH(WFLENGTH);
  pSh.SetIDSTART(IDSTART);
 
  std::string wf_file_name = (
      ((std::string) "data/EmptyFile") +
      ((std::string) *wf_name) + 
      ((std::string) ".root"));
  std::cout << wf_file_name << std::endl;

  pSh.SetFNAMESHAPE(wf_file_name);
  pSh.Init();
 
  std::cout << " pSh ready " << std::endl;
 
 
  FullSampleVector fullpulse;
  FullSampleMatrix fullpulsecov;
  SampleMatrix noisecor;
  BXVector activeBX;
  SampleVector amplitudes;
 
  fullpulse.resize(2*NSAMPLES,1);   fullpulse.setZero(); 
  fullpulsecov.resize(2*NSAMPLES,2*NSAMPLES); fullpulsecov.setZero(); 
  noisecor.resize(NSAMPLES,NSAMPLES); noisecor.setZero(); 
  activeBX.resize(Eigen::NoChange,1);
  amplitudes.resize(NSAMPLES,1); amplitudes.setZero(); 
 
  std::cout << " default ready " << std::endl;
 
  std::vector<double> pulseShapeTemplate;
 

  // suzannah: What on earth is (NSAMPLES + 7 * int(25 / NFREQ)) ???
  for(int i=0; i<(NSAMPLES+7*int(25 /NFREQ)); i++) {
   

    // depends on i:
    double this_magic_number;
 
    this_magic_number = double( IDSTART + NFREQ * i + 3*25. - 500 / 2. );  //----> 500 ns is fixed!  
  
    pulseShapeTemplate.push_back( pSh.fShape(this_magic_number));
  
    // suzannah: What on earth is (NSAMPLES + 2 * 25 / NFREQ) ???
    std::cout << " [" << i << "::" << (NSAMPLES+2*25 /NFREQ) << "] --> pSh.fShape(" << this_magic_number << ") = " << pSh.fShape(this_magic_number) << " ---> " << pSh.fShape(this_magic_number) * NFREQ/25. << std::endl;
 
  }
 
  for (int i=1; i<(NSAMPLES + 2*int(25 /NFREQ)); i++) {
  
    fullpulse(i + 7 * int(25 /NFREQ)) = pulseShapeTemplate[i];
  }
 
  //---- correlation
  for (int i=0; i<NSAMPLES; ++i) {
    for (int j=0; j<NSAMPLES; ++j) {
      int vidx = std::abs(j-i);
    noisecor(i,j) = pSh.corr(vidx);
    }
  }
 
  std::cout << " noise ready " << std::endl;
 
  //----  collision every 25 ns -> this is fixed number
  //----                       number of sampls * frequence in ns / 25 ns
  if ( round((NSAMPLES * NFREQ) / 25.) != (NSAMPLES * NFREQ) / 25 ) {
    std::cout << " Attention please! How do you think multifit can fit a pulse in the middle between collisions!?!?!?!?" << std::endl;
  }
 
  int totalNumberOfBxActive = int(NSAMPLES * NFREQ) / 25; 
  std::cout << " totalNumberOfBxActive = " << totalNumberOfBxActive << std::endl;
 
  std::vector<int> activeBXs;
  for (unsigned int ibx=0; ibx<totalNumberOfBxActive; ++ibx) {

    activeBXs.push_back( ibx * int(25 /NFREQ) - 4 * int(25 /NFREQ) ); //----> -5 BX are active w.r.t. 0 BX
  
    std::cout << " activeBXs[" << ibx << "] = " << activeBXs[ibx] << std::endl;
  }
 
  activeBX.resize(totalNumberOfBxActive);
  for (unsigned int ibx=0; ibx<totalNumberOfBxActive; ++ibx) {
    activeBX.coeffRef(ibx) = activeBXs[ibx];
  } 
 
  std::cout << " end init " << std::endl;
 
 
 
  TFile *output_file;
  TH1D *h01;
 
  std::vector<TH1F*> v_pulses;
  std::vector<TH1F*> v_amplitudes_reco;
 
  std::cout << " out_file_name = " << out_file_name << std::endl;
  output_file = new TFile(out_file_name.c_str(),"recreate");
  h01 = new TH1D("h01", "dA", 5000, -5.0, 5.0);
  //h01 = new TH1D("h01", "dA", 100, -0.15, 0.15);
 
  output_file->cd();
  TTree* newtree = (TTree*) tree->CloneTree(0); //("RecoAndSim");
  newtree->SetName("RecoAndSim");
 
  std::vector <double> samplesReco;
  int ipulseintime = 0;
  newtree->Branch("samplesReco",   &samplesReco);
  newtree->Branch("ipulseintime",  ipulseintime,  "ipulseintime/I");
  newtree->Branch("activeBXs",     &activeBXs);
  newtree->Branch("pulseShapeTemplate",   &pulseShapeTemplate);
  std::cout << " pulseShapeTemplate.size () = " << pulseShapeTemplate.size() << std::endl;
 
  double chiSquare = 0;
  newtree->Branch("chiSquare", &chiSquare, "chiSquare/D");
 
  int outerIterations = 0;
  newtree->Branch("outerIterations", &outerIterations, "outerIterations/I");
  int outerIterationsCheck = 0;
  newtree->Branch("outerIterationsCheck", &outerIterations, "outerIterations/I");
  std::vector <int> innerIterations;
  newtree->Branch("innerIterations",   &innerIterations);
 
  for (unsigned int ibx=0; ibx<totalNumberOfBxActive; ++ibx) {
    samplesReco.push_back(0.);
  }
 
 
  v_amplitudes_reco.clear();
 
  //---- create the multifit
  PulseChiSqSNNLS pulsefunc;
  pulsefunc.setNSAMPLES(NSAMPLES);
  pulsefunc.setNFREQ(NFREQ);
  pulsefunc.Init(); //---- initialization, needed
 
  output_file->cd();
 
  for(int ievt=0; ievt<nentries; ++ievt){
  
    if (!(ievt%100)) {
      std::cout << " ievt = " << ievt << " :: " << nentries << std::endl;
    }
  
    tree->GetEntry(ievt);
  
    for(int i=0; i<NSAMPLES; i++){
      amplitudes[i] = samples->at(i);
    }
  
    double pedval = 0.;
    double pedrms = 1.0;
  
   
    pulsefunc.disableErrorCalculation();
  
    bool status = pulsefunc.DoFit( amplitudes, noisecor, pedrms, activeBX, fullpulse, fullpulsecov );
    double chisq = pulsefunc.ChiSq();
    std::cout << "  >> chisq =       " << chisq << std::endl;
    chiSquare = chisq;

    outerIterations = pulsefunc.OuterIterations();
    outerIterationsCheck = pulsefunc.InnerIterations().size();
    innerIterations = pulsefunc.InnerIterations();
  
    ipulseintime = 0;
    for (unsigned int ipulse=0; ipulse<pulsefunc.BXs()->rows(); ++ipulse) {
      if ( ((int(pulsefunc.BXs()->coeff(ipulse))) * NFREQ/25 + 5) == 0) {
        ipulseintime = ipulse;
        break;
      }
    }
  
    std::cout << "  >> status =       " << status << std::endl;
    double aMax = status ? (*(pulsefunc.X()))[ipulseintime] : 0.;
    if (!status) {
      std::cout << "asdfasdf" << std::endl;
    }
  
    for (unsigned int ipulse=0; ipulse<pulsefunc.BXs()->rows(); ++ipulse) {
      if (status) {
        if (ievt == 0) std::cout << " ip = " << ipulse << " --> [" <<  (int(pulsefunc.BXs()->coeff(ipulse))) << "] --> " << (int(pulsefunc.BXs()->coeff(ipulse))) * NFREQ/25 + 5  << " == " << (*(pulsefunc.X()))[ ipulse ] << std::endl;

          //---- YES
          samplesReco[ (int(pulsefunc.BXs()->coeff(ipulse))) * NFREQ/25 + 5] = (*(pulsefunc.X()))[ ipulse ];
    
      }
      else {
        samplesReco[ipulse] = -1;
      }
    }
  
    std::cout << "  >> aMax =       " << aMax << std::endl;
    std::cout << "  >> amplitudeTruth =       " << amplitudeTruth << std::endl;
    h01->Fill(aMax - amplitudeTruth);
  
    newtree->Fill();
  
  }
  // CONTINUED HERE //
  std::cout << "  Mean of REC-MC = " << h01->GetMean() << " GeV" << std::endl;
  std::cout << "   RMS of REC-MC = " << h01->GetRMS()  << " GeV" << std::endl;
 
 
  output_file->cd();
  std::cout << " done (1) " << std::endl;
  h01->Write();
  std::cout << " done (2) " << std::endl;

  newtree->Write();
  std::cout << " done (3) " << std::endl;
  output_file->Close();
 
  std::cout << " done ... " << std::endl;
 
}

# ifndef __CINT__

int main(int argc, char** argv) {

  std::string in_file_name = "data/samples_signal_10GeV_pu_0.root";
  if (argc>=2) {
    in_file_name = argv[1];
  }
 
  std::string out_file_name = "output.root";
  if (argc>=3) {
    out_file_name = argv[2];
  }
  std::cout << " out_file_name = " << out_file_name << std::endl;
 
  //---- number of samples per impulse
  int NSAMPLES = 10;
  if (argc>=4) {
    NSAMPLES = atoi(argv[3]);
  }
  std::cout << " NSAMPLES = " << NSAMPLES << std::endl;
 
  //---- number of samples per impulse
  float NFREQ = 25;
  if (argc>=5) {
    NFREQ = atof(argv[4]);
  }
  std::cout << " NFREQ = " << NFREQ << std::endl;
 
//  //---- waveform file
//  std::string wf_name = "CRRC43";
//  if (argc>=6) {
//    wf_name = (std::string) argv[5];
//  }
//  std::cout << " wf_name = " << wf_name << std::endl;
 
 
 
  run(in_file_name, out_file_name); //wf_name);
 
  std::cout << " out_file_name = " << out_file_name << std::endl;
 
  return 0;
}

# endif

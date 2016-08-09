//---- plot output of multifit

void plotPulse (std::string nameInputFile = "output.root", std::string nsample, std::string nfreq, std::string nameWF, int nEvent = 10){
 
 Color_t* color = new Color_t [200];
 color[0] = kAzure; //kRed ;
 color[1] = kAzure + 10 ;
 color[2] = kYellow + 2 ;
 color[3] = kGreen ;
 color[4] = kGreen + 4 ;
 color[5] = kBlue ;
 color[6] = kCyan ;
 color[7] = kPink + 1 ;
 color[8] = kBlack ;
 color[9] = kYellow + 4 ;
 for (int i=0; i<30; i++) {
  color[i+10] = kBlue + i;
 }
 
 
 TFile *file = new TFile(nameInputFile.c_str());
 
 TTree* tree = (TTree*) file->Get("RecoAndSim");
  
 int    nWF;
 std::vector<double>* pulse_signal    = new std::vector<double>;
 std::vector<double>* samplesReco = new std::vector<double>;
 std::vector<double>* samples     = new std::vector<double>;
 std::vector<int>*    activeBXs   = new std::vector<int>;
 std::vector<double>* pulseShapeTemplate     = new std::vector<double>;
 
 float NFREQ;
 double chiSquare;
 
 tree->SetBranchAddress("nWF",      &nWF);
 tree->SetBranchAddress("pulse_signal", &pulse_signal);
 tree->SetBranchAddress("samplesReco", &samplesReco);
 tree->SetBranchAddress("samples",   &samples);
 tree->SetBranchAddress("activeBXs", &activeBXs);
 tree->SetBranchAddress("nFreq",   &NFREQ);
 tree->SetBranchAddress("pulseShapeTemplate",   &pulseShapeTemplate);
 tree->SetBranchAddress("chiSquare",      &chiSquare);
 
 
 tree->GetEntry(nEvent);
 std::cout << " NFREQ = " << NFREQ << std::endl;
 
 TCanvas* ccwaveform = new TCanvas ("ccwaveform","",800,600);
 TGraph *gr = new TGraph();
 for(int i=0; i<nWF; i++){
  gr->SetPoint(i, i, pulse_signal->at(i));
 }
 gr->Draw("AL");
 std::string graph_title = nameWF + " Waveform";
 char * graph_title_cst = graph_title.c_str();
 gr->SetTitle(graph_title_cst);
 gr->SetLineColor(kMagenta);
 gr->SetLineWidth(2);
 gr->GetXaxis()->SetTitle("time [ns]");
 std::string png_name = nameWF + "_raw.png";
 char * png_name_cst = png_name.c_str();
 ccwaveform->SaveAs(png_name_cst);
 
 
 TCanvas* ccReco = new TCanvas ("ccReco","",800,600);
 TGraph *grReco = new TGraph();
 for(int i=0; i<samplesReco->size(); i++){
  std::cout << " i, activeBXs->at(i), samplesReco->at(i) = " << i << "::" << samplesReco->size() << " -> " << activeBXs->at(i) << " , " << samplesReco->at(i) << std::endl;
  grReco->SetPoint(i, activeBXs->at(i), samplesReco->at(i));
 }
 grReco->SetMarkerSize(2);
 grReco->SetMarkerStyle(22);
 grReco->SetMarkerColor(kBlue);
 grReco->Draw("ALP");
 grReco->GetXaxis()->SetTitle("BX");
 png_name = nameWF + "_" + nsample + "_" + nfreq + "_reconstructed.png";
 png_name_cst = png_name.c_str();
 graph_title = "Reconstructed " + nameWF + " Pulse: " + nsample + " samples, " + nfreq + "ns period";
 graph_title_cst = graph_title.c_str();
 grReco->SetTitle(graph_title_cst);
 ccReco->SaveAs(png_name_cst);
 
 
 TCanvas* ccPulse = new TCanvas ("ccPulse","",800,600);
 TGraph *grPulse = new TGraph();
 for(int i=0; i<samples->size(); i++){
  grPulse->SetPoint(i, i * NFREQ , samples->at(i));
 }
 grPulse->SetMarkerSize(2);
 grPulse->SetMarkerStyle(21);
 grPulse->SetMarkerColor(kRed);
 grPulse->Draw("ALP");
 grPulse->GetXaxis()->SetTitle("time [ns]");
 png_name = nameWF + "_" + nsample + "_" + nfreq + "_digitized.png";
 png_name_cst = png_name.c_str();
 graph_title = "Digitized " + nameWF + " Waveform: " + nsample + " samples, " + nfreq + "ns period";
 graph_title_cst = graph_title.c_str();
 grPulse->SetTitle(graph_title_cst);
 ccPulse->SaveAs(png_name_cst);
 
 std::cout << " end " << std::endl;

 TCanvas* ccPulseAndReco = new TCanvas ("ccPulseAndReco","",800,600);
 TGraph *grPulseRecoAll = new TGraph();
 TGraph *grPulseReco[100];  // more than enough space
 std::cout << " samplesReco->size() = " << samplesReco->size() << std::endl;
 std::cout << " activeBXs->size() = " << activeBXs->size() << std::endl;
 std::cout << " pulseShapeTemplate->size() = " << pulseShapeTemplate->size() << std::endl;
 std::cout << " samples->size() = " << samples->size() << std::endl;
 
 //TLegend* leg = new TLegend(0.7,0.2,0.9,0.9);
 TLegend* leg = new TLegend(0.9,0.2,1.0,0.9);
 TPaveText* box = new TPaveText(0.9,0.9,1.0,1.0, "NDC");
 
 float totalRecoSpectrum[100];
 for(int i=0; i<samples->size(); i++){ 
  totalRecoSpectrum[i]=0;
 }
 
 
//  for(int iBx=0; iBx<3; iBx++){
 for(int iBx=0; iBx<samplesReco->size(); iBx++){
  std::cout << " iBx = " << iBx << std::endl;
  grPulseReco[iBx] = new TGraph();
  for(int i=0; i<samples->size(); i++){
   std::cout << "  >> i = " << i << std::endl;
   grPulseReco[iBx]->SetPoint(i, i * NFREQ + activeBXs->at(iBx)*NFREQ + 2 * 25, pulseShapeTemplate->at(i) * samplesReco->at(iBx));
  
   int iReco = (i * NFREQ + activeBXs->at(iBx)*NFREQ + 2 * 25) / NFREQ;
   if ( iReco >= 0 && iReco <samples->size() ) {
    totalRecoSpectrum[iReco] += pulseShapeTemplate->at(i) * samplesReco->at(iBx);
   } 
   
  }
  grPulseReco[iBx]->SetMarkerColor(color[iBx]);
  grPulseReco[iBx]->SetLineColor(color[iBx]);
  grPulseReco[iBx]->SetMarkerSize(1);
  grPulseReco[iBx]->SetMarkerStyle(21+iBx);
  TString nameHistoTitle = Form ("BX %d", activeBXs->at(iBx));
  leg->AddEntry(grPulseReco[iBx],nameHistoTitle.Data(),"p");
 }
 
 grPulse->Draw("ALP");
//  for(int iBx=0; iBx<3; iBx++){
 for(int iBx=1; iBx<samplesReco->size(); iBx++){
  grPulseReco[iBx]->Draw("PL");
 }
 
 for(int i=0; i<samples->size(); i++){
  grPulseRecoAll->SetPoint(i, i * NFREQ, totalRecoSpectrum[i]);
 }
 
 TString chiSquareString = Form ("#chi^{2} = %f", chiSquare);
 box->AddText(chiSquareString.Data());
 
 grPulseRecoAll->SetMarkerColor(kMagenta);
 grPulseRecoAll->SetLineColor(kMagenta);
 grPulseRecoAll->SetLineStyle(1);
 grPulseRecoAll->SetMarkerSize(2);
 grPulseRecoAll->SetMarkerStyle(24);
 grPulseRecoAll->Draw("PL");
 leg->AddEntry(grPulseRecoAll,"BX Sum","p");
 grPulse->GetXaxis()->SetTitle("time [ns]");
  

 box->Draw();
 
 leg->Draw();

 png_name = nameWF + "_" + nsample + "_" + nfreq + "_PulseRecoAll.png";
 png_name_cst = png_name.c_str();
 ccPulseAndReco->SaveAs(png_name_cst);
 
 
// --------------------------------------------------------
// Attempting to  extract in time pulse 
// not as E_i*f(time) but as 
// data-sum(all bunch crossings except intime)E_{j}*f(i-j)
// --------------------------------------------------------

 TCanvas* ccNewPulseAndReco = new TCanvas ("ccNewPulseAndReco","",800,600);
 TGraph *grNewPulseRecoAll = new TGraph();
 TGraph *grNewPulseReco[100];  // more than enough space
 std::cout << " samplesReco->size() = " << samplesReco->size() << std::endl;
 std::cout << " activeBXs->size() = " << activeBXs->size() << std::endl;
 std::cout << " pulseShapeTemplate->size() = " << pulseShapeTemplate->size() << std::endl;
 std::cout << " samples->size() = " << samples->size() << std::endl;
 
 //TLegend* leg = new TLegend(0.7,0.2,0.9,0.9);
 TLegend* leg = new TLegend(0.9,0.2,1.0,0.9);
 TPaveText* box = new TPaveText(0.9,0.9,1.0,1.0, "NDC");
 
 float totalRecoSpectrum[100];
 for(int i=0; i<samples->size(); i++){
  totalRecoSpectrum[i]=0;
 }
 
 
//  for(int iBx=0; iBx<3; iBx++){
 for(int iBx=0; iBx<samplesReco->size(); iBx++){ 
  std::cout << " iBx = " << iBx << std::endl;
  if (iBx==4) { //excluding in time bunch cross
  continue;
  }
  grNewPulseReco[iBx] = new TGraph();
  for(int i=0; i<samples->size(); i++){
   std::cout << "  >> i = " << i << std::endl;
   grNewPulseReco[iBx]->SetPoint(i, i * NFREQ + activeBXs->at(iBx)*NFREQ + 2 * 25, pulseShapeTemplate->at(i) * samplesReco->at(iBx));
  
   int iReco = (i * NFREQ + activeBXs->at(iBx)*NFREQ + 2 * 25) / NFREQ;
   if ( iReco >= 0 && iReco <samples->size() ) {
    totalRecoSpectrum[iReco] += pulseShapeTemplate->at(i) * samplesReco->at(iBx);
   } 
   
  }
  grNewPulseReco[iBx]->SetMarkerColor(color[iBx]);
  grNewPulseReco[iBx]->SetLineColor(color[iBx]);
  grNewPulseReco[iBx]->SetMarkerSize(1);
  grNewPulseReco[iBx]->SetMarkerStyle(21+iBx);
  TString nameHistoTitle = Form ("BX %d", activeBXs->at(iBx));
  leg->AddEntry(grNewPulseReco[iBx],nameHistoTitle.Data(),"p");
 }
 
 grPulse->Draw("ALP");
//  for(int iBx=0; iBx<3; iBx++){ 
 for(int iBx=1; iBx<samplesReco->size(); iBx++){
  if (iBx==4) {
  continue;
  }
   grNewPulseReco[iBx]->Draw("PL");
 }
 
 for(int i=0; i<samples->size(); i++){
  grNewPulseRecoAll->SetPoint(i, i * NFREQ, totalRecoSpectrum[i]);
 }
 
 //samples->at(i)-totalRecoSpectrum_nointime[i]
  
 TString chiSquareString = Form ("#chi^{2} = %f", chiSquare);
 box->AddText(chiSquareString.Data());
 
 grNewPulseRecoAll->SetMarkerColor(kMagenta);
 grNewPulseRecoAll->SetLineColor(kMagenta);
 grNewPulseRecoAll->SetLineStyle(1);
 grNewPulseRecoAll->SetMarkerSize(2);
 grNewPulseRecoAll->SetMarkerStyle(24);
 grNewPulseRecoAll->Draw("PL");
 grPulse->GetXaxis()->SetTitle("time [ns]");
 leg->AddEntry(grNewPulseRecoAll,"BX Sum","p");
 
 box->Draw();
 
 leg->Draw();

 png_name = nameWF + "_" + nsample + "_" + nfreq + "_NewPulseRecoAll.png";
 png_name_cst = png_name.c_str();
 ccNewPulseAndReco->SaveAs(png_name_cst);
 
}



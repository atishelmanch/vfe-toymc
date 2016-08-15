using namespace std;

void TestFile (string nameInputFile = "output.root", string nsample, string nfreq, string nameWF, string ps, int nEvent = 0){ // Input File and variable declarations 
 
 //Marker colors and shapes
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

 //30 more colors
 for (int i=0; i<30; i++) { 
  color[i+10] = kBlue + i;
 }
 
 //String of manually entered input file name
 TFile *file = new TFile(nameInputFile.c_str()); 
 
 //Select tree to access branches from
 TTree* tree = (TTree*) file->Get("RecoAndSim");
 
 //Creating pointers for branch information
 int    nWF;
 vector<double>* pulse_signal        = new vector<double>;
 vector<double>* samplesReco         = new vector<double>;
 vector<double>* samples             = new vector<double>;
 vector<int>*    activeBXs           = new vector<int>;
 float  NFREQ;
 vector<double>* pulseShapeTemplate  = new vector<double>;  
 double chiSquare;
 double amplitudeTruth;
 float  pulse_shift;
 
 //Obtaining Branch information
 tree->SetBranchAddress("nWF",                &nWF); //Total number of time entries (x values) for raw waveform
 tree->SetBranchAddress("pulse_signal",       &pulse_signal); //Gives waveform y values
 tree->SetBranchAddress("samplesReco",        &samplesReco); //Incident particle(s?) energy guess
 tree->SetBranchAddress("samples",            &samples); //Raw sample data, samples of waveform every nFreq seconds
 tree->SetBranchAddress("activeBXs",          &activeBXs); //Bunch crossings by number (for ex -4, -3, ..., 5)
 tree->SetBranchAddress("nFreq",              &NFREQ); //Sample time
 tree->SetBranchAddress("pulseShapeTemplate", &pulseShapeTemplate); //Roughly explained as 'mfit guess of how waveform looks'
 tree->SetBranchAddress("chiSquare",          &chiSquare); //Chi squared of.. 
 tree->SetBranchAddress("amplitudeTruth",     &amplitudeTruth); //True amplitude of event
 tree->SetBranchAddress("pulse_shift",        &pulse_shift); 

 //std::ostringstream ss;
 //ss << pulse_shift;
 //std::string pulse_string(ss.str());

 //std::string s = boost::lexical_cast<std::string>(pulse_shift);
 tree->GetEntry(nEvent); //Choosing event number for branches

 //Checking values from branches
 cout << " nWF = " << nWF << endl;
 cout << " NFREQ = " << NFREQ << endl;
 cout << " chiSquare = " << chiSquare << endl;
 cout << " amplitudeTruth = " << amplitudeTruth << endl;
 cout << " pulse_shift = " << pulse_shift << endl;

 TTreeReader myReader("ntuple", 

 //Plotting the unsampled (raw) waveform
 TCanvas* ccwaveform = new TCanvas ("ccwaveform","1",800,600); //Name, Title, width and height
 TGraph *gr = new TGraph();
 for(int i=0; i<nWF; i++){ //nWF is time for entire waveform
  gr->SetPoint(i, i, pulse_signal->at(i)); //Create Data Points: (point i, x value, y value)
 }
 gr->Draw("AL"); //A=Axis, L=Line graph
 string graph_title = nameWF + " Waveform";
 char * graph_title_cst = graph_title.c_str(); //c_str() returns pointer, roughly meant to make data accessible 
 gr->SetTitle(graph_title_cst); 
 gr->SetLineColor(kMagenta);
 gr->SetLineWidth(2);
 gr->GetXaxis()->SetTitle("time [ns]");
 string png_name = "images/plotPulse/" + nameWF + "_raw.png";
 char * png_name_cst = png_name.c_str();
 ccwaveform->SaveAs(png_name_cst);

}

// include all necessary header files
#include <TH1.h>
#include <TRandom3.h>
#include <TMath.h>
#include <TFile.h>

void eta()
{
  // declare and define two histograms (their number of bins and boundaries)
  TH1F* h_eta = new TH1F("h_eta","",100,-5,5);
  TH1F* h_theta = new TH1F("h_theta","",100,0,TMath::Pi());
     
  // start producing distributions
  // set the number of events to be 10000
  const int neve=10000;
  TRandom3* myrndm = new TRandom3();

  for(unsigned int i=0; i<neve; i++){
    
   
    float eta = (myrndm->Rndm()*(10))-5;
    h_eta->Fill(eta);

    float theta= (TMath::ATan(TMath::Exp(-eta)))/0.5;
    h_theta->Fill(theta);
  }


  h_eta->Draw();
  h_theta->Draw();

  // save the histograms in a root file
  TFile* outFile = new TFile("eta_theta.root","recreate");
  
  h_theta->Write();
  h_eta->Write();
 
  outFile->Close();


}

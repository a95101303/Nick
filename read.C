#include <vector>
#include <iostream>
#include <TH1F.h>
#include <TFile.h>
#include "untuplizer.h"
#include <TCanvas.h>

using namespace std;
void read(std::string inputFile){

  // now we can perform the fit
  TFile *f1 = TFile::Open("electrons_250_GeV_5_7_X0.root");
  TH1F *f2 = (TH1F*)f1->Get("TimeCorrected_17_Amp_0");
  TCanvas* c1 = new TCanvas("c1");
  f2->Fit("gaus");
  gStyle->SetOptFit(111111);
  c1->Print("TimeCorrected_17_Amp_0+gaus.pdf");

}
~           

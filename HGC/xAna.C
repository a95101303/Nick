#include <vector>
#include <iostream>
#include <TH1F.h>
#include <TFile.h>
#include <TH1.h>
#include "untuplizer.h"
#include <TCanvas.h>
#include <TLatex.h>
#include <TRandom3.h>
#include <TF1.h>
using namespace std;

void xAna(std::string inputFile){

  // get the root file from .root and take the TH1F
  TFile *f1 = TFile::Open("electrons_250_GeV_5_7_X0.root");
  TH1F *h_tc17 = (TH1F*)f1->Get("TimeCorrected_17_Amp_0");
  TCanvas* c1 = new TCanvas("c1");
  h_tc17->GetYaxis()->SetTitle("#Entry");
  h_tc17->GetYaxis()->SetTitleSize(0.04);
  h_tc17->SetLineColor(96);
  h_tc17->GetYaxis()->CenterTitle();
  h_tc17->GetXaxis()->SetTitle("time");
  h_tc17->GetXaxis()->SetTitleSize(0.04);
  h_tc17->GetYaxis()->SetTitleOffset(1);
  h_tc17->SetLineWidth(2);
  
  //find Max x and Max y 
  float h_tmc,h_tmc1;
  h_tmc= h_tc17->GetBinContent(h_tc17->GetMaximumBin());
  
  int a=h_tc17->GetMaximumBin();
  h_tmc1 = h_tc17->GetXaxis()->GetBinCenter(a);

  //find the RMS
  float RMS;
  RMS=h_tc17->GetRMS();

  //find the std dev
  float RMSError;
  RMSError=h_tc17->GetRMSError();
     
  //Create the Random that fit with RMS*2 range
  TF1 *fitplot= new TF1 ("fitplot","gaus",-2*(RMS),2*(RMS));
  h_tc17->Fit("fitplot","R");
  //And also can be this:
  //h_tc17->Fit("gaus","","",-2*RMSError,2*RMSError);
  

  gStyle->SetOptFit(111111);
  c1->Print("TimeCorrected_17_Amp_0gaus.pdf");
  cout<<h_tmc<<endl;
  cout<<h_tmc1<<endl;   
  cout<<RMSError<<endl;
  cout<<RMS<<endl;
}


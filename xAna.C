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
#include <fstream>
#include <TStyle.h>
#include <TROOT.h>
#include <TLegend.h>
using namespace std;

void xAna(std::string inputFile){

  // get the root file from .root and take the TH1F
  TFile *f1 = TFile::Open("electrons_250_GeV_5_7_X0.root");
  TH1F *h_tc17 = (TH1F*)f1->Get("TimeCorrected_17_Amp_4");
  TCanvas* c1 = new TCanvas("c1");
  h_tc17->GetYaxis()->SetTitle("#Entry");
  h_tc17->GetYaxis()->SetTitleSize(0.04);
  h_tc17->SetLineColor(56);
  h_tc17->GetYaxis()->CenterTitle();
  h_tc17->GetXaxis()->SetTitle("time");
  h_tc17->GetXaxis()->SetTitleSize(0.04);
  h_tc17->GetYaxis()->SetTitleOffset(1);
  h_tc17->SetLineWidth(2);
  
  //find Max x and Max y 
  float h_tmc,h_tmc1,h_FWHM;
  h_tmc= h_tc17->GetBinContent(h_tc17->GetMaximumBin());
  h_FWHM= h_tmc/2;
  
  int a=h_tc17->GetMaximumBin();
  h_tmc1 = h_tc17->GetXaxis()->GetBinCenter(a);


  //find the RMS
  float RMS;
  //RMS=h_tc17->GetStdDev();
  //or can use 
  RMS=h_tc17->GetRMS();
  
  //find the std dev
  float RMSError;
  RMSError=h_tc17->GetStdDevError();
  //or can use RMSError=h_tc17->GetRMSError();
   
  //for FWHM
  float f,c,g,d;
  for(double i=0;i<=1000;i++){
    if(h_tc17->GetBinContent(i) < h_FWHM && h_FWHM < h_tc17->GetBinContent(i+1)){
    	f=h_tc17->GetXaxis()->GetBinCenter(i);
	c=h_tc17->GetXaxis()->GetBinCenter(i+1);
        cout<<(f+c)/2<<endl;
    }
    if(h_tc17->GetBinContent(i) > h_FWHM && h_FWHM > h_tc17->GetBinContent(i+1)){
    	g=h_tc17->GetXaxis()->GetBinCenter(i);
    	d=h_tc17->GetXaxis()->GetBinCenter(i+1);
        cout<<(g+d)/2;

    }
  }
  
  //Create the Random that fit with RMS*2 range
  TF1 *fitplot= new TF1 ("fitplot","gaus",(f+c)/2,(g+d)/2);
  //fitplot->GetStdDev()
  fitplot->SetLineColor(2);
  h_tc17->Fit("fitplot","R");
  //And also can be this:
  //h_tc17->Fit("gaus","","",-2*RMSError,2*RMSError);
  
  //Draw Legend
  TLegend* leg = new TLegend(0.1,0.7,0.38,0.9);
  leg->AddEntry(h_tc17,"time_correct17");
  leg->AddEntry(fitplot,"fitgausplot");
  leg->Draw();
  
  //Latex
  //TString a= "";
  //TString b= "";
  //TString c= "";
  //TLatex Tl; Tl.SetTextFont(72); Tl.SetTextSize(0.04); 
  //Tl.SetNDC(kTRUE); 
  //Tl.SetTextAlign(22);
  //Tl.DrawLatex(0.5,0.96,a);
  //Tl.DrawLatex(0.75,0.6,b);
  //Tl.DrawLatex(0.75, 0.53,c);


  //Set some parameter and print
  gStyle->SetOptFit(111111);
  c1->Print("TimeCorrected_17_Amp_0_FWHMgaus.pdf");
  cout<<h_tmc<<endl;
  cout<<h_FWHM<<endl;
  cout<<h_tmc1<<endl;   
  cout<<RMSError<<endl;
  cout<<RMS<<endl;

  //Set the text file
  ofstream fout3;
  fout3.open(("Parameter:2*RMS.txt"),ios::out| ios::app);
  //fout3 << "Histogramname" << " " << "mean" <<" "<< "rms"<<endl; 
  fout3 << "TimeCorrected_17_Amp_5"<< fitplot->GetParameter(1) << " " << RMS <<endl;
  fout3.close();
  
  

}

#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TBrowser.h"
#include "TH1.h"
#include "TH2.h"
void analysis1()
{
	TFile *f = new TFile("electrons_100_GeV_5_7_X0.root");
	TTree *t1=(TTree*)f->Get("t1065");


	//create the histogram that we want to see
	float gauspeak[36];
	t1->SetBranchAddress("gauspeak",&gauspeak[36]);
	
	//h_photek_time,h_int[17]-> TH1F histogram
	TH1F *h_photek_time = new TH1F("h_tphotek_time","photek time",1000,-100,100);
	h_photek_time->SetXTitle("x");
	h_photek_time->SetYTitle("time");
	TCanvas* c1= new TCanvas("c1");
     		
	//Long64_t nentries =t1 ->GetEntries();
	//for(Long64_t i=0;i<nentries;i++) {
	//	t1->GetEntry(i);
		h_photek_time->Fill(gauspeak[16]);
     		h_photek_time->SetLineColor(2);
	

	//set in pdf and print
	c1->Print("photek_time_plot.pdf");
}

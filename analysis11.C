#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include <TBrowser.h>
#include <TH1.h>
#include <TH2.h>
#include <TH2F.h>
#include <TCanvas.h>
#include <iostream>
#include <TList.h>
#include <TBranch.h>
#include "untuplizer.h"

using namespace std;
void analysis11(std::string inputFile)
{
	
	TreeReader data(inputFile.data(),"t1065");
	
	//TFile *f1 = TFile::Open("electrons_100_GeV_5_7_X0.root");
        //TTree *t1=(TTree*)f1->Get("t1065");
	
	float *gauspeak;
        float *amp;

	TH2F *h_photek_time_amp = new TH2F("h_photek_time_amp","photek time amp",100,22,40,100,0,0.2);

        h_photek_time_amp->SetXTitle("time");
        h_photek_time_amp->SetYTitle("amp");
	TCanvas* c1 = new TCanvas("c1","c1",900,700);
	
	for(Long64_t jEntry=0; jEntry<data.GetEntriesFast() ;jEntry++){

    	if (jEntry % 10000 == 0)
     	 	fprintf(stderr, "Processing event %lli of %lli\n", jEntry + 1, data.GetEntriesFast());			data.GetEntry(jEntry);

    	*gauspeak = data.GetLong64("gauspeak");
	*amp= data.GetLong64("amp");
	h_photek_time_amp->Fill(gauspeak[16],amp[16]);
}
	

	h_photek_time_amp->SetFillColor(3);
	h_photek_time_amp->Draw("textcolz");
	c1->Print("photek_time_amp_plot17.pdf");
	
	TFile* outFile = new TFile("analysis1.root","recreate");
        c1->Write();
        outFile->Close();
}

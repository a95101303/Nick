#include "TROOT.h"
#include "TFile.h"
#include "TTree.h"
#include "TBrowser.h"
#include "TH1.h"
#include "TH2.h"
#include "TH2F.h"
#include "TCanvas.h"
#include "iostream"

using namespace std;
void analysis1()
{
	TFile *f1 = TFile::Open("electrons_100_GeV_5_7_X0.root");
	TTree *t1=(TTree*)f1->Get("t1065");


	//create the histogram that we want to see
	float *gauspeak;
	float *amp;
	t1->SetBranchAddress("gauspeak",gauspeak);
	t1->SetBranchAddress("amp",amp);
	cout << gauspeak[16] << "\t" << amp[16] << endl;

	cout << "ede" << endl;		
	//h_photek_time-> TH1F histogram
	TCanvas* c1 = new TCanvas("c1","c1",900,700);
	//TH1F *h_photek_time = new TH1F("h_tphotek_time","photek time",1000,22,40);
	//h_photek_time->SetXTitle("x");
	//h_photek_time->SetYTitle("time");
     		
	//h_photek_amp->TH1F histogram
	//TH1F *h_photek_amp = new TH1F("h_tphotek_amp","photek amp",1000,0,0.2);
        //h_photek_amp->SetXTitle("x");
        //h_photek_amp->SetYTitle("amp");
        //TCanvas* c2= new TCanvas("c2");

	//h_photek_time_amp->TH2F histogram

	TH2F *h_photek_time_amp = new TH2F("h_photek_time_amp","photek time amp",100,22,40,100,0,0.2);
	
	h_photek_time_amp->SetXTitle("time");
	h_photek_time_amp->SetYTitle("amp");
	//TCanvas* c4= new TCanvas("c4");

	
	//Event loop
	int nentries =t1->GetEntries();
	//for(int i=0;i<100;i++) {
	for(int i=0;i<nentries;i++) {
		t1->GetEntry(i);
		cout << gauspeak[16] << "\t" << amp[16] << endl;
		//h_photek_time->Fill(gauspeak[16]);
		//h_photek_amp->Fill(amp[16]);
		h_photek_time_amp->Fill(gauspeak[16],amp[16]);
	}
	cout << "end" << endl;
	//h_photek_time->SetLineColor(2);
	h_photek_time_amp->SetFillColor(3);
	
	//set in pdf and print
	
	cout << "draw" << endl;
	//h_photek_time->Draw("hist");
	h_photek_time_amp->Draw("textcolz");
	cout << "print" << endl;
	//c1->Print("photek_time_plot17.pdf");
	cout << "00000000" << endl;
	
	//c2->Print("photek_amp_plot17.pdf");
	c1->Print("photek_time_amp_plot17.pdf");
	cout << "savingfig" << endl;
	//set the rootfile
	
	
	TFile* outFile = new TFile("analysis1.root","recreate");
	c1->Write();
	//h_photek_time->Write();
	//h_photek_amp->Write();
	//h_photek_time_amp->Write();
	outFile->Close();
	cout << "writing"<< endl;
	
}

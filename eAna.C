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
void eAna(std::string inputFileName){
  
 auto c = new TCanvas();c->SetGrid();
 TGraphErrors graph("Parameter2RMS.txt","%lg %lg","\t,;");
 graph.SetTitle(
  "Time_corrected_17;"
  "Time_corrected_17_x;"
  "Mean_y");
graph.SetMarkerStyle(kCircle);
graph.SetFillColor(kYellow);
graph.DrawClone("E3AL");// E3 draws the band


//Draw the Legend
TLegend leg(.1,.7,.3,.9,"Time_corrected_17");
//leg.SetFillColor(0);
//leg.AddEntry(&graph,"Expected Points");
leg.AddEntry(&graph,"Measured Points");
leg.DrawClone("Same");
graph.Print();
c->Print("Tgraph.pdf");
}
  



 

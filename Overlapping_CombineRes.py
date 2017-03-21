# In this at the end of filevector I am putting the dirname
# so loop over n-1 files and n will give the name of the output dir.

# In legend also the n element will give the name for the ratio plot y axis label.
#edited by Monika Mittal 
#Script for ratio plot 
#import sys
#sys.argv.append( '-b-' )
import ROOT
ROOT.gROOT.SetBatch(True)

#import ROOT
from ROOT import TFile, TH1F, gDirectory, TCanvas, TPad, TProfile,TGraph, TGraphAsymmErrors
from ROOT import TH1D, TH1, TH1I
from ROOT import gStyle
from ROOT import gROOT
from ROOT import TStyle
from ROOT import TLegend
from ROOT import TMath
from ROOT import TPaveText
from ROOT import TLatex

import os
colors=[5,1,4,3,32,20,6,2,20,11,41,46,30,12,28,20,32]
markerStyle=[23,21,22,20,24,25,26,27,28,29,20,21,22,23]            
linestyle=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def DrawOverlap(fileVec, histVec, titleVec,legendtext,pngname,logstatus=[0,0],xRange=[-99999,99999,1]):

    gStyle.SetOptTitle(0)
    gStyle.SetOptStat(0)
    gStyle.SetTitleOffset(1.1,"Y");#the distance between axis and axis/default=x
    gStyle.SetTitleOffset(0.9,"X");
    gStyle.SetLineWidth(3)
    gStyle.SetFrameLineWidth(3); 

    i=0

    histList_=[]#set four array
    histList=[]
    histList1=[]
    maximum=[]
    
    ## Legend    #the line legend
    leg = TLegend(0.4, 0.70, 0.939, 0.89)#,NULL,"brNDC");
    leg.SetBorderSize(0)
    leg.SetNColumns(2)
    leg.SetLineColor(1)
    leg.SetLineStyle(1)
    leg.SetLineWidth(1)
    leg.SetFillColor(0)
    leg.SetFillStyle(0)
    leg.SetTextFont(22)
    leg.SetTextSize(0.045)
     
    c = TCanvas("c1", "c1",0,0,500,500)
    #c.SetBottomMargin(0.15)
    #c.SetLeftMargin(0.15)
    #c.SetLogy(0)
    #c.SetLogx(0)
    c1_2 = TPad("c1_2","newpad",0.04,0.05,1,0.994)#What is used to?
    c1_2.Draw()

    
    print ("you have provided "+str(len(fileVec))+" files and "+str(len(histVec))+" histograms to make a overlapping plot" )
    print "opening rootfiles"
    c.cd()
    #c1_2.SetBottomMargin(0.13)
    c1_2.SetLogy(logstatus[1])#what is logstatus[1]?
    c1_2.SetLogx(logstatus[0])
    
    
    c1_2.cd()
    ii=0    
    inputfile={}
    print str(fileVec[(len(fileVec)-1)])#print the last one

    for ifile_ in range(len(fileVec)):
        print ("opening file  "+fileVec[ifile_])
        inputfile[ifile_] = TFile( fileVec[ifile_] )
        print "fetching histograms"
        for ihisto_ in range(len(histVec)):
            print ("printing histo "+str(histVec[ihisto_]))
            histo = inputfile[ifile_].Get(histVec[ihisto_])
            #status_ = type(histo) is TGraphAsymmErrors
            histList.append(histo)
            # for ratio plot as they should nt be normalize 
            histList1.append(histo)
            print histList[ii].Integral()
            #histList[ii].Rebin(xRange[2])
            type_obj = type(histList[ii])
            if (type_obj is TH1D) or (type_obj is TH1F) or (type_obj is TH1) or (type_obj is TH1I) :
                histList[ii].Rebin(1)#why we use this?I think this is uneffect?
                histList[ii].Scale(1.0/histList[ii].Integral())#i don't know what's this?
                maximum.append(histList[ii].GetMaximum())
                maximum.sort()
            ii=ii+1

    print histList
    for ih in range(len(histList)):
        tt = type(histList[ih])
#        print "graph_status =" ,(tt is TGraphAsymmErrors)
#        print "hist status =", (tt is TH1D) or (tt is TH1F)
        if ih == 0 :      
            if (tt is TGraphAsymmErrors) | (tt is TGraph) : 
                histList[ih].Draw("A3P")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw("HIST")   
        if ih > 0 :
            #histList[ih].SetLineWidth(2)
            if (tt is TGraphAsymmErrors) | (tt is TGraph) : 
                histList[ih].Draw("3P same")
            if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
                histList[ih].Draw("HISTsame")   

        if (tt is TGraphAsymmErrors) | (tt is TGraph) :
           # histList[ih].SetMaximum(0.06) 
           # histList[ih].SetMinimum(0.02) 

            histList[ih].SetMaximum(maximum+0.3)#is this Maximum is the plot maximum+0.3?
            histList[ih].SetMinimum(0)#is this the y-axis minimum 0?
            histList[ih].SetMarkerColor(colors[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(3)
            histList[ih].SetLineStyle(linestyle[ih])
            
            histList[ih].SetMarkerStyle(markerStyle[ih])
            histList[ih].SetMarkerSize(1)
            leg.AddEntry(histList[ih],legendtext[ih],"P")
        if (tt is TH1D) or (tt is TH1F) or (tt is TH1) or (tt is TH1I) :
            histList[ih].SetLineStyle(linestyle[ih])
            histList[ih].SetLineColor(colors[ih])
            histList[ih].SetLineWidth(3)
            histList[ih].SetMaximum(maximum[0]+0.3) 
            histList[ih].SetMinimum(0) 
            leg.AddEntry(histList[ih],legendtext[ih],"L")
        histList[ih].GetYaxis().SetTitle(titleVec[1])
        histList[ih].GetYaxis().SetTitleSize(0.045)
        histList[ih].GetYaxis().SetTitleOffset(1.1000998)
        histList[ih].GetYaxis().SetTitleFont(22)
        histList[ih].GetYaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelSize(.045)
        histList[ih].GetXaxis().SetRangeUser(xRange[0],xRange[1])
        histList[ih].GetXaxis().SetLabelSize(0.0000);
        histList[ih].GetXaxis().SetTitle(titleVec[0])
        histList[ih].GetXaxis().SetLabelSize(0.052)
        histList[ih].GetXaxis().SetTitleSize(0.052)
        histList[ih].GetXaxis().SetTitleOffset(1.04)
        histList[ih].GetXaxis().SetTitleFont(22)
        histList[ih].GetXaxis().SetTickLength(0.07)
        histList[ih].GetXaxis().SetLabelFont(22)
        histList[ih].GetYaxis().SetLabelFont(22) 
# histList[ih].GetXaxis().SetNdivisions(508)
#

        i=i+1
    pt = TPaveText(0.0877181,0.9,0.9580537,0.96,"brNDC")#no default,NDC is ourself set.
    pt.SetBorderSize(0)
    pt.SetTextAlign(12)
    pt.SetFillStyle(0)
    pt.SetTextFont(22)
    pt.SetTextSize(0.046)
    text = pt.AddText(0.05,0.5,"CMS Preliminary")
    #text = pt.AddText(0.5,0.5,"12.9 fb^{-1} (13 TeV)")
#    text = pt.AddText(0.8,0.5," (13 TeV)")
 #   text = pt.AddText(0.65,0.5," AK8")
    pt.Draw()
   
    

#    t2a = TPaveText(0.0877181,0.81,0.9580537,0.89,"brNDC")
#    t2a.SetBorderSize(0)
#    t2a.SetFillStyle(0)
#    t2a.SetTextSize(0.040) 
#    t2a.SetTextAlign(12)
#    t2a.SetTextFont(62)
#    histolabel1= str(fileVec[(len(fileVec)-1)])
#    text1 = t2a.AddText(0.06,0.5,"CMS Internal") 
#    t2a.Draw()
    leg.Draw()
#
#    c.cd()
    outputdirname = 'HGCAL/'
    histname=outputdirname+pngname 
    c.SaveAs(histname+'.png')
    c.SaveAs(histname+'.pdf')
#    outputname = 'cp  -r '+ outputdirname +' /afs/hep.wisc.edu/home/khurana/public_html/'
#    os.system(outputname) 



print "calling the plotter"
files=['histogramsRootFile/electrons_20_GeV_5_7_X0.root','histogramsRootFile/electrons_32_GeV_5_7_X0.root','histogramsRootFile/electrons_50_GeV_5_7_X0.root','histogramsRootFile/electrons_100_GeV_5_7_X0.root','histogramsRootFile/electrons_150_GeV_5_7_X0.root','histogramsRootFile/electrons_200_GeV_5_7_X0.root','histogramsRootFile/electrons_250_GeV_5_7_X0.root']
legend=['20','32','50','100', '150', '200', '250' ]
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_0'],["# Pads","# entries"],legend,'CombineRes_NPad_0',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_5'],["# Pads","# entries"],legend,'CombineRes_NPad_5',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_10'],["# Pads","# entries"],legend,'CombineRes_NPad_10',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_15'],["# Pads","# entries"],legend,'CombineRes_NPad_15',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_25'],["# Pads","# entries"],legend,'CombineRes_NPad_25',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_75'],["# Pads","# entries"],legend,'CombineRes_NPad_75',[0,0],[1,10]) 


files=['histogramsRootFile/electrons_20_GeV_10_X0.root','histogramsRootFile/electrons_32_GeV_10_X0.root','histogramsRootFile/electrons_50_GeV_10_X0.root','histogramsRootFile/electrons_100_GeV_10_X0.root','histogramsRootFile/electrons_150_GeV_10_X0.root','histogramsRootFile/electrons_200_GeV_10_X0.root','histogramsRootFile/electrons_250_GeV_10_X0.root']
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_0'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_0',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_5'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_5',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_10'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_10',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_15'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_15',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_25'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_25',[0,0],[1,10]) 
DrawOverlap(files,['h_NPads_Amp_0_AmpTh_75'],["# Pads","# entries"],legend,'CombineRes_NPad_10Xo_75',[0,0],[1,10]) 

Plotname =['h_NPads_Amp_0_AmpTh_0','h_NPads_Amp_0_AmpTh_5','h_NPads_Amp_0_AmpTh_15','h_NPads_Amp_0_AmpTh_25','h_NPads_Amp_0_AmpTh_50']
legend1 =['0','5','15','25','50']
DrawOverlap(['histogramsRootFile/electrons_100_GeV_5_7_X0.root'],Plotname,["# Pads","# entries"],legend1,'CombineRes_NPad_Energy100',[0,0],[1,10])
DrawOverlap(['histogramsRootFile/electrons_200_GeV_5_7_X0.root'],Plotname,["# Pads","# entries"],legend1,'CombineRes_NPad_Energy200',[0,0],[1,10])

DrawOverlap(['histogramsRootFile/electrons_100_GeV_10_X0.root'],Plotname,["# Pads","# entries"],legend1,'CombineRes_NPad_Energy100_10Xo_',[0,0],[1,10])
DrawOverlap(['histogramsRootFile/electrons_200_GeV_10_X0.root'],Plotname,["# Pads","# entries"],legend1,'CombineRes_NPad_Energy200_10Xo_',[0,0],[1,10])

#DrawOverlap(filesname_1,['MeanValue_18'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_18',[0,0],) 
#DrawOverlap(filesname_1,['MeanValue_19'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_19',[0,0],) 
#DrawOverlap(filesname_1,['MeanValue_20'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_20',[0,0],) 
#DrawOverlap(filesname_1,['MeanValue_21'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_21',[0,0],) 
#DrawOverlap(filesname_1,['MeanValue_22'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_22',[0,0],) 
#DrawOverlap(filesname_1,['MeanValue_23'],["Amplitude","Offset"],legend_1,'Timewalk_Extracter_23',[0,0],) 

#############Plot type ###############

#legend2=['17','18','19','20','21','22','23','Combo'] 
#plotname =['Resolution_cell_17_amp_0','Resolution_cell_18_amp_0','Resolution_cell_19_amp_0','Resolution_cell_20_amp_0','Resolution_cell_21_amp_0','Resolution_cell_22_amp_0','Resolution_cell_23_amp_0','Resolution_cell_100_amp_0']
#plotname1 =['Resolution_cell_17_amp_1','Resolution_cell_18_amp_1','Resolution_cell_19_amp_1','Resolution_cell_20_amp_1','Resolution_cell_21_amp_1','Resolution_cell_22_amp_1','Resolution_cell_23_amp_1','Resolution_cell_100_amp_1']
#plotname2 =['Resolution_cell_17_amp_2','Resolution_cell_18_amp_2','Resolution_cell_19_amp_2','Resolution_cell_20_amp_2','Resolution_cell_21_amp_2','Resolution_cell_22_amp_2','Resolution_cell_23_amp_2','Resolution_cell_100_amp_2']
#plotname3 =['Resolution_cell_17_amp_3','Resolution_cell_18_amp_3','Resolution_cell_19_amp_3','Resolution_cell_20_amp_3','Resolution_cell_21_amp_3','Resolution_cell_22_amp_3','Resolution_cell_23_amp_3','Resolution_cell_100_amp_3']
#plotname4 =['Resolution_cell_17_amp_4','Resolution_cell_18_amp_4','Resolution_cell_19_amp_4','Resolution_cell_20_amp_4','Resolution_cell_21_amp_4','Resolution_cell_22_amp_4','Resolution_cell_23_amp_4','Resolution_cell_100_amp_4']


#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname,["E_{beam}[GeV]","Resolution"],legend2,'ResolutionVsenergy_amp0',[0,0],)
#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname1,["E_{beam}[GeV]","Resolution"],legend2,'ResolutionVsenergy_amp1',[0,0],)
#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname2,["E_{beam}[GeV]","Resolution"],legend2,'ResolutionVsenergy_amp2',[0,0],)
#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname3,["E_{beam}[GeV]","Resolution"],legend2,'ResolutionVsenergy_amp3',[0,0],)
#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname4,["E_{beam}[GeV]","Resolution"],legend2,'ResolutionVsenergy_amp4',[0,0],)

#plotname5 =['Resolution_cell_17_amp_1','Resolution_cell_18_amp_1','Resolution_cell_19_amp_1','Resolution_cell_20_amp_1','Resolution_cell_21_amp_1','Resolution_cell_22_amp_1','Resolution_cell_23_amp_1']
#legend3=['17','18','19','20','21','22','23']
#DrawOverlap(['OutputrootFileResolution_withamplitude.root'],plotname5,["E_{beam}[GeV]","Resolution"],legend3,'ResolutionVsenergy_amp1_withoutcombo',[0,0],)

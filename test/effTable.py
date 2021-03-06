import sys
import os
import subprocess
from array import array
from ROOT import TH1D,TH2D,TFile,TMath,TCanvas,THStack,TLegend,TPave,TLine,TLatex,TPaveText
from ROOT import gROOT,gStyle,gPad,gStyle
from ROOT import Double,kBlue,kRed,kOrange,kMagenta,kYellow,kCyan,kGreen,kGray,kBlack,kTRUE

gROOT.Macro("~/rootlogon.C")
gStyle.SetOptStat(0)
#gROOT.SetBatch()
gROOT.SetStyle("Plain")
gStyle.SetOptStat()
gStyle.SetOptTitle(0)
gStyle.SetPalette(1)
gStyle.SetNdivisions(405,"x");
gStyle.SetEndErrorSize(0.)
gStyle.SetErrorX(0.1000)
gStyle.SetPadTickX(1)
gStyle.SetPadTickY(1)

from optparse import OptionParser
parser = OptionParser()
parser.add_option('--plotDir', metavar='P', type='string', action='store',
                  default='Summer2018Plots',
                  dest='plotDir',
                  help='output directory of plots')
(options,args) = parser.parse_args()

outDir = options.plotDir

execfile("input.py")

c1 = TCanvas('c1', 'c1', 1800, 1000)
pt1 = TPaveText(.05,.05,.15,.95)
pt2 = TPaveText(0.15, 0.05, 0.23, 0.95)
pt3 = TPaveText(0.23, 0.05, 0.31, 0.95)
pt4 = TPaveText(0.31, 0.05, 0.39, 0.95)
pt5 = TPaveText(0.39, 0.05, 0.47, 0.95)
pt6 = TPaveText(0.47, 0.05, 0.55, 0.95)
pt7 = TPaveText(0.55, 0.05, 0.63, 0.95)
pt8 = TPaveText(0.63, 0.05, 0.71, 0.95)
pt9 = TPaveText(0.71, 0.05, 0.79, 0.95)
pt10 = TPaveText(0.79, 0.05, 0.87, 0.95)
pt11 = TPaveText(0.87, 0.05, 0.95, 0.95)

pt1.AddText("Sample")
pt1.AddLine(0.0, 0.1, 1.0, 0.1)
pt1.AddText("DYToLL")
pt1.AddLine(0.0, 0.2, 1.00, .200)
pt1.AddText("SingleT")
pt1.AddLine(0.0, .3, 1.00, .300)
pt1.AddText("TTbar")
pt1.AddLine(0.0, .4, 1.00, .400)
pt1.AddText("WJets")
pt1.AddLine(0.0, .5, 1.00, .5)
pt1.AddText("T_M1000_W10")
pt1.AddLine(0.0, .6, 1.00, .6)
pt1.AddText("T_M1500_W10")
pt1.AddLine(0.0, .7, 1.00, .7)
pt1.AddText("T_M2000_W10")
pt1.AddLine(0.0, .8, 1.00, .8)
pt1.AddText("T_M2500_W10")
pt1.AddLine(0.0, .9, 1.00, .9)
pt1.AddText("T_M3000_W10")
pt1.Draw()

pt2.AddText("Preselection")
pt2.AddLine(00, .100, 1.00, .100)
pt2.AddText(str(round(DYToLLnums[1]/DYToLLnums[1],3)))
pt2.AddLine(00, .200, 1.00, .200)
pt2.AddText(str(round(stnums[1]/stnums[1],3)))
pt2.AddLine(00, .300, 1.00, .300)
pt2.AddText(str(round(tt_M2T4nums[1]/tt_M2T4nums[1],3)))
pt2.AddLine(00, .400, 1.00, .400)
pt2.AddText(str(round(WToLNunums[1]/WToLNunums[1],3)))
pt2.AddLine(00, .500, 1.00, .500)
pt2.AddText(str(round(T_M1000_W10nums[1]/T_M1000_W10nums[1],3)))
pt2.AddLine(00, .600, 1.00, .600)
pt2.AddText(str(round(T_M1500_W10nums[1]/T_M1500_W10nums[1],3)))
pt2.AddLine(00, .700, 1.00, .700)
pt2.AddText(str(round(T_M2000_W10nums[1]/T_M2000_W10nums[1],3)))
pt2.AddLine(00, .800, 1.00, .800)
pt2.AddText(str(round(T_M2500_W10nums[1]/T_M2500_W10nums[1],3)))
pt2.AddLine(00, .900, 1.00, .900)
pt2.AddText(str(round(T_M3000_W10nums[1]/T_M3000_W10nums[1],3)))
pt2.Draw()

pt3.AddText("Exactly 1 Lepton")
pt3.AddLine(00, .100, 1.00, .100)
pt3.AddText(str(round(DYToLLnums[2]/DYToLLnums[1],3)))
pt3.AddLine(00, .200, 1.00, .200)
pt3.AddText(str(round(stnums[2]/stnums[1],3)))
pt3.AddLine(00, .300, 1.00, .300)
pt3.AddText(str(round(tt_M2T4nums[2]/tt_M2T4nums[1],3)))
pt3.AddLine(00, .400, 1.00, .400)
pt3.AddText(str(round(WToLNunums[2]/WToLNunums[1],3)))
pt3.AddLine(00, .500, 1.00, .500)
pt3.AddText(str(round(T_M1000_W10nums[2]/T_M1000_W10nums[1],3)))
pt3.AddLine(00, .600, 1.00, .600)
pt3.AddText(str(round(T_M1500_W10nums[2]/T_M1500_W10nums[1],3)))
pt3.AddLine(00, .700, 1.00, .700)
pt3.AddText(str(round(T_M2000_W10nums[2]/T_M2000_W10nums[1],3)))
pt3.AddLine(00, .800, 1.00, .800)
pt3.AddText(str(round(T_M2500_W10nums[2]/T_M2500_W10nums[1],3)))
pt3.AddLine(00, .900, 1.00, .900)
pt3.AddText(str(round(T_M3000_W10nums[2]/T_M3000_W10nums[1],3)))
pt3.Draw()

pt4.AddText("2D Lepton Isolation")
pt4.AddLine(00, .100, 1.00, .100)
pt4.AddText(str(round(DYToLLnums[3]/DYToLLnums[2],3)))
pt4.AddLine(00, .200, 1.00, .200)
pt4.AddText(str(round(stnums[3]/stnums[2],3)))
pt4.AddLine(00, .300, 1.00, .300)
pt4.AddText(str(round(tt_M2T4nums[3]/tt_M2T4nums[2],3)))
pt4.AddLine(00, .400, 1.00, .400)
pt4.AddText(str(round(WToLNunums[3]/WToLNunums[2],3)))
pt4.AddLine(00, .500, 1.00, .500)
pt4.AddText(str(round(T_M1000_W10nums[3]/T_M1000_W10nums[2],3)))
pt4.AddLine(00, .600, 1.00, .600)
pt4.AddText(str(round(T_M1500_W10nums[3]/T_M1500_W10nums[2],3)))
pt4.AddLine(00, .700, 1.00, .700)
pt4.AddText(str(round(T_M2000_W10nums[3]/T_M2000_W10nums[2],3)))
pt4.AddLine(00, .800, 1.00, .800)
pt4.AddText(str(round(T_M2500_W10nums[3]/T_M2500_W10nums[2],3)))
pt4.AddLine(00, .900, 1.00, .900)
pt4.AddText(str(round(T_M3000_W10nums[3]/T_M3000_W10nums[2],3)))
pt4.Draw()

pt5.AddText("3 or More Central Jets")
pt5.AddLine(00, .100, 1.00, .100)
pt5.AddText(str(round(DYToLLnums[4]/DYToLLnums[3],3)))
pt5.AddLine(00, .200, 1.00, .200)
pt5.AddText(str(round(stnums[4]/stnums[3],3)))
pt5.AddLine(00, .300, 1.00, .300)
pt5.AddText(str(round(tt_M2T4nums[4]/tt_M2T4nums[3],3)))
pt5.AddLine(00, .400, 1.00, .400)
pt5.AddText(str(round(WToLNunums[4]/WToLNunums[3],3)))
pt5.AddLine(00, .500, 1.00, .500)
pt5.AddText(str(round(T_M1000_W10nums[4]/T_M1000_W10nums[3],3)))
pt5.AddLine(00, .600, 1.00, .600)
pt5.AddText(str(round(T_M1500_W10nums[4]/T_M1500_W10nums[3],3)))
pt5.AddLine(00, .700, 1.00, .700)
pt5.AddText(str(round(T_M2000_W10nums[4]/T_M2000_W10nums[3],3)))
pt5.AddLine(00, .800, 1.00, .800)
pt5.AddText(str(round(T_M2500_W10nums[4]/T_M2500_W10nums[3],3)))
pt5.AddLine(00, .900, 1.00, .900)
pt5.AddText(str(round(T_M3000_W10nums[4]/T_M3000_W10nums[3],3)))
pt5.Draw()

pt6.AddText("1 or More Forward Jets")
pt6.AddLine(00, .100, 1.00, .100)
pt6.AddText(str(round(DYToLLnums[5]/DYToLLnums[4],3)))
pt6.AddLine(00, .200, 1.00, .200)
pt6.AddText(str(round(stnums[5]/stnums[4],3)))
pt6.AddLine(00, .300, 1.00, .300)
pt6.AddText(str(round(tt_M2T4nums[5]/tt_M2T4nums[4],3)))
pt6.AddLine(00, .400, 1.00, .400)
pt6.AddText(str(round(WToLNunums[5]/WToLNunums[4],3)))
pt6.AddLine(00, .500, 1.00, .500)
pt6.AddText(str(round(T_M1000_W10nums[5]/T_M1000_W10nums[4],3)))
pt6.AddLine(00, .600, 1.00, .600)
pt6.AddText(str(round(T_M1500_W10nums[5]/T_M1500_W10nums[4],3)))
pt6.AddLine(00, .700, 1.00, .700)
pt6.AddText(str(round(T_M2000_W10nums[5]/T_M2000_W10nums[4],3)))
pt6.AddLine(00, .800, 1.00, .800)
pt6.AddText(str(round(T_M2500_W10nums[5]/T_M2500_W10nums[4],3)))
pt6.AddLine(00, .900, 1.00, .900)
pt6.AddText(str(round(T_M3000_W10nums[5]/T_M3000_W10nums[4],3)))
pt6.Draw()

pt7.AddText("Leading Jet Pt #geq 200 GeV")
pt7.AddLine(00, .100, 1.00, .100)
pt7.AddText(str(round(DYToLLnums[6]/DYToLLnums[5],3)))
pt7.AddLine(00, .200, 1.00, .200)
pt7.AddText(str(round(stnums[6]/stnums[5],3)))
pt7.AddLine(00, .300, 1.00, .300)
pt7.AddText(str(round(tt_M2T4nums[6]/tt_M2T4nums[5],3)))
pt7.AddLine(00, .400, 1.00, .400)
pt7.AddText(str(round(WToLNunums[6]/WToLNunums[5],3)))
pt7.AddLine(00, .500, 1.00, .500)
pt7.AddText(str(round(T_M1000_W10nums[6]/T_M1000_W10nums[5],3)))
pt7.AddLine(00, .600, 1.00, .600)
pt7.AddText(str(round(T_M1500_W10nums[6]/T_M1500_W10nums[5],3)))
pt7.AddLine(00, .700, 1.00, .700)
pt7.AddText(str(round(T_M2000_W10nums[6]/T_M2000_W10nums[5],3)))
pt7.AddLine(00, .800, 1.00, .800)
pt7.AddText(str(round(T_M2500_W10nums[6]/T_M2500_W10nums[5],3)))
pt7.AddLine(00, .900, 1.00, .900)
pt7.AddText(str(round(T_M3000_W10nums[6]/T_M3000_W10nums[5],3)))
pt7.Draw()

pt8.AddText("2nd Leading Jet Pt #geq 80 GeV")
pt8.AddLine(00, .100, 1.00, .100)
pt8.AddText(str(round(DYToLLnums[7]/DYToLLnums[6],3)))
pt8.AddLine(00, .200, 1.00, .200)
pt8.AddText(str(round(stnums[7]/stnums[6],3)))
pt8.AddLine(00, .300, 1.00, .300)
pt8.AddText(str(round(tt_M2T4nums[7]/tt_M2T4nums[6],3)))
pt8.AddLine(00, .400, 1.00, .400)
pt8.AddText(str(round(WToLNunums[7]/WToLNunums[6],3)))
pt8.AddLine(00, .500, 1.00, .500)
pt8.AddText(str(round(T_M1000_W10nums[7]/T_M1000_W10nums[6],3)))
pt8.AddLine(00, .600, 1.00, .600)
pt8.AddText(str(round(T_M1500_W10nums[7]/T_M1500_W10nums[6],3)))
pt8.AddLine(00, .700, 1.00, .700)
pt8.AddText(str(round(T_M2000_W10nums[7]/T_M2000_W10nums[6],3)))
pt8.AddLine(00, .800, 1.00, .800)
pt8.AddText(str(round(T_M2500_W10nums[7]/T_M2500_W10nums[6],3)))
pt8.AddLine(00, .900, 1.00, .900)
pt8.AddText(str(round(T_M3000_W10nums[7]/T_M3000_W10nums[6],3)))
pt8.Draw()

pt9.AddText("1 or More B-Jet")
pt9.AddLine(00, .100, 1.00, .100)
pt9.AddText(str(round(DYToLLnums[8]/DYToLLnums[7],3)))
pt9.AddLine(00, .200, 1.00, .200)
pt9.AddText(str(round(stnums[8]/stnums[7],3)))
pt9.AddLine(00, .300, 1.00, .300)
pt9.AddText(str(round(tt_M2T4nums[8]/tt_M2T4nums[7],3)))
pt9.AddLine(00, .400, 1.00, .400)
pt9.AddText(str(round(WToLNunums[8]/WToLNunums[7],3)))
pt9.AddLine(00, .500, 1.00, .500)
pt9.AddText(str(round(T_M1000_W10nums[8]/T_M1000_W10nums[7],3)))
pt9.AddLine(00, .600, 1.00, .600)
pt9.AddText(str(round(T_M1500_W10nums[8]/T_M1500_W10nums[7],3)))
pt9.AddLine(00, .700, 1.00, .700)
pt9.AddText(str(round(T_M2000_W10nums[8]/T_M2000_W10nums[7],3)))
pt9.AddLine(00, .800, 1.00, .800)
pt9.AddText(str(round(T_M2500_W10nums[8]/T_M2500_W10nums[7],3)))
pt9.AddLine(00, .900, 1.00, .900)
pt9.AddText(str(round(T_M3000_W10nums[8]/T_M3000_W10nums[7],3)))
pt9.Draw()

pt10.AddText("Missing E_{t} #geq 20 GeV")
pt10.AddLine(00, .100, 1.000, .100)
pt10.AddText(str(round(DYToLLnums[9]/DYToLLnums[8],3)))
pt10.AddLine(00, .200, 1.000, .200)
pt10.AddText(str(round(stnums[9]/stnums[8],3)))
pt10.AddLine(00, .300, 1.000, .300)
pt10.AddText(str(round(tt_M2T4nums[9]/tt_M2T4nums[8],3)))
pt10.AddLine(00, .400, 1.000, .400)
pt10.AddText(str(round(WToLNunums[9]/WToLNunums[8],3)))
pt10.AddLine(00, .500, 1.000, .500)
pt10.AddText(str(round(T_M1000_W10nums[9]/T_M1000_W10nums[8],3)))
pt10.AddLine(00, .600, 1.000, .600)
pt10.AddText(str(round(T_M1500_W10nums[9]/T_M1500_W10nums[8],3)))
pt10.AddLine(00, .700, 1.000, .700)
pt10.AddText(str(round(T_M2000_W10nums[9]/T_M2000_W10nums[8],3)))
pt10.AddLine(00, .800, 1.000, .800)
pt10.AddText(str(round(T_M2500_W10nums[9]/T_M2500_W10nums[8],3)))
pt10.AddLine(00, .900, 1.000, .900)
pt10.AddText(str(round(T_M3000_W10nums[9]/T_M3000_W10nums[8],3)))
pt10.Draw()

pt11.AddText("1 or More Higgs")
pt11.AddLine(000, .100, 1.00, .100)
pt11.AddText(str(round(DYToLLnums[10]/DYToLLnums[9],3)))
pt11.AddLine(000, .200, 1.00, .200)
pt11.AddText(str(round(stnums[10]/stnums[9],3)))
pt11.AddLine(000, .300, 1.00, .300)
pt11.AddText(str(round(tt_M2T4nums[10]/tt_M2T4nums[9],3)))
pt11.AddLine(000, .400, 1.00, .400)
pt11.AddText(str(round(WToLNunums[10]/WToLNunums[9],3)))
pt11.AddLine(000, .500, 1.00, .500)
pt11.AddText(str(round(T_M1000_W10nums[10]/T_M1000_W10nums[9],3)))
pt11.AddLine(000, .600, 1.00, .600)
pt11.AddText(str(round(T_M1500_W10nums[10]/T_M1500_W10nums[9],3)))
pt11.AddLine(000, .700, 1.00, .700)
pt11.AddText(str(round(T_M2000_W10nums[10]/T_M2000_W10nums[9],3)))
pt11.AddLine(000, .800, 1.00, .800)
pt11.AddText(str(round(T_M2500_W10nums[10]/T_M2500_W10nums[9],3)))
pt11.AddLine(000, .900, 1.00, .900)
pt11.AddText(str(round(T_M3000_W10nums[10]/T_M3000_W10nums[9],3)))
pt11.Draw()

c1.SaveAs(outDir+"/"+"effTable.png")
c1.SaveAs(outDir+"/"+"effTable.pdf")
raw_input("hold on")

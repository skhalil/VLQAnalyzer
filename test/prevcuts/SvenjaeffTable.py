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

DYToLLnums = [0,173579.5+107288.4,70155.9+59836.5,52409.7+46910.8,50456.7+45507.2,50014.6+45124.1,19925.9+17249.9,18679.1+16200.7,16464.1+14233.2]
stnums = [0,59028.0+24639.6,25735.7+14313.7,23744.7+13065.3,17629.0+12642.1,17570.6+12601.7,9061.1+6582.6,8633.8+6280.6,8237.1+5987.8]
tt_M2T4nums = [0,589249.2+234015.7,228395.2+135775.0,217763.2+129280.6,174310.7+123401.8,174039.4+123258.7,103071.5+73579.0,98488.5+70403.1,92039.5+65743.0]
WToLNunums = [0,508430.7+301508.9,193130.1+151794.7,139522.5+109383.7,133882.4+106013.9,133294.2+105612.2,55590.0+44474.1,53395.2+42714.9,52255.0+41696.4]
T_M700nums = [0,2312.8+879.0,1279.2+590.9,1231.2+565.2,773.2+527.6,772.9+527.6,464.6+312.1,441.4+300.1,417.3+284.7]
T_M1000nums = [0,4209.7+1587.4,3420.8+1353.6,3336.5+1307.0,1826.3+1225.7,1826.0+1225.7,1400.3+937.7,1365.5+916.3,1320.0+886.8]
T_M1500nums = [0,5995.0+1910.7,5601.3+1793.4,5474.4+1726.0,2862.4+1606.6,2862.0+1606.3,2267.9+1258.0,2211.1+1230.3,2146.3+1204.3]
T_M1700nums = [0,6199.1+1804.0,5916.9+1711.3,5787.8+1726.0,2992.5+1518.7,2992.5+1518.7,2393.4+1202.5,2324.7+1178.1,2261.0+1151.8]
T_M1800nums = [0,6625.8+1832.1,6351.2+1748.6,6187.0+1677.2,3156.4+1545.8,3156.4+1545.8,2507.8+1211.9,2426.9+1187.5,2365.4+1164.0]

c1 = TCanvas('c1', 'c1', 1800, 1000)
pt1 = TPaveText(.05,.05,.15,.95)
pt2 = TPaveText(0.15, 0.05, 0.25, 0.95)
pt3 = TPaveText(0.25, 0.05, 0.35, 0.95)
pt4 = TPaveText(0.35, 0.05, 0.45, 0.95)
pt5 = TPaveText(0.45, 0.05, 0.55, 0.95)
pt6 = TPaveText(0.55, 0.05, 0.65, 0.95)
pt7 = TPaveText(0.65, 0.05, 0.75, 0.95)
pt8 = TPaveText(0.75, 0.05, 0.85, 0.95)
pt9 = TPaveText(0.85, 0.05, 0.95, 0.95)

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
pt1.AddText("T_M700")
pt1.AddLine(0.0, .6, 1.00, .6)
pt1.AddText("T_M1000")
pt1.AddLine(0.0, .7, 1.00, .7)
pt1.AddText("T_M1500")
pt1.AddLine(0.0, .8, 1.00, .8)
pt1.AddText("T_M1700")
pt1.AddLine(0.0, .9, 1.00, .9)
pt1.AddText("T_M1800")
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
pt2.AddText(str(round(T_M700nums[1]/T_M700nums[1],3)))
pt2.AddLine(00, .600, 1.00, .600)
pt2.AddText(str(round(T_M1000nums[1]/T_M1000nums[1],3)))
pt2.AddLine(00, .700, 1.00, .700)
pt2.AddText(str(round(T_M1500nums[1]/T_M1500nums[1],3)))
pt2.AddLine(00, .800, 1.00, .800)
pt2.AddText(str(round(T_M1700nums[1]/T_M1700nums[1],3)))
pt2.AddLine(00, .900, 1.00, .900)
pt2.AddText(str(round(T_M1800nums[1]/T_M1800nums[1],3)))
pt2.Draw()

pt3.AddText("Leading Jet P_{t} > 185 GeV")
pt3.AddLine(00, .100, 1.00, .100)
pt3.AddText(str(round(DYToLLnums[2]/DYToLLnums[1],3)))
pt3.AddLine(00, .200, 1.00, .200)
pt3.AddText(str(round(stnums[2]/stnums[1],3)))
pt3.AddLine(00, .300, 1.00, .300)
pt3.AddText(str(round(tt_M2T4nums[2]/tt_M2T4nums[1],3)))
pt3.AddLine(00, .400, 1.00, .400)
pt3.AddText(str(round(WToLNunums[2]/WToLNunums[1],3)))
pt3.AddLine(00, .500, 1.00, .500)
pt3.AddText(str(round(T_M700nums[2]/T_M700nums[1],3)))
pt3.AddLine(00, .600, 1.00, .600)
pt3.AddText(str(round(T_M1000nums[2]/T_M1000nums[1],3)))
pt3.AddLine(00, .700, 1.00, .700)
pt3.AddText(str(round(T_M1500nums[2]/T_M1500nums[1],3)))
pt3.AddLine(00, .800, 1.00, .800)
pt3.AddText(str(round(T_M1700nums[2]/T_M1700nums[1],3)))
pt3.AddLine(00, .900, 1.00, .900)
pt3.AddText(str(round(T_M1800nums[2]/T_M1800nums[1],3)))
pt3.Draw()

pt4.AddText("Sub-Leading Jet P_{t} > 50 GeV")
pt4.AddLine(00, .100, 1.00, .100)
pt4.AddText(str(round(DYToLLnums[3]/DYToLLnums[2],3)))
pt4.AddLine(00, .200, 1.00, .200)
pt4.AddText(str(round(stnums[3]/stnums[2],3)))
pt4.AddLine(00, .300, 1.00, .300)
pt4.AddText(str(round(tt_M2T4nums[3]/tt_M2T4nums[2],3)))
pt4.AddLine(00, .400, 1.00, .400)
pt4.AddText(str(round(WToLNunums[3]/WToLNunums[2],3)))
pt4.AddLine(00, .500, 1.00, .500)
pt4.AddText(str(round(T_M700nums[3]/T_M700nums[2],3)))
pt4.AddLine(00, .600, 1.00, .600)
pt4.AddText(str(round(T_M1000nums[3]/T_M1000nums[2],3)))
pt4.AddLine(00, .700, 1.00, .700)
pt4.AddText(str(round(T_M1500nums[3]/T_M1500nums[2],3)))
pt4.AddLine(00, .800, 1.00, .800)
pt4.AddText(str(round(T_M1700nums[3]/T_M1700nums[2],3)))
pt4.AddLine(00, .900, 1.00, .900)
pt4.AddText(str(round(T_M1800nums[3]/T_M1800nums[2],3)))
pt4.Draw()

pt5.AddText("2D Lepton Isolation")
pt5.AddLine(00, .100, 1.00, .100)
pt5.AddText(str(round(DYToLLnums[4]/DYToLLnums[3],3)))
pt5.AddLine(00, .200, 1.00, .200)
pt5.AddText(str(round(stnums[4]/stnums[3],3)))
pt5.AddLine(00, .300, 1.00, .300)
pt5.AddText(str(round(tt_M2T4nums[4]/tt_M2T4nums[3],3)))
pt5.AddLine(00, .400, 1.00, .400)
pt5.AddText(str(round(WToLNunums[4]/WToLNunums[3],3)))
pt5.AddLine(00, .500, 1.00, .500)
pt5.AddText(str(round(T_M700nums[4]/T_M700nums[3],3)))
pt5.AddLine(00, .600, 1.00, .600)
pt5.AddText(str(round(T_M1000nums[4]/T_M1000nums[3],3)))
pt5.AddLine(00, .700, 1.00, .700)
pt5.AddText(str(round(T_M1500nums[4]/T_M1500nums[3],3)))
pt5.AddLine(00, .800, 1.00, .800)
pt5.AddText(str(round(T_M1700nums[4]/T_M1700nums[3],3)))
pt5.AddLine(00, .900, 1.00, .900)
pt5.AddText(str(round(T_M1800nums[4]/T_M1800nums[3],3)))
pt5.Draw()

pt6.AddText("ST > 400 GeV")
pt6.AddLine(00, .100, 1.00, .100)
pt6.AddText(str(round(DYToLLnums[5]/DYToLLnums[4],3)))
pt6.AddLine(00, .200, 1.00, .200)
pt6.AddText(str(round(stnums[5]/stnums[4],3)))
pt6.AddLine(00, .300, 1.00, .300)
pt6.AddText(str(round(tt_M2T4nums[5]/tt_M2T4nums[4],3)))
pt6.AddLine(00, .400, 1.00, .400)
pt6.AddText(str(round(WToLNunums[5]/WToLNunums[4],3)))
pt6.AddLine(00, .500, 1.00, .500)
pt6.AddText(str(round(T_M700nums[5]/T_M700nums[4],3)))
pt6.AddLine(00, .600, 1.00, .600)
pt6.AddText(str(round(T_M1000nums[5]/T_M1000nums[4],3)))
pt6.AddLine(00, .700, 1.00, .700)
pt6.AddText(str(round(T_M1500nums[5]/T_M1500nums[4],3)))
pt6.AddLine(00, .800, 1.00, .800)
pt6.AddText(str(round(T_M1700nums[5]/T_M1700nums[4],3)))
pt6.AddLine(00, .900, 1.00, .900)
pt6.AddText(str(round(T_M1800nums[5]/T_M1800nums[4],3)))
pt6.Draw()

pt7.AddText("#geq 1 Higgs Candidate")
pt7.AddLine(00, .100, 1.00, .100)
pt7.AddText(str(round(DYToLLnums[6]/DYToLLnums[5],3)))
pt7.AddLine(00, .200, 1.00, .200)
pt7.AddText(str(round(stnums[6]/stnums[5],3)))
pt7.AddLine(00, .300, 1.00, .300)
pt7.AddText(str(round(tt_M2T4nums[6]/tt_M2T4nums[5],3)))
pt7.AddLine(00, .400, 1.00, .400)
pt7.AddText(str(round(WToLNunums[6]/WToLNunums[5],3)))
pt7.AddLine(00, .500, 1.00, .500)
pt7.AddText(str(round(T_M700nums[6]/T_M700nums[5],3)))
pt7.AddLine(00, .600, 1.00, .600)
pt7.AddText(str(round(T_M1000nums[6]/T_M1000nums[5],3)))
pt7.AddLine(00, .700, 1.00, .700)
pt7.AddText(str(round(T_M1500nums[6]/T_M1500nums[5],3)))
pt7.AddLine(00, .800, 1.00, .800)
pt7.AddText(str(round(T_M1700nums[6]/T_M1700nums[5],3)))
pt7.AddLine(00, .900, 1.00, .900)
pt7.AddText(str(round(T_M1800nums[6]/T_M1800nums[5],3)))
pt7.Draw()

pt8.AddText("#Delta R(higgs,top) > 2")
pt8.AddLine(00, .100, 1.00, .100)
pt8.AddText(str(round(DYToLLnums[7]/DYToLLnums[6],3)))
pt8.AddLine(00, .200, 1.00, .200)
pt8.AddText(str(round(stnums[7]/stnums[6],3)))
pt8.AddLine(00, .300, 1.00, .300)
pt8.AddText(str(round(tt_M2T4nums[7]/tt_M2T4nums[6],3)))
pt8.AddLine(00, .400, 1.00, .400)
if WToLNunums[6] != 0: pt8.AddText(str(round(WToLNunums[7]/WToLNunums[6],3)))
else: pt8.AddText(str(round(WToLNunums[6],3)))
pt8.AddLine(00, .500, 1.00, .500)
pt8.AddText(str(round(T_M700nums[7]/T_M700nums[6],3)))
pt8.AddLine(00, .600, 1.00, .600)
pt8.AddText(str(round(T_M1000nums[7]/T_M1000nums[6],3)))
pt8.AddLine(00, .700, 1.00, .700)
pt8.AddText(str(round(T_M1500nums[7]/T_M1500nums[6],3)))
pt8.AddLine(00, .800, 1.00, .800)
pt8.AddText(str(round(T_M1700nums[7]/T_M1700nums[6],3)))
pt8.AddLine(00, .900, 1.00, .900)
pt8.AddText(str(round(T_M1800nums[7]/T_M1800nums[6],3)))
pt8.Draw()

pt9.AddText("Top P_{t} > 100 GeV")
pt9.AddLine(00, .100, 1.00, .100)
pt9.AddText(str(round(DYToLLnums[8]/DYToLLnums[7],3)))
pt9.AddLine(00, .200, 1.00, .200)
pt9.AddText(str(round(stnums[8]/stnums[7],3)))
pt9.AddLine(00, .300, 1.00, .300)
pt9.AddText(str(round(tt_M2T4nums[8]/tt_M2T4nums[7],3)))
pt9.AddLine(00, .400, 1.00, .400)
if WToLNunums[7] != 0: pt9.AddText(str(round(WToLNunums[8]/WToLNunums[7],3)))
else: pt9.AddText(str(round(WToLNunums[7],3)))
pt9.AddLine(00, .500, 1.00, .500)
pt9.AddText(str(round(T_M700nums[8]/T_M700nums[7],3)))
pt9.AddLine(00, .600, 1.00, .600)
pt9.AddText(str(round(T_M1000nums[8]/T_M1000nums[7],3)))
pt9.AddLine(00, .700, 1.00, .700)
pt9.AddText(str(round(T_M1500nums[8]/T_M1500nums[7],3)))
pt9.AddLine(00, .800, 1.00, .800)
pt9.AddText(str(round(T_M1700nums[8]/T_M1700nums[7],3)))
pt9.AddLine(00, .900, 1.00, .900)
pt9.AddText(str(round(T_M1800nums[8]/T_M1800nums[7],3)))
pt9.Draw()

c1.SaveAs(outDir+"/"+"prevcutseffTable.png")
c1.SaveAs(outDir+"/"+"prevcutseffTable.pdf")
raw_input("hold on")

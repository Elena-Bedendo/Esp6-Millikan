# Millikan
import ROOT
import math as m
import numpy as np

# Main
def MultiGaus():
    multigaus = "[2]*TMath::Gaus(x,[0],[1],1)"
    for i in range(3,5,1):
        multigaus +=  " + [" + str(i) +"]*TMath::Gaus(x,"+ str(i-1) +"*[0],[1],1) "
    return multigaus

# Acquisizione dati
# Istogramma.
h = ROOT.TH1D("h", "Millikan" , 50 , 0 , 5.6)

# prende i dati dal file e li mette in un array.
x = np.loadtxt('Millikan.dat')

for x_i in x:
    h.Fill(x_i)

h.Draw()
fun_Gaus = MultiGaus()
print(fun_Gaus)
f = ROOT.TF1("f" , fun_Gaus  , 0 , 5.6)
f.SetParameters(1.6 , .1 , 7 , 9, 8)

h.Fit("f" , "L")

ROOT.gApplication.Run(True)

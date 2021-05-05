import os
os.chdir("G:\\GitHubRepo\\Crypto\\Set2\\RSA\\")
import extended_euclid as eea
import exp 

#Dati del problema
c1 = 13740701343175031613859506260680271
c2 = 442020648620790478265510268903148188611479520134128911 
n = 1200867589138402836833011627922648843865398758356119243237528992192661195883356632897345588719304934438534205354787918897834861577085344762327143956220911721261528444200091612203799709834594997775067917847690315178675148605331912292785817786238119642200812571328900475396454557843711810878201457471117182510681991129539167165552073440243913144926216242708247975357913354302233984628116835035339887667027876020733894592318754941490852771134623356130705203596572659
e1 = 7
e2 = 11

gcd,x,y = eea.EEA(e1,e2)
c1_inv = eea.EEA(c1,n)[1]
m = exp.exp_veloce(c1_inv,-1*x,n) * exp.exp_veloce(c2,y,n)

print("m recuperato: ", m)
if(c1 == exp.exp_veloce(m,e1,n) and c2 == exp.exp_veloce(m,e2,n)):
    print("L'operazione ha avuto successo")
else:
    print("Operazione fallita")
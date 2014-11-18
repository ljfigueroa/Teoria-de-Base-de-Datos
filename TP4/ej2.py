#!/usr/bin/python

'''
def cuentadf(F):
    cuenta = []
    for i,k in enumerate(F.keys()):
        cuenta[k]=len(k)
    return cuenta
'''

def cuentadf(F):
  cuenta = []
  for i,k in enumerate(F.keys()):
    cuenta.append(len(k))
  return cuenta

def apareceFunc(R,F):
  aparece = []
  for r in R:
    aux = []
    for i,j in enumerate(F.keys()):
      if r in j:
        aux.append(i) 
    aparece.append(aux)

  C={}
  for i,k in enumerate(R):
     C[k]=aparece[i]

  return C

def agregarFunc(Alfa,Res,DF,aparece,cuenta):
  
  print "------------------------------- \n", "RESULTADO IN=",Res
  for a in Alfa:
    if a not in Res:
      Res.add(a)
      if [] != aparece[a]:
        print "--IF-- \n"
        print "a=",a, "aparece=",aparece[a]
        print "cuenta =", cuenta
        for  j in aparece[a]:
          cuenta[j] = (cuenta[j] - 1)
          if cuenta[j] == 0:
            print "j=",j
            if isin(DF.keys()[j], Res): 
              print "ultimo caso: DF.k[j]=",DF.keys()[j], Res
              agregarFunc(DF[(DF.keys()[j])], Res, DF,aparece,cuenta)

  
def isin(String, Set):
  for i in String:
    if i not in Set:
      return False

  return True

def cierre(Alfa,F,R):
  resultado=set([])
  aparece = apareceFunc(R,F)
  cuentaf = cuentadf(F)
  agregarFunc(Alfa,resultado,F,aparece,cuentaf)
  return resultado


def main():
    
  F = {"AB":"C", "AD":"GH", "BD":"EF","A":"I", "H":"J"}
  R = set (['A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'J'])

  print "F =", F
  print "R =",R 
  print "cuentadf =",cuentadf(F)
  print "F.keys() =",F.keys()    

  print "APARECE -> ", apareceFunc(R,F)
  print "APARECE['A'] -> ", apareceFunc(R,F)['A']
  
  alfa = set(['A','B','D','H'])
  print "--> cierre: ", cierre(alfa,F,R)

if __name__ == "__main__":
  main()


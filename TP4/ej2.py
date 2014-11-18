#!/usr/bin/python


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
  
  for a in Alfa:
    if a not in Res:
      Res.add(a)
      if [] != aparece[a]:
        print "RESULTADO NUEVO =", Res
        for  j in aparece[a]:
          cuenta[j] = (cuenta[j] - 1)
          if cuenta[j] == 0:
            print "set -> ",(set(DF.keys()[j])), "in", Res
            atrib = DF.keys()[j]
            if set(atrib).issubset(Res): 
              det = DF[atrib]
              agregarFunc(set(det), Res, DF,aparece,cuenta)

  
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
    
  F1 = {"AB":"C", "AD":"GH", "BD":"EF","A":"I", "H":"J"}
  R1 = set (['A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'J'])

  R2 = set(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
  F2 = {'A':'BC', 'C':'D', 'D':'G', 'H':'E', 'E':'A', 'E':'H'}
  
  R3 = set(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
  F3 = {'A':'G', 'A':'F', 'B':'E', 'C':'D', 'E':'A', 'D':'B', 'GF':'C'}


  alfa = set(['A','B','D','H'])
  print "--> cierre: ", cierre(alfa,F1,R1)

  print "cirre de F#"
  alfa = set(['A'])
  print "--> cierre: ", cierre(alfa,F3,R3)

if __name__ == "__main__":
  main()


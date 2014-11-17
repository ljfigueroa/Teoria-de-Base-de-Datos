#!/usr/bin/python

def cardinalDet(F):
    cuentadf = []
    for i,k in enumerate(F.keys()):
        cuentadf.append(len(k))
    return cuentadf
    
def apareceFunc(R,F):
	aparece = []
	for r in R:
		aux = []
		for i,j in enumerate(F.keys()):
			if r in j:
				aux.append(i) 
		aparece.append(aux)
	return aparece

def main():
    
	F = {"AB":"C", "AD":"GH", "BD":"EF","A":"I", "H":"J"}
	print cardinalDet(F)
	print F.keys()		

	R = set (['A', 'C', 'B', 'E', 'D', 'G', 'F', 'I', 'H', 'J'])
	print apareceFunc(R,F)

if __name__ == "__main__":
	main()


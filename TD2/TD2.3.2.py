from pyscipopt import Model

def reines(n):
    model=Model()
    q=[model.addVar('q%i'%i) for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            True # model.addCons()

if __name__=="__main__":
	reines(4)

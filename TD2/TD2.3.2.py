from pyscipopt import Model

def reines(n)
    model=Model()
    q=[model.addVar('q%i'%i) for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            model.addCons()

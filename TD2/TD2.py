from itertools import combinations

def peterson():
    V = list(range(10))
    A = [(0, 1), (0, 4), (0, 7), (1, 5), (1, 2), (2, 3), (2, 9), (3, 4), (3, 6), (4, 8), (5, 6), (5, 8), (6, 7), (7, 9),
         (8, 9)]

    res = "c td2.1 \n"

    nb_equations = 4 * len(V) + 3 * len(A)
    res += "p cnf 30 " + str(nb_equations) + '\n'
    for v in V:
        variables = [str(v * 3 + i + 1) for i in range(3)]
        res += " ".join(variables) + " 0 \n"
        res += "-" + variables[0] + " -" + variables[1] + " 0 \n"
        res += "-" + variables[0] + " -" + variables[2] + " 0 \n"
        res += "-" + variables[2] + " -" + variables[1] + " 0 \n"
    for v1, v2 in A:
        variables_1 = [str(v1 * 3 + i + 1) for i in range(3)]
        variables_2 = [str(v2 * 3 + i + 1) for i in range(3)]
        for i in range(3):
            res += "-" + variables_1[i] + " -" + variables_2[i] + " 0 \n"
    return res



def Reine(n, comment="td"):
    res = "c "+comment+" \n"
    n_equation = 0

    res_1 = ""

    for line in range(n):
        variables = [str(line * n + 1 + i) for i in range(n)]
        res_1 += " ".join(variables) + " 0 \n"
        n_equation += 1
        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    for col in range(n):
        variables = [str(col + 1 + i * n) for i in range(n)]
        res_1 += " ".join(variables) + " 0 \n"
        n_equation += 1
        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    for diag in range(1, n + 1):
        i = 1
        variables = [str(diag * n)]
        while diag * n - i * (n + 1) > 0:
            variables.append(str(diag * n - i * (n + 1)))
            i += 1

        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    for diag in range(1, n):
        i = 1
        variables = [str(n * diag + 1)]
        while n * diag + i * (n + 1) < n * n:
            variables.append(str(n + diag + i * (n + 1)))
            i += 1
        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    for diag in range(n):
        i = 1
        variables = [str(diag * n + 1)]
        while diag * n + 1 - i * (n - 1) > 0:
            variables.append(str(diag * n + 1 - i * (n - 1)))
            i += 1

        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    for diag in range(2, n + 1):
        i = 1
        variables = [str(n * diag)]
        while n * diag + i * (n - 1) < n * n:
            variables.append(str(n * diag + i * (n - 1)))
            i += 1

        for v1, v2 in combinations(variables, 2):
            res_1 += "-" + v1 + " -" + v2 + " 0\n"
            n_equation += 1

    res += "p cnf " + str(n * n) + " " + str(n_equation) + '\n'
    res += res_1
    return res




if __name__ == "__main__":
    with open("td2.1.cnf", 'w', encoding='utf-8') as f:
        f.write(peterson())
    # 120 solutions possibles

    with open("td2.2.cnf", 'w', encoding='utf-8') as f:
        f.write(Reine(4, comment="td2.2"))

    # n=4 on a 2 solutions
    # solution 2,4,1,3 (meilleure solution lexicographiquement)
    # solutions
    # Sommet 0 : R
    # Sommet 1 : V
    # Sommet 2 : R
    # Sommet 3 : V
    # Sommet 4 : B
    # Sommet 5 : R
    # Sommet 6 : B
    # Sommet 7 : V
    # Sommet 8 : V
    # Sommet 9 : B

    with open("td2.3.1.1.cnf", 'w', encoding='utf-8') as f:
        f.write(Reine(10,comment="td2.3.1 10 reines"))
    # with SAT (scip 3482 feasible solutions) ~30s
    # with ZIMPL (scip
    with open("td2.3.2.1.cnf", 'w', encoding='utf-8') as f:
        f.write(Reine(20,comment="td2.3.2 20 reines"))




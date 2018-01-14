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



def SAT(n):
    res = "c td2.2 \n"
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
    peterson()
    # 120 solutions possibles

    print(SAT(4))
    # n=4 on a 2 solutions
    # Exercice 2 :
    # solution 2,4,1,3

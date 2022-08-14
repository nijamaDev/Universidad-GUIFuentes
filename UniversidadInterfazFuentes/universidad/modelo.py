from minizinc import Instance, Model, Solver

uni = Model("Universidad.mzn")

gecode = Solver.lookup("gecode")

instance = Instance(gecode, uni)

def resolver(n,m,ciudades):

    instance["n"] = n
    instance["m"] = m
    instance["ciudades"] = ciudades

    result = instance.solve()
    lgstDist = round(pow(result["largestDistance"],0.5),2)

    return lgstDist
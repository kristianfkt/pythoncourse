import pandas as pd 
import pybamm

def make():
    model = pybamm.lithium_ion.SPM()

    dcir = [
        (f"Charge at {c}C for 10 seconds",
        "Rest for 30 seconds",
        f"Discharge at {c}C for 10 seconds",
        "Rest for 30 seconds") for c in [0.5, 1.0, 1.5, 2.0, 2.5]]
    
    dcir = [item for sublist in dcir for item in sublist]
    
    dod = 0.05
    crt = 0.1
    pulse = (
        f"Charge at {crt}C for {0.05/crt} hours or until 4.2V",
        "Rest for 2 hours",
    )

    expr = ["Discharge at 0.1C until 2.5V",
            "Rest for 2 hours"]
    for _ in range(int(1/dod)):
        expr.extend(dcir)
        expr.extend(pulse)

    experiment = pybamm.Experiment(expr)
    simulation = pybamm.Simulation(model, solver=pybamm.CasadiSolver(), experiment=experiment)
    solution = simulation.solve([0,3600],showprogress=True)
    solution.plot()
        #     [
            
    #         *dcir,
    #         *pulse,
    #         *dcir,
    #         *pulse,
    #     ] * 1/dod



    

if __name__ == "__main__":
    make()

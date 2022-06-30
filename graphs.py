import matplotlib.pyplot as plt
import numpy as np


def money_supply(initial_ms: int, final_ms: int, size: int = 10, ticks: int = 100):
    # money demand function
    x = np.linspace(1, size, ticks)
    Ly = 1 / (0.1 * x)
    plt.plot(x, Ly)
    # initial money supply function
    plt.plot((initial_ms, initial_ms), (0, size))
    # final money supply function
    plt.plot((final_ms, final_ms), (0, size))

    plt.legend(["L(y)", "OM", "OM'"])
    plt.ylabel("Tasa de interés")
    plt.xlabel("Oferta Monetaria")
    plt.show()


def demand_contraction(
    supply_slope: int, demand_slope: int, final_demand_offset: int = 2, size: int = 11
):
    supply_curve = []
    initial_demand_curve = []
    final_demand_curve = []
    for x in range(size):
        supply_curve.append(x * supply_slope)
        initial_demand_curve.append(demand_slope * (size - x))
        final_demand_curve.append(demand_slope * (size - final_demand_offset - x))
    plt.plot(supply_curve)
    plt.plot(initial_demand_curve)
    plt.plot(final_demand_curve)
    plt.legend(["OA", "DA", "DA'"])
    plt.ylabel("Nivel General de Precios")
    plt.xlabel("PBI")
    plt.show()


def main():
    demand_contraction(10, 10)
    money_supply(6, 3)


if __name__ == "__main__":
    main()

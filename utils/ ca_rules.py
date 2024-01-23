
# Utility functions for cellular automata rules to be used in miner and validator routines
import cellpylib as cpl

# This is the main simulation runner for simple CA used in miner and validator routines
def run_ca_simulation(self, initial_state, steps, rule_func, neighborhood_func):
    # Initialize the cellular automata with the provided initial state
    ca = initial_state

    # Apply the ruleset and run the simulation
    ca = cpl.evolve2d(ca, timesteps=steps, apply_rule=rule_func, neighbourhood=neighborhood_func)

    return ca


def conway_rule(n, c, t):
    sum_n = sum(n)
    return c and 2 <= sum_n <= 3 or sum_n == 3

def moore_neighborhood(c, t):
    return cpl.moore_neighborhood(c, t, range_=1)

def von_neumann_neighborhood(c, t):
    return cpl.von_neumann_neighborhood(c, t, range_=1)

# Game of Life HighLife: a variant of Conway's Game of Life that also gives birth to a cell if there are 6 neighbors.
def highlife_rule(n, c, t):
    sum_n = sum(n)
    return c and 2 <= sum_n <= 3 or sum_n == 6

# Day & Night: a variant of Conway's Game of Life that also gives birth to a cell if there are 3, 6, 7, or 8 neighbors.
def day_and_night_rule(n, c, t):
    sum_n = sum(n)
    return sum_n in (3, 6, 7, 8) or c and sum_n in (4, 6, 7, 8)

# a one-dimensional cellular automaton rule introduced by Stephen Wolfram. known for its chaotic behavior.
def rule_30(n, c, t):
    return cpl.nks_rule(n, 30)

# Rule 110: It's another one-dimensional cellular automaton rule introduced by Stephen Wolfram. It's known for being Turing complete.
def rule_110(n, c, t):
    return cpl.nks_rule(n, 110)

# Fredkin's is a cellular automaton rule where a cell is "born" if it has exactly one neighbor, and a cell "survives" if it has exactly two neighbors. Otherwise, the cell dies or remains dead.
def fredkin_rule(n, c, t):
    sum_n = sum(n)
    return sum_n == 1 or c and sum_n == 2

# A three-state simulation. A cell is "born" if it was dead and has exactly two neighbors. A live cell dies in the next generation, and a dead cell remains dead.
def brians_brain_rule(n, c, t):
    sum_n = sum(n)
    if c == 0 and sum_n == 2:
        return 1
    elif c == 1:
        return 2
    elif c == 2:
        return 0

# Seeds is a cellular automaton where a cell is "born" if it has exactly two neighbors, and a cell "dies" otherwise.
def seeds_rule(n, c, t):
    sum_n = sum(n)
    return sum_n == 2


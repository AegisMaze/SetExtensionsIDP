import csv

from graph_gen import *

scfs = ["plurality", "borda", "instant runoff", "pareto", "omninomination", "condorcet", "copeland", "top cycle", "uncovered set", "bipartisan set"]
exts = ["kelly", "fishburn", "gardenfoers", "optimist", "pessimist", "opt pes"]

for n in [3,5,7,9,11]:
    for m in [3,4,5]:
        f = open("results/impartial_" + str(n) + "_" + str(m) + ".csv")
        counts = np.array([list(map(int,rec)) for rec in csv.reader(f, delimiter=',')])
        f.close()
        count_to_graph(scfs, exts, counts, "graphs/impartial_" + str(n) + "_" + str(m) + ".png")

        f = open("results/cube" + str(n) + "_" + str(m) + ".csv")
        counts = np.array([list(map(int, rec)) for rec in csv.reader(f, delimiter=',')])
        f.close()
        count_to_graph(scfs, exts, counts, "graphs/cube" + str(n) + "_" + str(m) + ".png")

        f = open("results/mallows5_" + str(n) + "_" + str(m) + ".csv")
        counts = np.array([list(map(int, rec)) for rec in csv.reader(f, delimiter=',')])
        f.close()
        count_to_graph(scfs, exts, counts, "graphs/mallows5_" + str(n) + "_" + str(m) + ".png")
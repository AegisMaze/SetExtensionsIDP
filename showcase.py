from timeit import default_timer as timer
from strprf_new import *
from tourneys import *
from graph_gen import *

import json

x = 10
d = 3

scfs = ["plurality", "borda", "instant runoff", "pareto", "omninomination", "condorcet", "copeland", "top cycle", "uncovered set", "bipartisan set", "2-plurality", "2-borda", "2-top cycle"]
exts = ["kelly", "fishburn", "gardenfoers", "optimist", "pessimist", "opt pes", "singleton", "even chance"]

con_res = [[condorcet_t(number_to_tournament(i, m)) for i in range(2 ** (m * (m - 1) >> 1))] for m in [3,4,5]]
cop_res = [[copeland_t(number_to_tournament(i, m)) for i in range(2 ** (m * (m - 1) >> 1))] for m in [3,4,5]]
top_res = [[top_cycle_t(number_to_tournament(i, m)) for i in range(2 ** (m * (m - 1) >> 1))] for m in [3,4,5]]
unc_res = [[uncovered_set_t(number_to_tournament(i, m)) for i in range(2 ** (m * (m - 1) >> 1))] for m in [3,4,5]]
bip_res = [[bipartisan_set_t(number_to_tournament(i, m)) for i in range(2 ** (m * (m - 1) >> 1))] for m in [3,4,5]]
res = [[con_res[m], cop_res[m], top_res[m], unc_res[m], bip_res[m]] for m in range(3)]

start = timer()
for n in [3,5,7,9,11]:
    for m in [3,4,5]:
        profiles = [generate_profile(n, m) for _ in range(x)]
        with open("profiles/impartial_" + str(n) + "_" + str(m) + ".json", 'w') as fout:
            json.dump([str(p) for p in profiles], fout)
        counts = sum(manipulable_count_all(p, n, res[m - 3]) for p in profiles).transpose()
        np.savetxt("results/impartial_" + str(n) + "_" + str(m) + ".csv", counts, delimiter=",", fmt="%d")
        count_to_graph(scfs, exts, counts, "graphs/impartial_" + str(n) + "_" + str(m) + ".png")

        profiles = [generate_cartesian_profile(n, m, d) for _ in range(x)]
        with open("profiles/cube" + str(n) + "_" + str(m) + ".json", 'w') as fout:
            json.dump([str(p) for p in profiles], fout)
        counts = sum(manipulable_count_all(p, n, res[m - 3]) for p in profiles).transpose()
        np.savetxt("results/cube" + str(n) + "_" + str(m) + ".csv", counts, delimiter=",", fmt="%d")
        count_to_graph(scfs, exts, counts, "graphs/cube" + str(n) + "_" + str(m) + ".png")

        dists = mallows_dists(m)
        profiles = [generate_mallows_profile(n, m, 0.25, dists) for _ in range(x)]
        with open("profiles/mallows25" + str(n) + "_" + str(m) + ".json", 'w') as fout:
            json.dump([str(p) for p in profiles], fout)
        counts = sum(manipulable_count_all(p, n, res[m - 3]) for p in profiles).transpose()
        np.savetxt("results/mallows25_" + str(n) + "_" + str(m) + ".csv", counts, delimiter=",", fmt="%d")
        count_to_graph(scfs, exts, counts, "graphs/mallows25_" + str(n) + "_" + str(m) + ".png")

        profiles = [generate_mallows_profile(n, m, 0.5, dists) for _ in range(x)]
        with open("profiles/mallows5" + str(n) + "_" + str(m) + ".json", 'w') as fout:
            json.dump([str(p) for p in profiles], fout)
        counts = sum(manipulable_count_all(p, n, res[m - 3]) for p in profiles).transpose()
        np.savetxt("results/mallows5_" + str(n) + "_" + str(m) + ".csv", counts, delimiter=",", fmt="%d")
        count_to_graph(scfs, exts, counts, "graphs/mallows5_" + str(n) + "_" + str(m) + ".png")
end = timer()
print(end - start)
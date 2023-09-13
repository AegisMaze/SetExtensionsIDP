import numpy as np
import matplotlib.pyplot as plt

def count_to_graph(scfs, exts, counts, name):
    width = 0.1
    colors = ['r', 'b', 'g', 'y', 'm', 'c']
    X = np.arange(len(scfs))
    fig = plt.subplots(figsize =(20, 8))
    for i in range(len(exts)):
        plt.bar(X + width * i, counts[i,0:len(scfs)], color = colors[i % len(colors)], width = width, label = exts[i])
    plt.xlabel('Social Choice Function', fontweight ='bold', fontsize = 12)
    plt.ylabel('Manipulable Profiles', fontweight ='bold', fontsize = 12)
    plt.xticks([r + width for r in range(len(scfs))], [scf for scf in scfs])
    plt.legend()
    plt.savefig(name)
    plt.close()
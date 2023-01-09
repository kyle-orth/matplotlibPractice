import matplotlib.pyplot as plt
# import cProfile
# import visualize_profile


def run():
    names = ['Group A', 'Group B', 'Group C']
    values = [1, 10, 100]
    plt.figure(1, figsize=(8, 5))
    plt.subplot(131)
    plt.bar(names, values, edgecolor='k', linewidth=2)
    my_plot = plt.subplot(132)
    plt.scatter(names, values, s=40, c='r', marker='^')
    x_labels = my_plot.get_xticklabels()
    plt.setp(x_labels, rotation=45, horizontalalignment='right')
    plt.subplot(133)
    plt.plot(names, values, 'g--')
    plt.suptitle('Title')

    names = [1, 2, 3, 4, 5, 6]
    values = [1, 4, 9, 16, 25, 36]
    plt.figure(2, figsize=(4, 6))
    plt.plot(names, values)
    plt.annotate('point(2, 4)', xy=(2, 4), xytext=(4, 2),
                 arrowprops=dict(facecolor='green', shrink=0.1))
    plt.show()


run()
"""
# PROFILING
stats_file = 'profiling_stats.txt'
dest_file = 'readable_stats.txt'
cProfile.run('run()', stats_file)
visualize_profile.run(stats_file, dest_file, 8)
"""

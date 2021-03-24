from r6stats import Stats, Platform

stats = Stats(key="")
generic_stats = stats.get_generic_stats(username="BikiniBodhi", platform=Platform.pc)

print(generic_stats.wins)

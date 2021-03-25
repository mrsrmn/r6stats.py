from r6stats import Stats, Platform

stats = Stats(key="")
generic_stats = stats.get_operator_stats(username="BikiniBodhi", platform=Platform.pc, operator="sledge")

print(generic_stats.ctu)

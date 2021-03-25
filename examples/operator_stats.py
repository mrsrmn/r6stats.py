from r6stats import Stats, Platform

stats = Stats(key="385b24e5-6f3a-4f13-8646-61bf1b9a2c08")
generic_stats = stats.get_operator_stats(username="BikiniBodhi", platform=Platform.pc, operator="sledge")

print(generic_stats.ctu)

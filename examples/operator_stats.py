from r6stats import Stats, Platform, Operators

stats = Stats(key="")
operator_stats = stats.get_operator_stats(username="BikiniBodhi", platform=Platform.pc, operator=Operators.jager)

print(operator_stats.kd)

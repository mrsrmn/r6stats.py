from r6stats import Stats, Platform, Seasons

stats = Stats(key="")
generic_stats = stats.get_seasonal_stats(username="BikiniBodhi", platform=Platform.pc, season=Seasons.crimson_heist)

print(generic_stats.rank_image)

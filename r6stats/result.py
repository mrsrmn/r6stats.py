class GenericResult:
    def __init__(self, username, platform, ubisoft_id, uplay_id, avatar_url, last_updated, aliases, level, total_xp,
                 lootbox_probability, assists, barricades_deployed, blind_kills, bullets_fired, dbnos, deaths, draws,
                 distance_travelled, gadgets_destroyed, games_played, headshots, kd, kills, losses, melee_kills, wl,
                 penetration_kills, playtime, rappel_breaches, reinforcements_deployed, revives, suicides, wins,
                 casual_data, ranked_data, unranked_data, gamemode_bomb, gamemode_secure, gamemode_hostage,
                 bullets_hit):
        self.username = username
        self.platform = platform
        self.ubisoft_id = ubisoft_id
        self.uplay_id = uplay_id
        self.avatar_url = avatar_url
        self.last_updated = last_updated
        self.aliases = aliases
        self.level = level
        self.total_xp = total_xp
        self.lootbox_probability = lootbox_probability
        self.assists = assists
        self.barricades_deployed = barricades_deployed
        self.blind_kills = blind_kills
        self.bullets_fired = bullets_fired
        self.dbnos = dbnos
        self.deaths = deaths
        self.draws = draws
        self.distance_travelled = distance_travelled
        self.gadgets_destroyed = gadgets_destroyed
        self.games_played = games_played
        self.headshots = headshots
        self.kd = kd
        self.kills = kills
        self.losses = losses
        self.melee_kills = melee_kills
        self.wl = wl
        self.penetration_kills = penetration_kills
        self.playtime = playtime
        self.rappel_breaches = rappel_breaches
        self.reinforcements_deployed = reinforcements_deployed
        self.revives = revives
        self.suicides = suicides
        self.wins = wins
        self.casual_data = casual_data
        self.ranked_data = ranked_data
        self.unranked_data = unranked_data
        self.gamemode_bomb = gamemode_bomb
        self.gamemode_secure = gamemode_secure
        self.gamemode_hostage = gamemode_hostage
        self.bullets_hit = bullets_hit


class SeasonalResult:
    def __init__(self, username, platform, ubisoft_id, uplay_id, avatar_url, last_updated, name, start_date, end_date,
                 max_mmr, max_rank, losses, mmr, next_rank_mmr, prev_rank_mmr, rank, skill_mean, wins, kills, deaths,
                 skill_standard_deviation, created_for_date, last_match_mmr_change, last_match_skill_mean_change,
                 last_match_skill_standard_deviation_change, last_match_result, champions_rank_position, rank_text,
                 rank_image, max_rank_text, max_rank_image, abandons):
        self.username = username
        self.platform = platform
        self.ubisoft_id = ubisoft_id
        self.uplay_id = uplay_id
        self.avatar_url = avatar_url
        self.last_updated = last_updated
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.max_mmr = max_mmr
        self.max_rank = max_rank
        self.losses = losses
        self.mmr = mmr
        self.next_rank_mmr = next_rank_mmr
        self.prev_rank_mmr = prev_rank_mmr
        self.rank = rank
        self.skill_mean = skill_mean
        self.wins = wins
        self.kills = kills
        self.deaths = deaths
        self.skill_standard_deviation = skill_standard_deviation
        self.created_for_date = created_for_date
        self.last_match_mmr_change = last_match_mmr_change
        self.last_match_skill_mean_change = last_match_skill_mean_change
        self.last_match_skill_standard_deviation_change = last_match_skill_standard_deviation_change
        self.last_match_result = last_match_result
        self.champions_rank_position = champions_rank_position
        self.rank_text = rank_text
        self.rank_image = rank_image
        self.max_rank_text = max_rank_text
        self.max_rank_image = max_rank_image
        self.abandons = abandons


class OperatorResult:
    def __init__(self, username, platform, ubisoft_id, uplay_id, avatar_url, last_updated, name, ctu, role, kills, kd,
                 deaths, wins, losses, wl, headshots, dbnos, melee_kills, experience, playtime, badge_image, abilities):
        self.username = username
        self.platform = platform
        self.ubisoft_id = ubisoft_id
        self.uplay_id = uplay_id
        self.avatar_url = avatar_url
        self.last_updated = last_updated
        self.name = name
        self.ctu = ctu
        self.role = role
        self.kills = kills
        self.kd = kd
        self.deaths = deaths
        self.wins = wins
        self.wl = wl
        self.headshots = headshots
        self.wins = wins
        self.losses = losses
        self.dbnos = dbnos
        self.melee_kills = melee_kills
        self.experience = experience
        self.playtime = playtime
        self.badge_image = badge_image
        self.abilities = abilities


class WeaponResult:
    def __init__(self, username, platform, ubisoft_id, uplay_id, avatar_url, last_updated, weapon_name, category, kills,
                 deaths, kd, headshots, headshot_percentage, times_chosen, bullets_fired, bullets_hit):
        self.username = username
        self.platform = platform
        self.ubisoft_id = ubisoft_id
        self.uplay_id = uplay_id
        self.avatar_url = avatar_url
        self.last_updated = last_updated
        self.weapon_name = weapon_name
        self.category = category
        self.kills = kills
        self.deaths = deaths
        self.kd = kd
        self.headshots = headshots
        self.headshot_percentage = headshot_percentage
        self.times_chosen = times_chosen
        self.bullets_fired = bullets_fired
        self.bullets_hit = bullets_hit


class WeaponCategoryResult:
    def __init__(self, username, platform, ubisoft_id, uplay_id, avatar_url, last_updated, category, kills,
                 deaths, kd, headshots, headshot_percentage, times_chosen, bullets_fired, bullets_hit):
        self.username = username
        self.platform = platform
        self.ubisoft_id = ubisoft_id
        self.uplay_id = uplay_id
        self.avatar_url = avatar_url
        self.last_updated = last_updated
        self.category = category
        self.kills = kills
        self.deaths = deaths
        self.kd = kd
        self.headshots = headshots
        self.headshot_percentage = headshot_percentage
        self.times_chosen = times_chosen
        self.bullets_fired = bullets_fired
        self.bullets_hit = bullets_hit

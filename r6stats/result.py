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

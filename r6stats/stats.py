import requests
import json
from .result import GenericResult


class Stats:
    def __init__(self, key):
        self.key = key


    def get_generic_stats(self, username, platform):
        headers = {"Authorization": f"Bearer {self.key}"}

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/generic',
                               headers=headers)
        content = json.loads(request.content)

        return GenericResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            aliases=content["aliases"],
            level=content["progression"]["level"],
            lootbox_probability=content["progression"]["lootbox_probability"],
            total_xp=content["progression"]["total_xp"],
            assists=content["stats"]["general"]["assists"],
            barricades_deployed=content["stats"]["general"]["barricades_deployed"],
            blind_kills=content["stats"]["general"]["blind_kills"],
            bullets_fired=content["stats"]["general"]["bullets_fired"],
            bullets_hit=content["stats"]["general"]["bullets_hit"],
            dbnos=content["stats"]["general"]["dbnos"],
            deaths=content["stats"]["general"]["deaths"],
            distance_travelled=content["stats"]["general"]["distance_travelled"],
            draws=content["stats"]["general"]["draws"],
            gadgets_destroyed=content["stats"]["general"]["gadgets_destroyed"],
            games_played=content["stats"]["general"]["games_played"],
            headshots=content["stats"]["general"]["headshots"],
            kd=content["stats"]["general"]["kd"],
            kills=content["stats"]["general"]["kills"],
            losses=content["stats"]["general"]["losses"],
            melee_kills=content["stats"]["general"]["melee_kills"],
            penetration_kills=content["stats"]["general"]["penetration_kills"],
            playtime=content["stats"]["general"]["playtime"],
            rappel_breaches=content["stats"]["general"]["rappel_breaches"],
            reinforcements_deployed=content["stats"]["general"]["reinforcements_deployed"],
            revives=content["stats"]["general"]["revives"],
            suicides=content["stats"]["general"]["suicides"],
            wins=content["stats"]["general"]["wins"],
            wl=content["stats"]["general"]["wl"],
            casual_data=content["stats"]["queue"]["casual"],
            ranked_data=content["stats"]["queue"]["ranked"],
            unranked_data=content["stats"]["queue"]["other"],
            gamemode_bomb=content["stats"]["gamemode"]["bomb"],
            gamemode_secure=content["stats"]["gamemode"]["secure_area"],
            gamemode_hostage=content["stats"]["gamemode"]["hostage"]
        )

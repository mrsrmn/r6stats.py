import requests
import json
from .result import GenericResult, SeasonalResult, OperatorResult, WeaponResult, WeaponCategoryResult
from .platforms import Platform
from .seasons import Seasons
from .exceptions import ApiError


class Stats:
    def __init__(self, key):
        self.key = key
        self.headers = {"Authorization": f"Bearer {self.key}",
                        "User-Agent": "r6stats.py/1.0.0"}

    def get_generic_stats(self, username, platform: Platform):

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/generic',
                               headers=self.headers)
        content = json.loads(request.content)

        self.check_for_api_error(content)

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

    def get_seasonal_stats(self, username, platform: Platform, season: Seasons):

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/seasonal',
                               headers=self.headers)
        content = json.loads(request.content)
        self.check_for_api_error(content)

        region = content["seasons"][season]["regions"]["ncsa"][0]

        return SeasonalResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            name=content["seasons"][season]["name"],
            start_date=content["seasons"][season]["start_date"],
            end_date=content["seasons"][season]["end_date"],
            abandons=region["abandons"],
            losses=region["losses"],
            max_rank=region["max_rank"],
            max_mmr=region["max_mmr"],
            mmr=region["mmr"],
            next_rank_mmr=region["next_rank_mmr"],
            prev_rank_mmr=region["prev_rank_mmr"],
            rank=region["rank"],
            skill_mean=region["skill_mean"],
            skill_standard_deviation=region["skill_standard_deviation"],
            created_for_date=region["created_for_date"],
            wins=region["wins"],
            kills=region["kills"],
            deaths=region["deaths"],
            last_match_mmr_change=region["last_match_mmr_change"],
            last_match_result=region["last_match_result"],
            last_match_skill_standard_deviation_change=region["last_match_skill_standard_deviation_change"],
            last_match_skill_mean_change=region["last_match_skill_mean_change"],
            champions_rank_position=region["champions_rank_position"],
            max_rank_text=region["max_rank_text"],
            max_rank_image=region["max_rank_image"],
            rank_image=region["rank_image"],
            rank_text=region["rank_text"]
        )

    def get_operator_stats(self, username, platform: Platform, operator: str):

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/operators',
                               headers=self.headers)
        name = None
        ctu = None
        dbnos = None
        abilities = None
        kd = None
        wl = None
        kills = None
        badge_image = None
        deaths = None
        experience = None
        role = None
        wins = None
        headshots = None
        losses = None
        melee_kills = None
        playtime = None

        content = json.loads(request.content)
        self.check_for_api_error(content)

        for op in content["operators"]:
            if op["name"] == operator.capitalize():
                name = op["name"]
                ctu = op["ctu"]
                dbnos = op["dbnos"]
                abilities = op["abilities"]
                kd = op["kd"]
                wl = op["wl"]
                kills = op["kills"]
                badge_image = op["badge_image"]
                deaths = op["deaths"]
                experience = op["experience"]
                role = op["role"]
                wins = op["wins"]
                headshots = op["headshots"]
                losses = op["losses"]
                melee_kills = op["melee_kills"]
                playtime = op["playtime"]

        return OperatorResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            name=name,
            ctu=ctu,
            dbnos=dbnos,
            abilities=abilities,
            kd=kd,
            wl=wl,
            kills=kills,
            badge_image=badge_image,
            deaths=deaths,
            experience=experience,
            role=role,
            wins=wins,
            headshots=headshots,
            losses=losses,
            melee_kills=melee_kills,
            playtime=playtime
        )

    def get_weapon_stats(self, username, platform: Platform, weapon: str):

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/weapons',
                               headers=self.headers)
        weapon_name = None
        category = None
        kills = None
        deaths = None
        kd = None
        headshots = None
        headshot_percentage = None
        times_chosen = None
        bullets_fired = None
        bullets_hit = None

        content = json.loads(request.content)
        self.check_for_api_error(content)

        for weapons in content["weapons"]:
            if weapons["name"] == weapon:
                weapon_name = weapons["name"]
                category = weapons["category"]
                kills = weapons["kills"]
                deaths = weapons["deaths"]
                kd = weapons["kd"]
                headshots = weapons["headshots"]
                headshot_percentage = weapons["headshot_percentage"]
                times_chosen = weapons["times_chosen"]
                bullets_fired = weapons["bullets_fired"]
                bullets_hit = weapons["bullets_hit"]

        return WeaponResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            weapon_name=weapon_name,
            category=category,
            kills=kills,
            deaths=deaths,
            kd=kd,
            headshots=headshots,
            headshot_percentage=headshot_percentage,
            times_chosen=times_chosen,
            bullets_fired=bullets_fired,
            bullets_hit=bullets_hit
        )

    def get_weapon_category_stats(self, username, platform: Platform, category: str):

        request = requests.get(f'https://api2.r6stats.com/public-api/stats/{username}/{platform}/weapons',
                               headers=self.headers)
        category = None
        kills = None
        deaths = None
        kd = None
        headshots = None
        headshot_percentage = None
        times_chosen = None
        bullets_fired = None
        bullets_hit = None

        content = json.loads(request.content)
        self.check_for_api_error(content)

        for ca in content["categories"]:
            if ca["category"] == category:
                category = ca["category"]
                kills = ca["kills"]
                deaths = ca["deaths"]
                kd = ca["kd"]
                headshots = ca["headshots"]
                headshot_percentage = ca["headshot_percentage"]
                times_chosen = ca["times_chosen"]
                bullets_fired = ca["bullets_fired"]
                bullets_hit = ca["bullets_hit"]

        return WeaponCategoryResult(
            username=content["username"],
            platform=content["platform"],
            ubisoft_id=content["ubisoft_id"],
            uplay_id=content["uplay_id"],
            avatar_url=content["avatar_url_256"],
            last_updated=content["last_updated"],
            category=category,
            kills=kills,
            deaths=deaths,
            kd=kd,
            headshots=headshots,
            headshot_percentage=headshot_percentage,
            times_chosen=times_chosen,
            bullets_fired=bullets_fired,
            bullets_hit=bullets_hit
        )

    def check_for_api_error(self, response: dict):
        if "status" in list(response.keys()):
            if response["status"] == "error":
                raise ApiError(response["error"])

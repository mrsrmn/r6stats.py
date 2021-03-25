from .exceptions import OperatorNotFoundError

class Operators:
    sledge = "Sledge"
    thatcher = "Thatcher"
    ash = "Ash"
    thermite = "Thermite"
    twitch = "Twitch"
    montagne = "Montagne"
    glaz = "Glaz"
    fuze = "Fuze"
    blitz = "Blitz"
    iq = "IQ"
    buck = "Buck"
    blackbeard = "Blackbeard"
    capitao = "Capitão"
    hibana = "Hibana"
    jackal = "Jackal"
    ying = "Ying"
    zofia = "Zofia"
    dokkaebi = "Dokkaebi"
    lion = "Lion"
    finka = "Finka"
    maverick = "Maverick"
    nomad = "Nomad"
    gridlock = "Gridlock"
    nokk = "Nøkk"
    amaru = "Amaru"
    kali = "Kali"
    iana = "Iana"
    ace = "Ace"
    zero = "Zero"
    flores = "Flores"
    smoke = "Smoke"
    mute = "Mute"
    castle = "Castle"
    pulse = "Pulse"
    doc = "Doc"
    rook = "Rook"
    kapkan = "Kapkan"
    tachanka = "Tachanka"
    jager = "Jäger"
    bandit = "Bandit"
    frost = "Frost"
    valkyrie = "Valkyrie"
    caveira = "Caveira"
    echo = "Echo"
    mira = "Mira"
    lesion = "Lesion"
    ela = "Ela"
    vigil = "Vigil"
    alibi = "Alibi"
    maestro = "Maestro"
    clash = "Clash"
    kaid = "Kaid"
    mozzie = "Mozzie"
    warden = "Warden"
    goyo = "Goyo"
    wamai = "Wamai"
    oryx = "Oryx"
    melusi = "Melusi"
    aruni = "Aruni"

    operators = ["Sledge", "Thatcher", "Ash", "Thermite", "Twitch", "Montagne", "Glaz", "Fuze", "Blitz", "IQ", "Buck",
                 "Blackbeard", "Capitão", "Hibana", "Jackal", "Ying", "Zofia", "Dokkaebi", "Lion", "Finka", "Maverick",
                 "Nomad", "Gridlock", "Nøkk", "Amaru", "Kali", "Iana", "Ace", "Zero", "Flores", "Defenders", "Recruit",
                 "Smoke", "Mute", "Castle", "Pulse", "Doc", "Rook", "Kapkan", "Tachanka", "Jäger", "Bandit", "Frost",
                 "Valkyrie", "Caveira", "Echo", "Mira", "Lesion", "Ela", "Vigil", "Alibi", "Maestro", "Clash", "Kaid",
                 "Mozzie", "Warden", "Goyo", "Wamai", "Oryx", "Melusi", "Aruni"]

    @classmethod
    def search(cls, query: str):
        matches = []
        for op in cls.operators:
            if op.startswith(query.capitalize()):
                matches.append(op)

        if not len(matches):
            raise OperatorNotFoundError("Your operator search returned no results")
        elif len(matches) > 1:
            raise OperatorNotFoundError("Your operator search returned multiple results")

        return matches[0]

from typing import Literal


class Unificator:
    WEAPON_TYPES = {
        "Auto rifle": "Auto Rifle",
        "autogun": "Auto Rifle",
        "Melee-sword/blade": "Melee",
        "near_sword": "Melee",
        "Melee-electric saw": "Melee",
        "near_saw": "Melee",
        "pistol_fast": "Pistol",
        "Hand-cannon": "Heavy Pistol",
        "pistol_heavy": "Heavy Pistol",
        "Deploy-ancient weapon": "Deploy Ancient",
        "place_ancient": "Deploy Ancient",
        "Deploy-battery": "Deploy Battery",
        "place_battery": "Deploy Battery",
        "Deploy-dolly": "Deploy Dolly",
        "place_doll": "Deploy Dolly",
        "Deploy-trap dolly": "Deploy Trap",
        "place_induce": "Deploy Trap",
        "Deploy mine": "Deploy Mine",
        "place_mine": "Deploy Mine",
        "Deploy-special": "Deploy Special",
        "place_special": "Deploy Special",
        "Rocket launcher": "RPG",
        "rpg": "RPG",
        "Spread shotgun": " Spread Shotgun",
        "shotgun_multi": "Spread Shotgun",
        "Single shotgun": "Single Shotgun",
        "shotgun_single": "Single Shotgun",
        "Sniper rifle": "Sniper Rifle",
        "sniper": "Sniper Rifle",
        "special": "Special",
        "special_bow": "Bow",
        "spray": "Spray",
        "Activate": "Activate Spray",
        "spray_active": "Activate Spray",
        "Enchant": "Spray",
        "spray_enchanting": "Spray",
        "Switch": "Switch Spray",
        "spray_switch": "Switch Spray",
        "Thrown weapon": "Thrown",
        "throw": "Thrown",
        0: None,
    }

    DAMAGE_TYPES = {
        "1": "Physical",
        "2": "Fire",
        "3": "Ice",
        "4": "Energy",
        "5": "Light",
        "6": "Poison",
        "physic": "Physical",
        "pure": "Physical",
        "fire": "Fire",
        "snow": "Ice",
        "ice": "Ice",
        "power": "Energy",
        "light": "Light",
        "poison": "Poison",
        "none": None,
        "null": None,
        ";": None,
    }

    PROPERTIES = {
        "负重": "Cost",
        "重量": "Cost",
        "Carry Load": "Cost",
        "最大等级": "Max Lvl",
        "Max LV": "Max Lvl",
        "类型": "Type",
        "タイプ": "Type",
        "满级攻击力": "Max Lvl Damage",
        "攻撃力": "Max Lvl Damage",
        "MaxLv Attack": "Max Lvl Damage",
        "MaxLv Atk": "Max Lvl Damage",
        "满级载弹": "Max Lvl Ammo",
        "弾薬上限": "Max Lvl Ammo",
        "MaxLv Ammo": "Max Lvl Ammo",
        "满级攻速": "Max Lvl Atk Speed",
        "攻速": "Max Lvl Atk Speed",
        "MaxLv ASPD": "Max Lvl Atk Speed",
        "暴击率": "Crit Rate",
        "会心率": "Crit Rate",
        "弹道数": "Projectiles Num",
        "Shoot Line Num": "Projectiles Num",
        "满级存在时间": "Duration",
        "継続時間": "Duration",
        "存在上限": "Deploy Limit",
        "設置上限": "Deploy Limit",
        "满级生命": "Max Lvl HP",
        "HP": "Max Lvl HP",
        "MaxLv HP": "Max Lvl HP",
    }

    @classmethod
    def unificate_weapon_type(
        cls, weapon_type: str
    ) -> str | None | Literal["Unknown Weapon Type"]:
        return cls.WEAPON_TYPES.get(weapon_type, "Unknown Weapon Type")

    @classmethod
    def unificate_damage_type(
        cls, damage_type: str
    ) -> str | None | Literal["Unknown Damage Type"]:
        return cls.DAMAGE_TYPES.get(damage_type, "Unknown Damage Type")

    @classmethod
    def unificate_property(cls, property: str) -> str | Literal["Unknown Property"]:
        return cls.PROPERTIES.get(property, "Unknown Property")

class WeaponProcessor:
    def __init__(self, weapon_list_path):
        weapon_list = []
        with open(weapon_list_path, encoding='utf-8') as f:
            for line in f:
                weapon = line.strip()
                if weapon:
                    weapon_list.append(weapon)
        self.weapon_list = weapon_list


    def find_weapon(self, clean_text: str) -> str:

        text = ' '.join(clean_text.split())
        tokens = set(text.split())
        padded = f" {text} "

        for weapon in self.weapon_list:
            if ' ' in weapon:
                if f" {weapon} " in padded:
                    print(f"Found weapon: {weapon}")
                    return weapon
            else:
                if weapon in tokens:
                    print(f"Found weapon: {weapon}")
                    return weapon

        return ""

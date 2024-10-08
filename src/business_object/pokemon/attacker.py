from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Attacker(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.speed_current + self.attack_current) / 200
        return (multiplier)

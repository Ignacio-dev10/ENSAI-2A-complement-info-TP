from business_object.pokemon.abstract_pokemon import AbstractPokemon


class Defender(AbstractPokemon):
    def get_pokemon_attack_coef(self):
        multiplier = 1 + (self.attack_current + self.defense_current) / 200
        return (multiplier)

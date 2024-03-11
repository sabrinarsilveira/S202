from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def getPokemonsByType(self, types: list):
        return self.database.collection.find({"type": {"$in": types}})
    
    def getPokemonByName(self, name: str):
        return self.database.collection.find({"name": name})
    
    def getPokemonBySpawn(self, name: list):
        return self.database.collection.find({"spawn_chance": {"$gt": 0.3, "$lt": 0.6}})
    
    def getPokemonByOneWeaknesses(self, name: list):
        return self.database.collection.find({"weaknesses": {"$size": 1}})
    
    def getPokemonByWeaknesses(self, types: list):
        return self.database.collection.find({"weaknesses": {"$in": types}})


db = Database("pokedex", "pokemons")
pokedex = Pokedex(db)


types = ["Grass", "Poison"]
pokemons = pokedex.getPokemonsByType(types)
writeAJson(pokemons, "tipos")

pikachu = pokedex.getPokemonByName("Pikachu")
writeAJson(pikachu, "pikachu")

spawn = pokedex.getPokemonBySpawn(types)
writeAJson(spawn, "spawn")

umafraqueza = pokedex.getPokemonByOneWeaknesses(types)
writeAJson(umafraqueza, "umafraqueza")

types = ["Fire"]
fraquezas = pokedex.getPokemonByWeaknesses(types)
writeAJson(fraquezas, "fraquezas")


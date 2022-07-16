import json
class NeighborhoodPets:
    def __init__(self):
        self.petLibrary = {}


    def add_pet(self, name, species, owner):
        if name not in self.petLibrary.keys():
            self.petLibrary[name] = {"name": name,
                                    "species": species,
                                    "owner": owner}

    def delete_pet(self, name):
        if name in self.petLibrary.keys():
            self.petLibrary.pop(name)

    def get_owner(self, name):
        if name in self.petLibrary.keys():
            return self.petLibrary[name]["owner"]
        else:
            return "pet not present"

    def save_as_json(self, file_name):
        data = self.petLibrary
        with open(file_name, 'w') as outfile:
            json.dump(data, outfile)

    def read_json(self, file_name):
        with open(file_name) as json_file:
            self.petLibrary = json.load(json_file)

    def get_all_species(self):
        petSpecies = {pet["species"] for pet in self.petLibrary.values()}
        return petSpecies
#test lines
np = NeighborhoodPets()
np.add_pet("Fluffy", "gila monster", "Oksana")
np.add_pet("Tiny", "stegasaurus", "Rachel")
np.add_pet("Spot", "zebra", "Farrokh")
np.save_as_json("pets.json")
np.delete_pet("Tiny")
spot_owner = np.get_owner("Spot")
np.read_json("other_pets.json")
print(spot_owner)
species_set = np.get_all_species()
print(species_set)

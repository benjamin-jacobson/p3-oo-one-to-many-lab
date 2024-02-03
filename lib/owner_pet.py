class Owner:
    def __init__(self,name):
        self.name = name

    def pets(self):
        """returns a full list of the owner's pets."""
        return [p for p in Pet.all if p.owner == self] # checking Pet class object all if owner

    def add_pet(self, pet):
        """checks that the the pet is of type Pet and adds the owner to the pet."""
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet class")
        pet.owner = self # setting that pet to this owner

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name) #smarter than method below

    # def sort_pets_by_name(self):
    #     """returns a sorted list of pets by their names."""
    #     my_pets = [p.name for p in Pet.all if p.owner == self]
    #     return sorted(my_pets)

# class Pet:

#     PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

#     all = []
    
#     def __init__(self,name, pet_type, owner=None):
#         self.name = name
#         self.pet_type = pet_type
#         self.owner = owner
#         Pet.all.append(self) # instantiated Pet, adding instance to the all class attribute

#         @property
#         def pet_type(self):
#             return self._pet_type

#         @pet_type.setter
#         def pet_type(self, pet_type):
#             if pet_type not in self.PET_TYPES:
#                 raise Exception('Not a valid pet type.')
#                 #raise TypeError("Teacher must be an instance of Teacher class")
#             self._pet_type = pet_type

class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Not a valid pet type.')
        self._pet_type = pet_type

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Object is not of type Owner")
        self._owner = owner

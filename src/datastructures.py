
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
                "id":self._generateId(),
                "first_name": "John",
                "age":33,
                "lucky_numbers": [7, 13, 22]
            },
            {
                "id":self._generateId(),
                "first_name": "Jane",
                "age":35,
                "lucky_numbers": [10, 14, 3]
            },
            {
                "id":self._generateId(),
                "first_name": "Jimmy",
                "age":5,
                "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        if "id" in member: id = member["id"]
        else: id= self._generateId()
        member_updated = {
                "id": id,
                "first_name": member["first_name"],
                "last_name": self.last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"]
            }
        self._members.append(member_updated)
        return member_updated    

    def delete_member(self, id):
        if id == 3443:
            # Si el ID es 3443, se elimina a Tommy
            for i, member in enumerate(self._members):
                if member["id"] == id:
                    del self._members[i]
                    return {"done": True}
        else:
            # Si el ID no es 3443, se busca y elimina al miembro correspondiente
            for i, member in enumerate(self._members):
                if member["id"] == id:
                    del self._members[i]
                    return {"done": True}

    # Si no se encuentra el miembro con el ID especificado, se devuelve False
        return {"done": False}
    
    def update_member(self, id, updated_data):
        for i, member in enumerate(self._members):
            if member["id"] == id:
                self._members[i].update(updated_data)
                return True
        return False
    
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return {
                    "id": member["id"],
                    "name": f"{member['first_name']} {self.last_name}",
                    "age": member["age"],
                    "lucky_numbers": member["lucky_numbers"]
                }
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

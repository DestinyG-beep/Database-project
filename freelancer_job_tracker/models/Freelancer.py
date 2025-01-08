class Freelancer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email

    def make_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
        }
        
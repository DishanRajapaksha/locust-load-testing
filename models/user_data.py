class UserData:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str

    def __init__(self, id, email, first_name, last_name, avatar):
        self.id = id
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.avatar = avatar

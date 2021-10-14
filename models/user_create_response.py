class UserCreateResponse:
    name: str
    job: str
    id: str
    createdAt: str

    def __init__(self, name, job, id, createdAt):
        self.name = name
        self.id = id
        self.job = job
        self.createdAt = createdAt

from pydantic import BaseModel, ConfigDict


class ClientSchema(BaseModel):
    name: str
    cpf: int


class ClientPublic(BaseModel):
    id: int
    name: str
    cpf: int
    model_config = ConfigDict(from_attributes=True)


class ClientList(BaseModel):
    clients: list[ClientPublic]

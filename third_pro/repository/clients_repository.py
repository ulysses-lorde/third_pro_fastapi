from typing import Optional

from sqlalchemy.orm import Session
from sqlalchemy import select

from third_pro.schemas.clients_schemas import ClientPublic, ClientSchema, ClientList
from third_pro.db.tables.clients import Client
from third_pro.db.errors import EntityDoesNotExist, CPFAlreadyExists


class ClientRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_cpf(self, client_cpf: int):
        statement = select(Client).where(Client.cpf == client_cpf)
        return self.session.scalar(statement)
    
    def create(self, client: ClientSchema) -> ClientPublic:
        db_client = self.get_by_cpf(client.cpf)
        if db_client:
            raise CPFAlreadyExists('CPF already registered')

        new_client = Client(
            name=client.name,
            cpf=client.cpf
        )
        self.session.add(new_client)
        self.session.commit()
        self.session.refresh(new_client)

        return new_client

    def get(self, client_cpf: int) -> Optional[ClientPublic]:
        db_client = self.get_by_cpf(client_cpf)

        if db_client is None:
            raise EntityDoesNotExist
        
        return db_client
    
    def list(self, limit: int, offset: int):
        clients = self.session.scalars(select(Client).offset(offset).limit(limit)).all()

        return {'clients': clients}
    
    def update(self, client_cpf: int, client: ClientSchema):
        db_client = self.get_by_cpf(client_cpf)
        if db_client is None:
            raise EntityDoesNotExist
        
        for attr, value in client.model_dump().items():
            setattr(db_client, attr, value)
        
        self.session.commit()
        self.session.refresh(db_client)
    
    def delete(self, client_cpf: int):
        db_client = self.get_by_cpf(client_cpf)
        if db_client is None:
            raise EntityDoesNotExist
        
        self.session.delete(db_client)

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, Body, Query

from third_pro.api.dependencies.repositories import get_repository
from third_pro.schemas.clients_schemas import ClientPublic, ClientSchema, ClientList
from third_pro.schemas.messages import Message
from third_pro.repository.clients_repository import ClientRepository
from third_pro.db.errors import EntityDoesNotExist, CPFAlreadyExists

router = APIRouter(prefix='/clients', tags=['clients'])


@router.post('/', status_code=201, response_model=ClientPublic)
def create_client(
    client: ClientSchema = Body(...),
    repository: ClientRepository = Depends(get_repository(ClientRepository))
) -> ClientPublic:
    try:
        client = repository.create(client)
        return client
    
    except CPFAlreadyExists:
        raise HTTPException(status_code=400, detail='CPF aready registered')


@router.get(
    '/{client_cpf}',
    response_model=ClientPublic,
    status_code=200
)
def get_client(
    client_cpf: int,
    repository: ClientRepository = Depends(get_repository(ClientRepository))
) -> ClientPublic:
    try:
        client = repository.get(client_cpf=client_cpf)
        return client
    
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=404, detail="CPF of the non-registered customer"
        )


@router.get(
    '/',
    response_model=ClientList,
    status_code=200
)
def get_client_list(
    limit: int = Query(default=10, lte=100),
    offset: int = Query(default=0),
    repository: ClientRepository = Depends(get_repository(ClientRepository))
) -> Optional[ClientList]:
    return repository.list(limit=limit, offset=offset)


@router.put('/{client_cpf}', response_model=ClientPublic)
def update_client(
    client_cpf: int,
    client: ClientSchema,
    repository: ClientRepository = Depends(get_repository(ClientRepository))
):
    try:
        updated_client = repository.update(client_cpf=client_cpf, client=client)
        return updated_client
    
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=404, detail="CPF of the non-registered customer"
        )


@router.delete('/{client_cpf}', response_model=Message)
def delete_client(
    client_cpf: int,
    repository: ClientRepository = Depends(get_repository(ClientRepository))
):
    try:
        repository.delete(client_cpf)
        return {'detail': 'Client deleted'}
    
    except EntityDoesNotExist:
        raise HTTPException(
            status_code=404, detail="CPF of the non-registered customer"
        )

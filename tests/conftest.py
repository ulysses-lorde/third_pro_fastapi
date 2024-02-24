import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from third_pro.app import app
from third_pro.configs.base import Base
from third_pro.configs.session import get_session
from third_pro.configs.settings import Settings


@pytest.fixture
def session():
    engine = create_engine(Settings().DATABASE_URL)
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)
    with Session() as session:
        yield session
        session.rollback()

        Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def client_app(session):

    session.add(client_app)
    session.commit()
    session.refresh(client_app)

    return client_app


@pytest.fixture
def other_client_app(session):
    # client_app(id=2)

    session.add(client_app)
    session.commit()
    session.refresh(client_app)

    return client_app

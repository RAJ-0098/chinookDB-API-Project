import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import get_db
from tests.database_test import (
    get_sessionmaker,
    override_get_db
)
from tests.container_utils import (
    get_postgres_container
)
import tests.database_test as database_test
@pytest.fixture(scope="session")
def postgres_container():

    container = get_postgres_container()

    yield container
@pytest.fixture(scope="session")
def test_sessionmaker(postgres_container):

    url = postgres_container.get_connection_url()

    session_maker = get_sessionmaker(url)

    database_test._test_session_maker = session_maker

    return session_maker
@pytest.fixture(scope="module")
def client(test_sessionmaker):

    app.dependency_overrides[get_db] = override_get_db

    with TestClient(app) as c:

        yield c
    app.dependency_overrides.clear()
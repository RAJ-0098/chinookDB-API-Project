from testcontainers.postgres import PostgresContainer


_container = None


def get_postgres_container():

    global _container

    if _container is None:

        _container = PostgresContainer(
            "postgres:15"
        )

        _container.start()

    return _container
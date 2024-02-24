import factory
import factory.fuzzy

from third_pro.db.tables.clients import Client


class ClientFactory(factory.factory):
    class Meta:
        model = Client

    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda obj: f'{obj.name}')
    cpf = factory.LazyAttribute(lambda obj: f'{obj.name}@test.com')

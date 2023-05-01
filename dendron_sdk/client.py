# This file was auto-generated by Fern from our API Definition.

from backports.cached_property import cached_property

from .environment import FernApiEnvironment
from .resources.dendron.client import AsyncDendronClient, DendronClient
from .resources.imdb.client import AsyncImdbClient, ImdbClient


class FernApi:
    def __init__(self, *, environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION):
        self._environment = environment

    @cached_property
    def dendron(self) -> DendronClient:
        return DendronClient(environment=self._environment)

    @cached_property
    def imdb(self) -> ImdbClient:
        return ImdbClient(environment=self._environment)


class AsyncFernApi:
    def __init__(self, *, environment: FernApiEnvironment = FernApiEnvironment.PRODUCTION):
        self._environment = environment

    @cached_property
    def dendron(self) -> AsyncDendronClient:
        return AsyncDendronClient(environment=self._environment)

    @cached_property
    def imdb(self) -> AsyncImdbClient:
        return AsyncImdbClient(environment=self._environment)

from pprint import pprint

from tests.async_tonapi import TestAsyncTonapi

ACCOUNTS_IDS = ["-1:5555555555555555555555555555555555555555555555555555555555555555"]


async def handler(event) -> None:
    pprint(event)


class TestSSEMethod(TestAsyncTonapi):

    async def test_subscribe_to_transactions(self):
        await self.tonapi.websocket.subscribe_to_transactions(ACCOUNTS_IDS, handler)

    async def test_subscribe_to_traces(self):
        await self.tonapi.websocket.subscribe_to_traces(ACCOUNTS_IDS, handler)

    async def test_subscribe_to_mempool(self):
        await self.tonapi.websocket.subscribe_to_mempool(ACCOUNTS_IDS, handler)
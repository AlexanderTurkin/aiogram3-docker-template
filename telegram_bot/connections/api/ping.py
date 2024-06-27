from connections.base import BaseClient


class PingPong(BaseClient):
    def __init__(self, **kwargs):
        self.base_url = "http://fastapi:8000"
        super().__init__(base_url=self.base_url)

    async def get_ping(self):
        response = await self._make_request(
            endpoint=f'/ping',
            method='get'
        )

        if response[0] == 200:
            return response[1]['message']
        else:
            raise Exception(response[1])
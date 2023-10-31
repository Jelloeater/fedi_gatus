import logging
import os

import uvicorn
from fastapi import FastAPI
from starlette import status
from starlette.responses import RedirectResponse

if os.getenv("LOG_LEVEL") is None:
    logging.basicConfig(level=logging.WARNING)
else:
    logging.basicConfig(level=int(os.getenv("LOG_LEVEL")))


class web_app:
    def __init__(self):
        self.app = FastAPI(debug=True)
        # TODO Add rate limit in Caddy
        # TODO Add auth option for tokenhttps://www.freecodecamp.org/news/how-to-add-jwt-authentication-in-fastapi/

        @self.app.get("/", include_in_schema=False)
        async def root():
            return RedirectResponse(self.app.docs_url)

        @self.app.get(
            "/healthcheck",  # For AutoDocs
            responses={
                status.HTTP_200_OK: {"description": "Connection to DB OK"},
                status.HTTP_503_SERVICE_UNAVAILABLE: {
                    "description": "Cannot connect DB",
                },
            },
        )
        async def healthcheck():
            pass
            # TODO Write health check endpoint
        #TODO Add top instance query function and JSON return

class Server:
    port = 8888

    @classmethod
    def local_nic(cls):
        import socket

        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        nic = s.getsockname()[0]
        s.close()
        return nic

    @classmethod
    def start_server(cls):  # pragma: no cover # TODO Remove when test fixed
        u = uvicorn
        c = u.config.Config(
            app=web_app().app,
            host=cls.local_nic(),
            port=cls.port,
            proxy_headers=True,
            # root_path="/api/v1"
        )
        w = u.Server(c)
        w.run()


if __name__ == "__main__":
    logging.info("Starting API Server")
    Server().start_server()

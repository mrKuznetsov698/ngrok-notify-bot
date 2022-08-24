import ngrok

TUNNEL_OPENED = 1
TUNNEL_CLOSED = 2


class NewEvent:
    def __init__(self, event_type: int, tunnel: ngrok.client.Tunnel):
        self._event_type: int = event_type
        self._tunnel: ngrok.client.Tunnel = tunnel

    def get_type(self) -> int:
        return self._event_type

    def get_tunnel(self) -> ngrok.client.Tunnel:
        return self._tunnel

from bascenev1 import SessionPlayer

class ServerPlayer:
    def __init__(
            self,
            account_id: str,
            account_name: str,
            sessionplayer: SessionPlayer = None,
            kills: int = 0,
            deaths: int = 0
    ):
        self.account_id = account_id
        self.account_name = account_name
        self.sessionplayer = sessionplayer
        self.kills = kills
        self.deaths = deaths
        self._dirty = False
    
    def add_kill(self) -> None:
        self.kills += 1
    
    def add_death(self) -> None:
        self.deaths += 1
    
    def __repr__(self):
        return f"<ServerPlayer(account_id=\"{self.account_id}\", account_name=\"{self.account_name}\", sessionplayer={self.sessionplayer}, kills={self.kills}, deaths={self.deaths})>"
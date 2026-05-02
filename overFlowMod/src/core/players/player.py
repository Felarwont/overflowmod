from bascenev1 import SessionPlayer

class ServerPlayer:
    def __init__(
            self,
            account_id: str,
            account_name: str,
            sessionplayer: SessionPlayer | None = None,
            kills: int = 0,
            deaths: int = 0
    ):
        self._account_id = account_id
        self.account_name = account_name
        self.sessionplayer = sessionplayer
        self.kills = kills
        self.deaths = deaths
        self._dirty = False
    
    def get_account_id(self) -> str:
        return self._account_id

    def add_kill(self) -> None:
        self.kills += 1
        self._dirty = True
    
    def add_death(self) -> None:
        self.deaths += 1
        self._dirty = True
    
    def __repr__(self):
        return f"<ServerPlayer(account_id=\"{self._account_id}\", account_name=\"{self.account_name}\", sessionplayer={self.sessionplayer}, kills={self.kills}, deaths={self.deaths})>"
from core.players.player import ServerPlayer

class PlayerManager:
    def __init__(self):
        self._serverplayers: dict[str, ServerPlayer] = dict()
    
    def all(self):
        return self._serverplayers.copy()

    def add(self, serverplayer: ServerPlayer) -> ServerPlayer:
        self._serverplayers[serverplayer._account_id] = serverplayer
        
        return serverplayer

    def remove(self, serverplayer: ServerPlayer) -> None:
        self._serverplayers.pop(serverplayer._account_id)
    
    def get(self, account_id: str) -> ServerPlayer | None:
        return self._serverplayers.get(account_id)
    
    def update_player_data(self, new_serverplayer: ServerPlayer) -> None:
        if new_serverplayer._account_id not in self._serverplayers:
            return

        self._serverplayers[new_serverplayer._account_id] = new_serverplayer
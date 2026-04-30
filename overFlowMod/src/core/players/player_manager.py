from core.players.player import ServerPlayer

class PlayerManager:
    def __init__(self):
        self.serverplayers: dict[str, ServerPlayer] = dict()
    
    def add(self, serverplayer: ServerPlayer) -> None:
        self.serverplayers[serverplayer.account_id] = serverplayer

    def remove(self, serverplayer: ServerPlayer) -> None:
        self.serverplayers.pop(serverplayer.account_id)
    
    def get_by_account_id(self, account_id: str) -> ServerPlayer | None:
        return self.serverplayers.get(account_id)
    
    def update_player_data(self, new_serverplayer: ServerPlayer) -> None:
        if new_serverplayer.account_id not in self.serverplayers:
            return

        self.serverplayers[new_serverplayer.account_id] = new_serverplayer
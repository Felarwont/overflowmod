from core.players.player import ServerPlayer

class PlayerManager:
    def __init__(self):
        self.__serverplayers: dict[str, ServerPlayer] = dict()
    
    def get_serverplayers(self):
        return self.__serverplayers.copy()

    def add(self, serverplayer: ServerPlayer) -> ServerPlayer:
        self.__serverplayers[serverplayer.account_id] = serverplayer
        
        return serverplayer

    def remove(self, serverplayer: ServerPlayer) -> None:
        self.__serverplayers.pop(serverplayer.account_id)
    
    def get(self, account_id: str) -> ServerPlayer | None:
        return self.__serverplayers.get(account_id)
    
    def update_player_data(self, new_serverplayer: ServerPlayer) -> None:
        if new_serverplayer.account_id not in self.__serverplayers:
            return

        self.__serverplayers[new_serverplayer.account_id] = new_serverplayer
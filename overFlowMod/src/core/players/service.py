import logging

from core.players.repository import PlayerRepository
from core.players.manager import PlayerManager
from core.players.player import ServerPlayer
from game.session.roster import PlayerSpec

logger = logging.getLogger(f"overflowmod.{__name__}")

class PlayerService:
    def __init__(
            self,
            manager: PlayerManager,
            repository: PlayerRepository
    ):
        self.manager = manager
        self.repository = repository
    
    def from_spec(self, player_spec: PlayerSpec):
        return ServerPlayer(
            account_id=player_spec.account_id,
            account_name=player_spec.account_name
        )
    
    def get(self, account_id: str, use_db: bool = False) -> ServerPlayer | None:
        player = self.manager.get(account_id)
        if player:
            logger.info("LOAD player data from cache")
            return player
        
        if use_db:
            player = self.repository.get(account_id)
            if player:
                logger.info("LOAD player data from database")
                return player

        return None

    def add_to_db(self, serverplayer: ServerPlayer) -> ServerPlayer:
        return self.repository.create(serverplayer)
    
    def add_to_cache(self, serverplayer: ServerPlayer) -> ServerPlayer:
        return self.manager.add(serverplayer)
    
    def remove_from_cache(self, serverplayer: ServerPlayer) -> None:
        self.manager.remove(serverplayer)
from typing import Callable

from core.players.player_repository import PlayerRepository
from core.players.player_manager import PlayerManager
from game.session import roster

class EventSystem:
    def __init__(
            self,
            player_repository: PlayerRepository,
            player_manager: PlayerManager,
            on_connect: Callable[[str], None],
            on_disconnect: Callable[[str], None]
    ):
        self.player_repository = player_repository
        self.player_manager = player_manager
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect
        self.old_acc_ids = set()
    
    def update(self) -> None:
        current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

        joined = current_acc_ids.difference(self.old_acc_ids)
        left = self.old_acc_ids.difference(current_acc_ids)

        for account_id in joined:
            player = self.player_repository.get_or_create(account_id)
            self.on_connect(player)
        
        for account_id in left:
            player = self.player_manager.get_by_account_id(account_id)
            self.on_disconnect(player)
        
        self.old_acc_ids = current_acc_ids
from typing import Callable

from core.players.service import PlayerService
from game.session import roster

class EventSystem:
    def __init__(
            self,
            player_service: PlayerService,
            on_connect: Callable[[str], None],
            on_disconnect: Callable[[str], None]
    ):
        self.player_service = player_service
        self.on_connect = on_connect
        self.on_disconnect = on_disconnect
        self.old_acc_ids = set()
    
    def update(self) -> None:
        current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

        joined = current_acc_ids.difference(self.old_acc_ids)
        left = self.old_acc_ids.difference(current_acc_ids)

        for account_id in joined:
            player = self.player_service.get(account_id, use_db=True)
            if not player:
                server_player = self.player_service.from_spec(roster.get_player_spec(account_id))
                player = self.player_service.add_to_db(server_player)

            self.on_connect(player)
        
        for account_id in left:
            player = self.player_service.get(account_id)
            self.on_disconnect(player)
        
        self.old_acc_ids = current_acc_ids
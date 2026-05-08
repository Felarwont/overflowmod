from core.events.types import PlayerConnectEvent, PlayerDisconnectEvent
from core.app import updater, events, player_service
from game.session import roster

old_account_ids = set()

@updater.every(delta=0.5)
def check_lifecycle() -> None:
    global old_account_ids

    current_acc_ids = {player_spec.account_id for player_spec in roster.get_players_spec()}

    joined = current_acc_ids.difference(old_account_ids)
    left = old_account_ids.difference(current_acc_ids)

    for account_id in joined:
        player = player_service.get(account_id, use_db=True)
        if not player:
            server_player = player_service.from_spec(roster.get_player_spec(account_id))
            player = player_service.add_to_db(server_player)

        events.emit(PlayerConnectEvent(player=player))
    
    for account_id in left:
        player = player_service.get(account_id)
        events.emit(PlayerDisconnectEvent(player=player))
    
    old_account_ids = current_acc_ids
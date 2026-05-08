import logging

from core.events.types import PlayerConnectEvent, PlayerDisconnectEvent
from core.app import events, player_service

logger = logging.getLogger(f"overflowmod.{__name__}")

@events.subscribe(PlayerConnectEvent)
def on_player_connect(event: PlayerConnectEvent) -> None:
    player_service.add_to_cache(event.player)

    logger.info(f"JOIN {event.player.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.all()}")

@events.subscribe(PlayerDisconnectEvent)
def on_player_disconnect(event: PlayerDisconnectEvent) -> None:
    player_service.remove_from_cache(event.player)
    player_service.save_in_db(event.player)

    logger.info(f"LEFT {event.player.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.all()}")
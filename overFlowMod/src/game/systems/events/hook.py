import logging

from bascenev1 import Player

from core.players.player import ServerPlayer
from core.app import player_service

logger = logging.getLogger(f"overflowmod.{__name__}")

def on_player_connect(serverplayer: ServerPlayer) -> None:
    player_service.add_to_cache(serverplayer)
    logger.info(f"JOIN {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.all()}")

def on_player_disconnect(serverplayer: ServerPlayer) -> None:
    player_service.remove_from_cache(serverplayer)
    player_service.save_in_db(serverplayer)
    logger.info(f"LEFT {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.all()}")

def on_player_death(player: Player, killer: Player | None) -> None:
    server_player = player_service.get(player.sessionplayer.get_account_id())
    server_player.add_death()
    logger.debug(server_player)
    if killer and killer is not player:
        server_killer = player_service.get(killer.sessionplayer.get_account_id())
        server_killer.add_kill()
        logger.debug(server_killer)
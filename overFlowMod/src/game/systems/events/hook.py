import logging

from core.players.player import ServerPlayer
from core.app import player_service

logger = logging.getLogger(f"overflowmod.{__name__}")

def on_player_connect(serverplayer: ServerPlayer):
    player_service.add_to_cache(serverplayer)
    logger.info(f"JOIN {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.get_serverplayers()}")

def on_player_disconnect(serverplayer: ServerPlayer):
    player_service.remove_from_cache(serverplayer)
    logger.info(f"LEFT {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_service.manager.get_serverplayers()}")
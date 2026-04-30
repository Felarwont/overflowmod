import logging

from core.players.player import ServerPlayer
from core.app import player_manager

logger = logging.getLogger(f"overflowmod.{__name__}")

def on_player_connect(serverplayer: ServerPlayer):
    player_manager.add(serverplayer)
    logger.info(f"JOIN {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_manager.serverplayers}")

def on_player_disconnect(serverplayer: ServerPlayer):
    player_manager.remove(serverplayer)
    logger.info(f"LEFT {serverplayer.account_name}")
    logger.debug(f"SERVERPLAYERS {player_manager.serverplayers}")
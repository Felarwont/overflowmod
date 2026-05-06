import logging

from bascenev1 import Player

from core.players.player import ServerPlayer
from game.systems.ranking import calc_score
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
    serverplayer = player_service.get(player.sessionplayer.get_account_id())
    serverplayer.add_death()
    serverplayer.score = calc_score(serverplayer)
    logger.debug(serverplayer)
    if killer and killer is not player:
        serverkiller = player_service.get(killer.sessionplayer.get_account_id())
        serverkiller.add_kill()
        serverkiller.score = calc_score(serverkiller)
        logger.debug(serverkiller)
import logging

from core.events.types import PlayerDiedEvent
from game.systems.ranking import calc_score
from core.app import events

logger = logging.getLogger(f"overflowmod.{__name__}")

@events.subscribe(PlayerDiedEvent)
def update_stats(event: PlayerDiedEvent) -> None:
    event.player.add_death()
    event.player.score = calc_score(event.player)
    
    logger.debug(event.player)
    if event.killer:
        event.killer.add_kill()
        event.killer.score = calc_score(event.killer)

        logger.debug(event.killer)
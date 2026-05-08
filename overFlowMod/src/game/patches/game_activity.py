import logging

from bascenev1 import GameActivity
from bascenev1 import PlayerDiedMessage

from core.events.types import PlayerDiedEvent
from core.app import events, player_service

logger = logging.getLogger(f"overflowmod.{__name__}")

old_handlemessage = GameActivity.handlemessage
def new_handlemessage(self, msg):
    if isinstance(msg, PlayerDiedMessage):
        # pylint: disable=cyclic-import
        from bascenev1lib.actor.spaz import Spaz

        player = msg.getplayer(self.playertype)
        killer = msg.getkillerplayer(self.playertype)

        serverplayer = player_service.get(player.sessionplayer.get_account_id())
        serverkiller = None
        if killer and killer is not player:
            serverkiller = player_service.get(killer.sessionplayer.get_account_id())

        events.emit(PlayerDiedEvent(player=serverplayer, killer=serverkiller))

        self.stats.player_was_killed(
            player, killed=msg.killed, killer=killer
        )
        if killer and killer.team is not player.team:
            assert isinstance(killer.actor, Spaz)
            pts, importance = killer.actor.get_death_points(msg.how)
            if not self.has_ended():
                self.stats.player_scored(
                    killer,
                    pts,
                    kill=True,
                    victim_player=player,
                    importance=importance,
                    showpoints=self.show_kill_points,
                )
            

    else:
        return old_handlemessage(self, msg)
    return None

def apply_game_activity_patches():
    GameActivity.handlemessage = new_handlemessage
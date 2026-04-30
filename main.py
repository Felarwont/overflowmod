# ba_meta require api 9
import babase

from overFlowMod.src.core.bootstrap import environment

def main(self):
    import logging

    from game.systems.events.engine import EventSystem
    from core.app import player_manager, player_repo
    from core.db.connection import engine, Base
    from game.systems.events import hook
    from game import patches

    logger = logging.getLogger(f"overflowmod.{__name__}")

    Base.metadata.create_all(engine)
    logger.info("База данных готова")

    event_system_ = EventSystem(
        player_repository=player_repo,
        player_manager=player_manager,
        on_connect=hook.on_player_connect,
        on_disconnect=hook.on_player_disconnect
    )
    self.timer = babase.AppTimer(0.5, event_system_.update, True)

    patches.apply_all()

# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        environment.setup_runtime()
        environment.setup_logger()
        main(self)
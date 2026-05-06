# ba_meta require api 9
import babase

from overFlowMod.src.core.bootstrap import environment

def main(self):
    import logging

    from game.systems.events.engine import EventSystem
    from core.db.connection import engine, Base
    from game.systems.events import hooks
    from core.app import player_service
    from game import patches

    logger = logging.getLogger(f"overflowmod.{__name__}")

    Base.metadata.create_all(engine)
    logger.info("База данных готова")

    event_system = EventSystem(
        player_service=player_service,
        on_connect=hooks.on_player_connect,
        on_disconnect=hooks.on_player_disconnect
    )
    self.timer = babase.AppTimer(0.5, event_system.update, True)

    patches.apply_all()

# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        environment.setup_runtime()
        environment.setup_logger()
        main(self)
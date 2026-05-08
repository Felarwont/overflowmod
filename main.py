# ba_meta require api 9
import babase

from overFlowMod.src.core import bootstrap

def main(self):
    import logging

    from core.db.connection import engine, Base
    from core.app import updater
    from game import patches

    logger = logging.getLogger(f"overflowmod.{__name__}")

    Base.metadata.create_all(engine)
    logger.info("База данных готова")

    self.timer = babase.AppTimer(0.5, updater.update, True)

    patches.apply_all()

# ba_meta export babase.Plugin
class OverFlowMod(babase.Plugin):
    def on_app_running(self):
        bootstrap.env.setup_runtime()
        bootstrap.env.setup_logger()
        bootstrap.apply_handlers()
        bootstrap.apply_updaters()
        main(self)
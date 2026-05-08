from core.players.repository import PlayerRepository
from core.players.manager import PlayerManager
from game.systems.players.service import PlayerService
from core.db.connection import SessionLocal
from core.events.engine import EventSystem
from game.systems.updater import Updater

player_repo = PlayerRepository(SessionLocal)
player_manager = PlayerManager()

player_service = PlayerService(
    manager=player_manager,
    repository=player_repo
)

events = EventSystem()

updater = Updater()
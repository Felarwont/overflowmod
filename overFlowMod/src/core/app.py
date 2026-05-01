from core.players.repository import PlayerRepository
from core.players.manager import PlayerManager
from core.players.service import PlayerService
from core.db.connection import SessionLocal

player_repo = PlayerRepository(SessionLocal)
player_manager = PlayerManager()

player_service = PlayerService(
    manager=player_manager,
    repository=player_repo
)
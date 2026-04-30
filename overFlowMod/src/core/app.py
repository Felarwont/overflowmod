from core.players.player_repository import PlayerRepository
from core.players.player_manager import PlayerManager
from core.db.connection import SessionLocal

player_repo = PlayerRepository(SessionLocal)
player_manager = PlayerManager()
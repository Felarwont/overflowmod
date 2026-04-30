import logging

from sqlalchemy.orm import sessionmaker

from core.players.player import ServerPlayer
from core.db.models import PlayerModel
from game.session import roster

logger = logging.getLogger(f"overflowmod.{__name__}")

class PlayerRepository:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
    
    def get_or_create(self, account_id: str) -> ServerPlayer:
        with self.session_factory() as session:
            player = session.query(PlayerModel).filter_by(account_id=account_id).first()
            if player:
                logger.info("LOAD player from databse")

            if not player:
                p_spec = roster.get_player_spec(account_id)
                player = PlayerModel(
                    account_id=p_spec.account_id,
                    account_name=p_spec.account_name
                )
                session.add(player)
                session.commit()
                logger.info("CREATE player in database")

            return ServerPlayer(
                account_id=player.account_id,
                account_name=player.account_name,
                kills=player.kills,
                deaths=player.deaths
            )
    
    def save(self, player: ServerPlayer) -> None: # Обновление данных игрока в базе данных
        pass
import logging

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from core.players.player import ServerPlayer
from core.db.models import PlayerModel

logger = logging.getLogger(f"overflowmod.{__name__}")

class PlayerRepository:
    def __init__(self, session_factory: sessionmaker):
        self.session_factory = session_factory
    
    def get(self, account_id: str) -> ServerPlayer | None:
        with self.session_factory() as session:
            player = session.query(PlayerModel).filter_by(account_id=account_id).first()
            if not player:
                return
            
            return ServerPlayer(
                account_id=player.account_id,
                account_name=player.account_name,
                kills=player.kills,
                deaths=player.deaths
            )
    
    def create(self, serverplayer: ServerPlayer) -> ServerPlayer:
        with self.session_factory() as session:
            player = PlayerModel(
                account_id=serverplayer.account_id,
                account_name=serverplayer.account_name
            )

            try:
                session.add(player)
                session.commit()
                logger.info("CREATE player in database")
            except IntegrityError:
                session.rollback()
            
            return serverplayer
    
    def save(self, player: ServerPlayer) -> None: # Обновление данных игрока в базе данных
        pass
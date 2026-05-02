import logging

from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

from core.players.player import ServerPlayer
from core.db.models import PlayerModel

logger = logging.getLogger(f"overflowmod.{__name__}")

class PlayerRepository:
    def __init__(self, session_factory: sessionmaker[Session]):
        self.session_factory = session_factory
    
    def get(self, account_id: str) -> ServerPlayer | None:
        with self.session_factory() as session:
            db_player = session.get(PlayerModel, account_id)
            if not db_player:
                return
            
            return ServerPlayer(
                account_id=db_player.account_id,
                account_name=db_player.account_name,
                kills=db_player.kills,
                deaths=db_player.deaths
            )
    
    def create(self, serverplayer: ServerPlayer) -> ServerPlayer:
        with self.session_factory() as session:
            player = PlayerModel(
                account_id=serverplayer.get_account_id(),
                account_name=serverplayer.account_name
            )

            try:
                session.add(player)
                session.commit()
                logger.info("CREATE player in database")
            except IntegrityError:
                session.rollback()
            
            return serverplayer
    
    def save(self, serverplayer: ServerPlayer) -> None: # Обновление данных игрока в базе данных
        with self.session_factory() as session:
            db_player = session.get(PlayerModel, serverplayer.get_account_id())
            if not db_player:
                return
            
            db_player.account_name = serverplayer.account_name
            db_player.kills = serverplayer.kills
            db_player.deaths = serverplayer.deaths

            session.commit()

            logger.info("SAVE player data in database")
    
    def save_all(self, serverplayers: dict[str, ServerPlayer]) -> None:
        with self.session_factory() as session:
            for account_id, serverplayer in serverplayers.items():
                db_player = session.get(PlayerModel, account_id)
                if not db_player:
                    return
                
                db_player.account_name = serverplayer.account_name
                db_player.kills = serverplayer.kills
                db_player.deaths = serverplayer.deaths

                session.commit()
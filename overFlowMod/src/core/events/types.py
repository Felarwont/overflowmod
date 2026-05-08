from core.players.player import ServerPlayer
from dataclasses import dataclass

class Event:
    pass

@dataclass(slots=True, frozen=True)
class PlayerConnectEvent(Event):
    player: ServerPlayer

@dataclass(slots=True, frozen=True)
class PlayerDisconnectEvent(Event):
    player: ServerPlayer

@dataclass(slots=True, frozen=True)
class PlayerDiedEvent(Event):
    player: ServerPlayer
    killer: ServerPlayer | None
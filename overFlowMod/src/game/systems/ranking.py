import math

from core.players.player import ServerPlayer

def calc_score(player: ServerPlayer) -> int:
    return math.floor(player.kills / (player.deaths + 1) * math.log(player.kills + player.deaths + 1))
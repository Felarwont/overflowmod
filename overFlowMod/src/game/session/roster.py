import json
from dataclasses import dataclass

from bascenev1 import get_game_roster

@dataclass
class PlayerSpec:
    account_id: str
    account_name: str
    client_id: int

def get_player_spec(account_id: str) -> PlayerSpec | None:
    for client in get_game_roster():
        if client['client_id'] == -1:
            continue

        if client['account_id'] == account_id:
            spec_string = json.loads(client['spec_string'])

            return PlayerSpec(
                account_id=client['account_id'],
                account_name=spec_string.get("n"),
                client_id=client.get("client_id")
            )

    return None

def get_players_spec() -> list[PlayerSpec]:
    result = []
    for client in get_game_roster():
        if (client['client_id'] != -1) and (client['account_id'] is not None):
            result.append(get_player_spec(client['account_id']))

    return result
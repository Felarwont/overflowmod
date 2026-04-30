from bascenev1 import Session, broadcastmessage

from core.app import player_manager

old_on_player_request = Session.on_player_request
def new_on_player_request(self, sessionplayer):
    serverplayer = player_manager.get_by_account_id(sessionplayer.get_account_id())
    if not serverplayer:
        broadcastmessage("Загрузка данных...", clients=[sessionplayer.inputdevice.client_id], transient=True, color=(1.0, 0.5, 0.5))
        return False
    serverplayer.sessionplayer = sessionplayer

    return old_on_player_request(self, sessionplayer)

old_on_player_leave = Session.on_player_leave
def new_on_player_leave(self, sessionplayer):
    old_on_player_leave(self, sessionplayer)
    serverplayer = player_manager.get_by_account_id(sessionplayer.get_account_id())
    if not serverplayer:
        return
    serverplayer.sessionplayer = None

def apply_session_patches():
    Session.on_player_request = new_on_player_request
    Session.on_player_leave = new_on_player_leave
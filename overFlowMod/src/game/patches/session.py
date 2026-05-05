from bascenev1 import Session, broadcastmessage

from core.app import player_service

old_on_player_request = Session.on_player_request
def new_on_player_request(self, sessionplayer):
    if not old_on_player_request(self, sessionplayer):
        return False

    serverplayer = player_service.get(sessionplayer.get_account_id())
    if not serverplayer:
        broadcastmessage("Загрузка данных...", clients=[sessionplayer.inputdevice.client_id], color=(1.0, 0.5, 0.5), transient=True)
        return False
    
    for s_player in self.sessionplayers:
        if s_player.get_account_id() == sessionplayer.get_account_id():
            broadcastmessage("Вы уже вошли с этого аккаунта", clients=[sessionplayer.inputdevice.client_id], color=(1.0, 1.0, 0.5), transient=True)
            return False

    serverplayer.sessionplayer = sessionplayer

    return True

old_on_player_leave = Session.on_player_leave
def new_on_player_leave(self, sessionplayer):
    old_on_player_leave(self, sessionplayer)
    serverplayer = player_service.get(sessionplayer.get_account_id())
    if not serverplayer:
        return

    serverplayer.sessionplayer = None

def apply_session_patches():
    Session.on_player_request = new_on_player_request
    Session.on_player_leave = new_on_player_leave
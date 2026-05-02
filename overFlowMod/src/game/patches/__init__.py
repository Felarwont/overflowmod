from .session import apply_session_patches
from .game_activity import apply_game_activity_patches

def apply_all():
    apply_session_patches()
    apply_game_activity_patches()
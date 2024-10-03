from dataclass_wizard import JSONWizard
from dataclasses import dataclass, field
from ..constants.scLiterals import *
from .trackSchemes import scTrack
from .playlistSchemes import scPlaylistBase
from .userSchemes import scUserMini

@dataclass
class scLikedTrack(JSONWizard):
    created_at  : str
    kind        : scLikeKind
    track       : scTrack

@dataclass
class scLikedPlaylist(JSONWizard):
    created_at  : str
    kind        : scLikeKind
    playlist    : scPlaylistBase
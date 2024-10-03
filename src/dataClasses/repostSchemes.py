from dataclass_wizard import JSONWizard
from dataclasses import dataclass, field
from ..constants.scLiterals import *
from .trackSchemes import scTrack
from .playlistSchemes import scPlaylist
from .userSchemes import scUserMini

@dataclass
class scRepost(JSONWizard):
    created_at  : str
    user        : scUserMini
    uuid        : str
    caption     : str | None

@dataclass
class scTrackRepost(JSONWizard, scRepost):
    type    : scTrackRepostKind
    track   : scTrack

@dataclass
class scPlaylistRepost(JSONWizard, scRepost):
    type        : scPlaylistRepostKind
    playlist    : scPlaylist
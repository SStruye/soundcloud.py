from dataclass_wizard import JSONWizard
from dataclasses import dataclass, field
from ..constants.scLiterals import *
from .commonSchemes import *
from .userSchemes import *
from .trackSchemes import *

@dataclass
class scPlaylistBase(JSONWizard):
    artwork_url         : str
    created_at          : str
    duration            : int
    id                  : int
    kind                : scPlaylistKind
    last_modified       : str
    likes_count         : int
    managed_by_feeds    : bool
    permalink           : str
    permalink_url       : str
    public              : bool
    release_date        : str | None
    reposts_count       : int
    secret_token        : str | None
    sharing             : scSharing
    title               : str
    uri                 : str
    user_id             : int
    set_type            : str | None
    is_album            : bool
    published_at        : str
    display_date        : str
    user                : scUserMini
    track_count         : int

@dataclass
class scPlaylist(JSONWizard):
    description     : str
    embeddable_by   : scEmbeddableBy
    genre           : str
    label_name      : str | None
    license         : scLicense
    purchase_title  : str | None
    purchase_url    : str | None
    tag_list        : str | None
    tracks          : list = field(default_factory=list)

    def __post_init__(self):
        self.tracks = [self._try_create_track(tracks) for tracks in self.tracks]

    def _try_create_track(self, track_data):
        try:
            return scTrack(**track_data)
        except:
            return scTrackMini(**track_data)
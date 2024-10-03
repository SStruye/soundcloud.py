from dataclass_wizard import JSONWizard
from dataclasses import dataclass
from ..constants.scLiterals import *
from .commonSchemes import scVisuals
from .userSchemes import scUserMini

@dataclass
class scPublisherMetaData:
    id                  : str
    urn                 : str
    album_title         : str  = None
    contains_music      : bool = None
    isrc                : str  = None
    release_title       : str  = None
    artist              : str  = None
    upc_or_ean          : str  = None
    explicit            : bool = None
    c_line_for_display  : str  = None
    p_line              : str  = None
    p_line_for_display  : str  = None
    c_line              : str  = None



@dataclass
class scTranscodingFormat:
    protocol    : scTranscodingFormatProtocol
    mime_type   : scTranscodingFormatMimeType

@dataclass
class scTranscoding(JSONWizard):
    duration    : int
    format      : scTranscodingFormat
    preset      : scTranscodingPreset
    quality     : scTranscodingQuality
    snipped     : bool
    url         : str

@dataclass
class scTrackMedia(JSONWizard):
    transcodings: list[scTranscoding]

@dataclass 
class scTrackMini:
    id                  : int
    kind                : scTrackKind
    monetization_model  : scMonetizationModel
    policy              : str

@dataclass
class scTrack(JSONWizard, scTrackMini):
    artwork_url         : str
    caption             : str
    comment_count       : int
    commentable         : bool
    created_at          : str
    description         : str
    display_date        : str
    download_count      : int
    downloadable        : bool
    duration            : int
    embeddable_by       : scEmbeddableBy
    full_duration       : int
    genre               : str
    has_downloads_left  : bool
    label_name          : str | None
    last_modified       : str
    license             : scLicense
    likes_count         : int
    media               : scTrackMedia
    permalink           : str
    permalink_url       : str
    playback_count      : int
    public              : bool
    publisher_metadata  : scPublisherMetaData | None
    purchase_title      : str | None
    purchase_url        : str | None
    release_date        : str | None
    reposts_count       : int
    secret_token        : str | None
    sharing             : scSharing
    state               : sctrackState
    station_permalink   : str
    station_urn         : str
    streamable          : bool
    tag_list            : str | None
    title               : str
    track_authorization : str
    uri                 : str
    urn                 : str
    user                : scUserMini
    user_id             : int
    visuals             : scVisuals | None
    waveform_url        : str    
from typing import Literal

scUserKind              = Literal["user"]
scTrackKind             = Literal["track"]
scPlaylistKind          = Literal["playlist"]
scLikeKind              = Literal["like"]
scTrackRepostKind       = Literal["track-repost"]
scPlaylistRepostKind    = Literal["playlist-repost"]

scTranscodingFormatProtocol = Literal[
    "hls", 
    "progressive"
]

scTranscodingFormatMimeType = Literal[
    'audio/mpeg', 
    'audio/ogg; codecs="opus"'
]

scTranscodingPreset = Literal[
    'mp3_standard', 
    'opus_0_0', 
    'mp3_1_0', 
    'mp3_0_1', 
    'mp3_0_0'
]

scTranscodingQuality = Literal[
    "sq"
]

scMonetizationModel = Literal[
    'BLACKBOX', 
    'NOT_APPLICABLE',
    'AD_SUPPORTED',
    'SUB_HIGH_TIER'
]

scEmbeddableBy = Literal[
    "all",
    "me",
    "none"
]

scLicense = Literal[
    "no-rights-reserved",
    "all-rights-reserved",
    "cc-by",
    "cc-by-nc",
    "cc-by-nd",
    "cc-by-sa",
    "cc-by-nc-nd",
    "cc-by-nc-sa"    
]

scSharing = Literal[
    "public",
    "private"
]

sctrackPolicy = Literal[
    "MONETIZE",
    "SNIP",
    "ALLOW"
]

sctrackState = Literal[
    "finished"
]
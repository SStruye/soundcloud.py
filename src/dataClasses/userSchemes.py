from dataclass_wizard import JSONWizard
from dataclasses import dataclass
from ..constants.scLiterals import scUserKind
from .commonSchemes import scVisuals

@dataclass
class scUserBadges:
    pro                 : bool
    creator_mid_tier    : bool
    pro_unlimited       : bool
    verified            : bool

@dataclass
class scUserMini(JSONWizard):
    avatar_url          : str
    badges              : scUserBadges
    city                : str
    country_code        : str
    first_name          : str
    followers_count     : int
    full_name           : str
    id                  : int
    kind                : scUserKind
    last_modified       : str
    last_name           : str
    permalink           : str
    permalink_url       : str
    station_permalink   : str
    station_urn         : str
    uri                 : str
    urn                 : str
    username            : str
    verified            : bool

@dataclass
class scProduct:
    id      : str

@dataclass
class scCreatorSubscription(JSONWizard):
    product : scProduct

@dataclass 
class scUser(JSONWizard):
    comments_count          : int
    created_at              : str
    creator_subscriptions   : list[scCreatorSubscription]
    creator_subscription    : scCreatorSubscription
    description             : str
    followings_count        : int
    groups_count            : int
    likes_count             : int
    playlist_likes_count    : int
    permalink               : str
    reposts_count           : int | None
    track_count             : int
    visuals                 : scVisuals | None
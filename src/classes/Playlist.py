from .Base import Base
from .Track import Track
from ..dataClasses.playlistSchemes import scPlaylist
from ..dataClasses.trackSchemes import scTrack
from dataclass_wizard import fromdict

class Playlist(Base):
    def __init__(self, clientId : str = None, oauthToken : str = None):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def get(self, resolvable : int | str, loaded : bool = False, asDataClass : bool = False):
        if(isinstance(resolvable, int)): playlist = self.getRequest(endpoint = f"playlists/{resolvable}")
        elif(isinstance(resolvable, str)): playlist = self.resolve(resolvable = resolvable)
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        if(loaded): playlist = self.load(playlist)
        return fromdict(scPlaylist, playlist) if asDataClass else playlist
    
    def load(self, playlist : dict | scPlaylist):
        if(isinstance(playlist, dict)):
            track = Track(self.getClientId(), self.getOauthToken())
            playlist["tracks"] = track.get([tr["id"] for tr in playlist["tracks"]])
            del track
            return playlist
        elif(isinstance(playlist, scPlaylist)):
            track = Track(self.getClientId(), self.getOauthToken())
            playlist.tracks = [fromdict(scTrack, track) for track in track.get([tr["id"] for tr in playlist["tracks"]])]
            del track
            return playlist
        else: raise TypeError("Unsupported input. Supported inputs are dict")
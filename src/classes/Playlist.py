from .Base import Base
from .Track import Track

class Playlist(Base):
    def __init__(self, clientId : str = None, oauthToken : str = None):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def get(self, resolvable : int | str, loaded = False):
        if(isinstance(resolvable, int)):
            playlist = self.getRequest(endpoint = f"playlists/{resolvable}")
        if (isinstance(resolvable, str)):
            playlist = self.resolve(resolvable = resolvable)
        else:
            raise TypeError("Unsupported input. Supported inputs are int | str")

        return self.load(playlist) if loaded else playlist
    
    def load(self, playlist : dict):
        track = Track(self.getClientId(), self.getOauthToken())
        playlist["tracks"] = track.get([tr["id"] for tr in playlist["tracks"]])
        del track
        return playlist
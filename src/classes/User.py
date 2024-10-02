from .Base import Base
from .Playlist import Playlist

class User(Base):
    def __init__(self, clientId : str = None, oauthToken : str = None):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def get(self, resolvable: str | int):
        if(type(resolvable) == str):
            return self.resolve(resolvable)
        if(type(resolvable) == int):
            return self.getRequest(f'/users/{resolvable}')
        raise TypeError("Unsupported input. Supported inputs are int | str")
    
    def getTracks(self, resolvable: str | int):
        return self._getCollection(endpoint = "tracks", resolvable = resolvable)
    
    def getPlaylists(self, resolvable: str | int, loaded = False):
        playlists = self._getCollection(endpoint = "playlists_without_albums", resolvable = resolvable)
        if(loaded):
            playlist = Playlist(self.getClientId(), self.getOauthToken())
            playlists = [playlist.load(pl) for pl in playlists]
            del playlist
        return playlists

    def getAlbums(self, resolvable: str | int, loaded = False):
        return self._getCollection(endpoint = "albums", resolvable = resolvable, loaded = loaded)
    
    def getTopTracks(self, resolvable: str | int):
        return self._getCollection(endpoint = "toptracks", resolvable = resolvable)
    
    def getLikes(self, resolvable: str | int):
        return self._getCollection(endpoint = "likes", resolvable = resolvable)
    
    def getReposts(self, resolvable: str | int):
        return self._getCollection(endpoint = "reposts", resolvable = resolvable, stream = True)
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
        if(isinstance(resolvable, str)): return self.resolve(resolvable)
        elif(isinstance(resolvable, int)): return self.getRequest(f'/users/{resolvable}')
        raise TypeError("Unsupported input. Supported inputs are int | str")
    
    def getTracks(self, resolvable: str | int):
        userId = self._resolveUserId(resolvable)
        return self._getCollection(endpoint = f"users/{userId}/tracks")
    
    def getPlaylists(self, resolvable: str | int, loaded : bool = False):
        userId = self._resolveUserId(resolvable)
        playlists = self._getCollection(endpoint = f"users/{userId}/playlists_without_albums")
        if(not loaded): return playlists
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        return [scPlaylist.load(playlist) for playlist in playlists]

    def getAlbums(self, resolvable: str | int, loaded : bool = False):
        userId = self._resolveUserId(resolvable)
        albums = self._getCollection(endpoint = f"users/{userId}/albums")
        if(not loaded): return albums
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        return [scPlaylist.load(album) for album in albums]
    
    def getTopTracks(self, resolvable: str | int):
        userId = self._resolveUserId(resolvable)
        return self._getCollection(endpoint = f"users/{userId}/toptracks")
    
    def getLikes(self, resolvable: str | int, loaded : bool = False):
        userId = self._resolveUserId(resolvable)
        likes = self._getCollection(endpoint = f"users/{userId}/likes")
        if(not loaded): return likes
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        return [scPlaylist.load(like) if like["kind"] == "playlist" else like for like in likes]

    def getReposts(self, resolvable: str | int, loaded : bool = False):
        userId = self._resolveUserId(resolvable)
        reposts = self._getCollection(endpoint = f"stream/users/{userId}/reposts")
        if(not loaded): return reposts
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        return [scPlaylist.load(repost) if repost["kind"] == "playlist" else repost for repost in reposts]

    def _resolveUserId(self, resolvable: str | int):
        if(isinstance(resolvable, int)): return resolvable
        elif(isinstance(resolvable, str)): return self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
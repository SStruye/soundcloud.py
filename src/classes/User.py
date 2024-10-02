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
        if(isinstance(resolvable, int)): return self.getRequest(f'/users/{resolvable}')
        raise TypeError("Unsupported input. Supported inputs are int | str")
    
    def getTracks(self, resolvable: str | int):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        return self._getCollection(endpoint = f"user/{userId}/tracks")
    
    def getPlaylists(self, resolvable: str | int, loaded : bool = False):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        playlists = self._getCollection(endpoint = f"user/{userId}/playlists_without_albums")
        if(not loaded): return playlists
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        playlists = [scPlaylist.load(playlist) for playlist in playlists]
        del scPlaylist
        return playlists

    def getAlbums(self, resolvable: str | int, loaded : bool = False):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        albums = self._getCollection(endpoint = f"user/{userId}/albums")
        if(not loaded): return albums
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        albums = [scPlaylist.load(album) for album in albums]
        del scPlaylist
        return albums
    
    def getTopTracks(self, resolvable: str | int):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        return self._getCollection(endpoint = f"user/{userId}/toptracks")
    
    def getLikes(self, resolvable: str | int, loaded : bool = False):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        likes = self._getCollection(endpoint = f"user/{userId}/likes")
        if(not loaded): return likes
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        likes = [scPlaylist.load(like) if like["kind"] == "playlist" else like for like in likes]
        del scPlaylist
    
    def getReposts(self, resolvable: str | int, loaded : bool = False):
        if(isinstance(resolvable, int)): userId = resolvable
        if(isinstance(resolvable, str)): userId = self.resolve(resolvable)["id"]
        else: raise TypeError("Unsupported input. Supported inputs are int | str")
        reposts = self._getCollection(endpoint = f"stream/user/{userId}/reposts")
        if(not loaded): return reposts
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        likes = [scPlaylist.load(repost) if repost["kind"] == "playlist" else repost for repost in reposts]
        del scPlaylist
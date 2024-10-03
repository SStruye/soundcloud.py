from .Base import Base
from urllib.parse import urlparse, parse_qs
from .Playlist import Playlist

class Search(Base):
    def __init__(self, clientId : str = None, oauthToken : str = None):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def all(self, query : str, endpoint : str = "search", facet : str = "model", place : str = None, genre : str = None, contentTier : str = None, resultsDec : int = 1, loaded : bool = False):
        params = {
            "q": query,
            "facet": facet,
            "limit": 10,
            "linked_partitioning": 1,
            "offset": 0
        }
        filters = {
            "filter.place": place,
            "filter.genre": genre,
            "filter.content_tier": contentTier
        }
        params.update({k: v for k, v in filters.items() if v is not None})
        self.setParams(params)
        response = self.getRequest(endpoint)
        results = response.get("collection")
        next_href = response.get("next_href")
        while next_href and len(results) < resultsDec:
            self.setParams(parse_qs(urlparse(next_href).query))
            response = self.getRequest(endpoint)
            next_href = response.get("next_href")
            results += response.get("collection")
        if(not loaded): return results
        scPlaylist = Playlist(self.getClientId(), self.getOauthToken())
        return [scPlaylist.load(item) if item["kind"] == "playlist" else item for item in results]
        
    def users(self, query : str, place : str = None, resultsDec : int = 1):
        return self.all(query = query, endpoint = "search/users", facet = "place", place = place, resultsDec = resultsDec)
    
    def tracks(self, query : str, genre : str = None, contentTier : str = None, resultsDec : int = 1):
        return self.all(query = query, endpoint = "search/tracks", facet = "place", genre = genre, contentTier = contentTier, resultsDec = resultsDec)
    
    def playlist(self, query : str, genre : str = None, resultsDec : int = 1, loaded : bool = False):
        return self.all(query = query, endpoint = "search/playlists_without_albums", facet = "genre", genre = genre, resultsDec = resultsDec, loaded = loaded)
    
    def albums(self, query : str, genre : str = None, resultsDec : int = 1, loaded : bool = False):
        return self.all(query = query, endpoint = "search/albums", facet = "genre", genre = genre, resultsDec = resultsDec, loaded = loaded)
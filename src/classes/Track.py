from .Base import Base
import requests
import re
from urllib.parse import unquote

class Track(Base):
    def __init__(self, clientId : str = None, oauthToken : str = None):
        #! if(clientId = None or oauthToken = None): fetch em
        #! else:
        self.setClientId(clientId)
        self.setOauthToken(oauthToken)

    def __del__(self):
        pass

    def get(self, resolvable: int | str | list[int]):
        if(isinstance(resolvable, str)): return self.resolve(resolvable=resolvable)
        if(isinstance(resolvable, int)): return self.getRequest(endpoint=f"tracks/{resolvable}")
        if(isinstance(resolvable, list) and all(isinstance(t, int) for t in resolvable)):
            splitted_ids = [resolvable[i:i + 50] for i in range(0, len(resolvable), 50)]
            tracks = []
            for split in splitted_ids:
                self.setParams({"ids": ",".join(map(str, split))})
                tracks += self.getRequest(endpoint="tracks")
            return tracks

        raise TypeError("Unsupported input. Supported inputs are int, str, or list[int]")
    
    def download(self, resolvable : int | str, savePath = "./test/", custom_fn : str = None):
        id = resolvable
        if(isinstance(resolvable, str)): id = self.resolve(resolvable)["id"]
        try:
            response = self.getRequest(f"tracks/{id}/download")
        except:
            raise ValueError("track is not downloadable")
        response = requests.get(response["redirectUri"])

        filename  = re.search(r'filename="([^"]+)"', response.headers["Content-Disposition"])
        filename_ = re.search(r'filename\*\=utf-8\'\'(.+)', response.headers["Content-Disposition"])

        if(custom_fn):
            filename = f"{custom_fn}.{response.headers['x-amz-meta-file-type']}"
        elif(filename_): 
            filename = unquote(filename_.group(1))
        elif(filename):
            filename = filename.group(1)
            if("." not in filename): filename += f".{response.headers['x-amz-meta-file-type']}"
        else:
            filename = f"untitled.{response.headers['x-amz-meta-file-type']}"
        if(savePath[-1] != "/"): savePath += "/"
        with open(savePath+filename, "wb") as file:
            file.write(response.content)
        return filename
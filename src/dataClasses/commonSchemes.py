from dataclass_wizard import JSONWizard
from dataclasses import dataclass
from ..constants.scLiterals import *

@dataclass
class scVisual:
    urn         : str
    entry_time  : int
    visual_url  : str

@dataclass
class scVisuals(JSONWizard):
    urn         : str
    enabled     : bool
    visuals     : list[scVisual]
    tracking    : str
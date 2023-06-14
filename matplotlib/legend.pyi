from .artist import Artist
from .font_manager import FontProperties

class Legend(Artist):
    def __init__(self, loc: str = ..., prop: FontProperties= ...) -> None:
        self.loc = loc
        self.prop = prop
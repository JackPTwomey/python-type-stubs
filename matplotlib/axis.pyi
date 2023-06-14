from .artist import Artist as Artist
from matplotlib.axes._base import _AxesBase as _AxesBase
from matplotlib.text import Text

class Axis(Artist):
    def __init__(self) -> None:
        self.labelpad = 4
class YAxis(Axis):
    def __init__(self, axes: _AxesBase) -> None: ...
    def get_ticklabels(self) -> list[Text]: ...
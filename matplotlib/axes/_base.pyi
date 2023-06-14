from matplotlib.artist import Artist as Artist
from matplotlib.axis import YAxis as YAxis
from matplotlib.font_manager import FontProperties as FontProperties
from matplotlib.patches import Patch as Patch
from matplotlib.transforms import BboxTransformTo as BboxTransformTo
from matplotlib.transforms import TransformedBbox as TransformedBbox

class _AxesBase(Artist):
    def __init__(self) -> None:
        self.bbox = self.get_window_extent()
        self.transAxes = BboxTransformTo(self.bbox)
        self.yaxis = YAxis(self)
    def add_patch(self, p: Patch) -> Patch: ...
    def get_window_extent(self) -> TransformedBbox: ...
    def get_yaxis(self) -> None: ...
    def set_ylabel(
        self,
        ylabel: str,
        rotation: float,
        fontproperties: FontProperties,
        fontsize: float,
        y: float
    ) -> None: ...
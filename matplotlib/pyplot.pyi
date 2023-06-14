from pathlib import Path
from typing import Literal, Optional, Sequence

from .artist import Artist
from .axes import Axes as Axes
from .collections import LineCollection, PathCollection
from .colorbar import Colorbar
from .colors import Colormap, Normalize
from .container import BarContainer
from .figure import Figure
from .font_manager import FontProperties
from .legend import Legend
from .markers import MarkerStyle
from .text import Text
from .transforms import Transform

from numpy.typing import ArrayLike

def annotate(
    text: str,
    xy: Sequence[float],
    xytext: Sequence[float] =  ...,
    xycoords: str | Artist | Transform = ...,
    ha: str = ...,
    fontproperties: FontProperties = ...,
    fontsize: float = ...,
    textcoords: str | Artist | Transform = ...,
    arrowprops: dict[str, str] = ...,
) -> None: ...
def axis() -> tuple[float, float, float, float]: ...
def bar(
    x: float | ArrayLike,
    height: float | ArrayLike,
    width: float | ArrayLike = ...,
    bottom: float | ArrayLike = ...,
    align: Literal['center', 'edge'] = ...,
    linewidth: float = ...,
    color: str | list[tuple[float, float, float] | str] = ...,
    edgecolor: str | list[tuple[float, float, float] | str] = ...
) -> BarContainer: ...
def boxplot(x: ArrayLike, sym: str = ...) -> dict[str, list[float]]: ...
def close() -> None: ...
def colorbar() -> Colorbar: ...
def clim(vmin: float | None = ..., vmax: float | None = ...) -> None: ...
def figure(figsize: Sequence[float] = ...) -> Figure: ...
def gca() -> None: ...
def hlines(
    y: float,
    xmin: float,
    xmax: float,
    linewidth: float = ...,
    alpha: float = ...,
    color: str = ...,
    label: Optional[str] = None
) -> LineCollection: ...
def legend(loc: str = ..., prop: FontProperties = ...) -> Legend: ...
def savefig(fname: str | Path) -> None: ...
def scatter(
    x: float | ArrayLike,
    y: float | ArrayLike,
    s: float | ArrayLike = ...,
    c: ArrayLike | str | list[tuple[float, float, float] | str] | tuple[float, float, float] | str = ...,
    marker: MarkerStyle = ...,
    cmap: str | Colormap = ...,
    norm: Normalize = ...,
    vmin: float = ...,
    vmax: float = ...,
    alpha: float = ...,
    linewidth: float | ArrayLike = ...,
    edgecolors: tuple[float, float, float] | str = ...,
    plotnonfinite: bool = ...,
) -> PathCollection: ...
def setp(obj: Artist | list[Artist], fontsize: str = ...) -> None: ...
def tight_layout() -> None: ...
def text(
    x: float,
    y: float,
    text: str,
    fontproperties: FontProperties = ...,
    fontsize: float | str = ...,
    ha: Literal['left', 'center', 'right'] = ...
) -> Text: ...
def title(label: str, fontproperties: FontProperties = ..., fontsize: float = ...) -> None: ...
def xlabel(
    xlabel: str,
    fontproperties: FontProperties = ...,
    fontsize: float = ...,
    labelpad: float = ...
) -> None: ...
def xlim(lims: list[float] | float = ..., left: float = ..., right: float = ...) -> tuple[float, float]: ...
def xticks(ticks: ArrayLike = ..., labels: ArrayLike = ..., fontproperties: FontProperties = ..., fontsize: float = ...) -> tuple[list[float], list[Text]]: ...
def ylabel(ylabel: str, fontproperties: FontProperties = ..., fontsize: float = ...) -> None: ...
def ylim(lims: list[float] | float = ..., bottom: float = ..., top: float = ...) -> tuple[float, float]: ...
def yticks(ticks: ArrayLike = ..., labels: ArrayLike = ..., fontproperties: FontProperties = ..., fontsize: float = ...) -> tuple[list[float], list[Text]]: ...
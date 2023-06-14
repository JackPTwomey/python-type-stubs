from matplotlib.axes import Axes as Axes

class Colorbar:
    ax: Axes
    def __init__(self, ax: Axes) -> None:
        self.ax = ax
    def set_ticklabels(self, ticklabels: list[str]) -> None: ...
    def set_ticks(self, ticks: list[float]) -> None: ...
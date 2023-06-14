from matplotlib.artist import Artist
from matplotlib.cm import ScalarMappable

class _CollectionWithSizes(Collection): ...
class Collection(Artist, ScalarMappable): ...
class LineCollection(Collection):
    def __init__(self, segments: list[list[tuple[float, float]]]) -> None:
        self.segments = segments
class PathCollection(_CollectionWithSizes): ...
from enum import Enum


class UnitType(Enum):
    PIXELS = 0


# 2DAABBP - 2 Dimensional Axis Aligned Bounding Box in Pixels
#
# xlu - x coordinate for upper left corner in pixels
# ylu - x coordinate for upper left corner in pixels
# w - width in pixels
# h - height in pixels

def pixels_to_2daabbp_v0(letter: str = '', xlu: int = 0, ylu: int = 0, w: int = 0, h: int = 0) -> dict:
    r = dict()
    r['l'] = letter
    r['xlu'] = xlu
    r['ylu'] = ylu
    r['w'] = w
    r['h'] = h

    return r


def coord_to_2daabb(letter: str = '', xlu: int = 0, ylu: int = 0, w: int = 0, h: int = 0, ut: int = 0) -> dict:
    r = dict()
    if ut == UnitType.PIXELS.value:
        r = pixels_to_2daabbp_v0(letter=letter, xlu=xlu, ylu=ylu, w=w, h=h)

    return r

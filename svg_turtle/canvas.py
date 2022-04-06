import typing
from dataclasses import dataclass
from operator import attrgetter

from svgwrite import Drawing

ANCHOR_NAMES = dict(sw='start',
                    s='middle',
                    se='end')


class DummyWindow:
    def call(self, *args, **kwargs):
        pass


class Canvas(object):
    def __init__(self, width=400, height=250):
        self.options = {'width': width,
                        'height': height,
                        'bg': 'white'}
        self.items: typing.List[CanvasItem] = []
        self.max_zorder = 0

        def make_call(method_name):
            return lambda *args, **kwargs: self.call(method_name,
                                                     *args,
                                                     **kwargs)

        method_names = ('create_line',
                        'create_polygon',
                        'create_text',
                        'create_image')
        for name in method_names:
            self.__dict__[name] = make_call(name)

    def call(self, method_name, *args, **kwargs):
        if method_name == 'create_polygon':
            args = args[0]
        item = CanvasItem(method_name, args, kwargs)
        item_id = len(self.items)
        self.items.append(item)
        return item_id

    def to_drawing(self):
        width = self.winfo_width()
        height = self.winfo_height()
        width_text = f'{width}px'
        height_text = f'{height}px'
        drawing = Drawing(size=(width_text, height_text))

        clip_path = drawing.defs.add(drawing.clipPath(id='border_clip'))
        clip_path.add(drawing.rect(size=(width, height)))
        bgcolor = self.options.get('bg')
        if bgcolor:
            drawing.add(drawing.rect(fill=bgcolor, size=('100%', '100%')))

        for item_details in sorted(self.items, key=attrgetter('z_order')):
            attribs = item_details.attribs.copy()
            method_name = item_details.method_name
            if method_name == 'create_polygon':
                attribs['outline'] = ''
                try:
                    del attribs['width']
                except KeyError:
                    pass
            self.add_svg_element(item_details, drawing)
        return drawing

    def add_svg_element(self, item_details: 'CanvasItem', drawing: Drawing):
        if item_details.is_deleted:
            return
        if item_details.attribs.get('fill') == '':
            return
        if item_details.attribs.get('image') == '':
            return
        sx1, sy1, sx2, sy2 = self.options.get(
            'scrollregion',
            (0, -self.winfo_height(), self.winfo_width(), 0))
        xoff = 0.5 - sx1
        yoff = 0.5 - sy1
        coords = list(item_details.coords)
        # noinspection DuplicatedCode
        for i in range(0, len(coords), 2):
            x, y = coords[i:i+2]
            x = x + xoff
            y = y + yoff
            coords[i] = x
            coords[i+1] = y
        attribs = item_details.attribs
        if item_details.method_name == 'create_line':
            drawing.add(drawing.polyline(build_coordinate_pairs(coords),
                                         stroke=attribs['fill'],
                                         stroke_width=attribs['width'],
                                         stroke_linecap='round',
                                         fill='none',
                                         clip_path='url(#border_clip)'))
        elif item_details.method_name == 'create_polygon':
            drawing.add(drawing.polygon(build_coordinate_pairs(coords),
                                        fill=attribs['fill'],
                                        stroke=attribs['outline'],
                                        stroke_width=attribs.get('width', 0),
                                        fill_rule='evenodd',
                                        clip_path='url(#border_clip)'))
        elif item_details.method_name == 'create_text':
            font_name, font_size, font_style = attribs['font']
            x, y = coords
            y -= font_size * 0.45
            font_size *= 1.65
            style = 'font-family: {}; font-size: {}; font-style: {};'.format(
                font_name,
                font_size,
                font_style)

            drawing.add(drawing.text(attribs['text'],
                                     insert=(x, y),
                                     text_anchor=ANCHOR_NAMES[attribs['anchor']],
                                     style=style,
                                     fill=attribs['fill'],
                                     clip_path='url(#border_clip)'))

    def cget(self, option):
        return self[option]

    def __getitem__(self, item):
        return self.options[item]

    def winfo_width(self):
        return self['width']

    def winfo_height(self):
        return self['height']

    def config(self, **kwargs):
        self.options.update(kwargs)

    def find_all(self):
        return range(len(self.items))

    def coords(self, item, *coords):
        item_details = self.items[item]
        if len(coords) == 0:
            return item_details.coords
        item_details.coords = coords

    def itemconfigure(self, item, **kwargs):
        item_details = self.items[item]
        item_details.attribs.update(kwargs)

    def delete(self, item):
        if item == 'all':
            self.items.clear()
        else:
            item_details = self.items[item]
            item_details.is_deleted = True

    @staticmethod
    def winfo_toplevel():
        return DummyWindow()

    def update(self):
        pass

    def bind(self, *args, **kwargs):
        pass

    def unbind(self, *args, **kwargs):
        pass

    def tag_bind(self, *args, **kwargs):
        pass

    def tag_unbind(self, *args, **kwargs):
        pass

    def focus_force(self):
        pass

    def after(self, *args, **kwargs):
        pass

    def tag_raise(self, item):
        item_details = self.items[item]
        self.max_zorder += 1
        item_details.z_order = self.max_zorder

    def bbox(self, item):
        item_details = self.items[item]
        # noinspection PyTupleAssignmentBalance
        x, y = item_details.coords
        return x, y, x, y

    def type(self, item):
        item_details = self.items[item]
        return item_details.method_name[7:]


@dataclass
class CanvasItem:
    method_name: str
    coords: typing.Tuple[float]
    attribs: dict
    z_order: int = 0
    is_deleted: bool = False


def build_coordinate_pairs(coords: typing.Sequence[float]):
    assert len(coords) % 2 == 0
    coords_iter = iter(coords)
    return [(x, y) for x, y in zip(coords_iter, coords_iter)]

import collections
scale = 128
stroke_width = 48
Point = collections.namedtuple('Point', ['x', 'y'])
origin = Point(0, stroke_width/2)

backwards_s = ' '.join([
    f'M{origin.x},{origin.y}',
    f'l {2*scale + stroke_width/2},0',
    f'a{scale},{scale} 0 0,1 0,{2 * scale}',
    f'l -{scale},0',
    f'a{scale},{scale} 0 0,0 0,{2 * scale}',
    f'l {2*scale + stroke_width/2},0'])

vertical_line = f'M{origin.x},{origin.y} m{1.5*scale + stroke_width/2},{scale} l 0,{2 * scale}'

path_d = f'{backwards_s} {vertical_line}'

symbol_svg = f'''<?xml version="1.0" standalone="no"?>
<svg
        xmlns="http://www.w3.org/2000/svg"
        version="1.1" style="display:none">
    <symbol id="pcattori-logo" viewBox="0 0 {3*scale + stroke_width} {4*scale + stroke_width}">
        <path d="{path_d}" fill="none" stroke="black" stroke-width="{stroke_width}"/>
    </symbol>
</svg>
'''

svg = f'''<?xml version="1.0" standalone="no"?>
<svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 {3*scale + stroke_width} {4*scale + stroke_width}"
        version="1.1">
    <path d="{path_d}" fill="none" stroke="black" stroke-width="{stroke_width}"/>
</svg>
'''

print(svg)

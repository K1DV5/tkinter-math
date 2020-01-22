# -{cd ../tests | python test.py}
from .data import *

# default
MEASURE = FONT = None
LINESPACE = OVERRIDE_LINESPACE = 0

def calculate_linespace(font):
    linespace = font.metrics('linespace')
    mwidth = font.measure('M')
    to_set = mwidth*1.52
    if to_set > linespace:
        return [linespace, linespace]
    return [linespace, to_set]

def select_font(font):
    '''use this before doing anything using this module'''
    global MEASURE, FONT, LINESPACE, OVERRIDE_LINESPACE
    MEASURE = font.measure
    font_props = font.actual()
    FONT = (font_props['family'], font_props['size'])
    LINESPACE, OVERRIDE_LINESPACE = calculate_linespace(font)

class Primitive:
    '''text and line'''
    def __init__(self, content, kind='t', **kwargs):
        self.content = content
        self.kind = kind
        self.relsize = 1
        self.x = kwargs['x'] if 'x' in kwargs else 0
        self.y = kwargs['y'] if 'y' in kwargs else 0
        if self.kind == 't':
            self.slant = kwargs['slant'] if 'slant' in kwargs else 'roman'
            self.width, self.height = MEASURE(self.content), OVERRIDE_LINESPACE
        else:  # line
            self.linewidth = OVERRIDE_LINESPACE * 0.04
            if 'linewidth' in kwargs:
                self.linewidth *= kwargs['linewidth']  # must be relative
            if 'width' in kwargs or 'height' in kwargs:
                self.width, self.height = kwargs['width'], kwargs['height']
            else:
                xes, ys = [], []
                for i in range(int(len(self.content)/2)):  # take two at a time
                    i_x = i*2
                    xes.append(self.content[i_x])
                    ys.append(self.content[i_x + 1])
                self.width, self.height = max(xes) - min(xes), max(ys) - min(ys)
                if not self.height: self.height = self.linewidth * 3
            self.smooth = kwargs['smooth'] if 'smooth' in kwargs else False
        self.midline = kwargs['midline'] if 'midline' in kwargs else 0.5
        if 'relsize' in kwargs:
            self.pull_size(kwargs['relsize'])

    def pull_size(self, to):
        # relsize = self.relsize
        # self.relsize = (self.relsize + to) / 2
        # factor = self.relsize / relsize
        factor = to*1.4
        self.relsize *= factor
        self.width *= factor
        self.height *= factor
        self.x *= factor
        self.y *= factor

    def render(self, canvas):
        if self.kind == 't':
            y = self.y - (LINESPACE - OVERRIDE_LINESPACE) * self.relsize / 2  # in the middle
            font = (FONT[0], round(FONT[1] * self.relsize), self.slant)
            canvas.create_text((self.x, y), text=self.content, font=font, anchor='nw')
        elif self.kind == 'l':
            points = []
            for i in range(int(len(self.content)/2)):  # take two at a time
                i_x = i * 2
                points.append(self.content[i_x] * self.relsize + self.x)
                points.append(self.content[i_x + 1] * self.relsize + self.y)
            # three times with different colors & thickness to approximate anti-aliasing
            canvas.create_line(points, width=self.linewidth + .9, smooth=self.smooth, joinstyle='miter', fill='#999')
            canvas.create_line(points, width=self.linewidth - .3, smooth=self.smooth, joinstyle='miter', fill='#444')
            canvas.create_line(points, width=self.linewidth - .5, smooth=self.smooth, joinstyle='miter')
            # canvas.create_line(points, width=self.linewidth, smooth=self.smooth, joinstyle='miter')

    def split(self, string):
        if self.kind != 't':
            return
        return [Primitive(part, 't', slant=self.font_props['slant']) for part in self.content.split(string)]

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError(type(other))
        if isinstance(other, Entity):
            if other.arrange_direc == 'horiz':
                return Entity([self, *other.content])
        return Entity([self, other])

    def join(self, others):
        to_join = []
        for other in others:
            to_join += [other, self]
        return Entity(to_join[:-1])

    def __repr__(self):
        content = self.content if type(self.content) == str else "line"
        return f'Primitive({content})'


class Entity:
    '''combination of text, line, (primitives) or other entities'''
    def __init__(self, content, arrange='horiz'):
        self.x = self.y = self.width = self.height = 0
        self.content = content
        self.arrange_direc = arrange
        self.midline = 0.5
        self.relsize = 1
        self.arrange()

    def arrange(self):
        if not self.arrange_direc:
            return
        if self.arrange_direc == 'horiz':
            # calculate the height
            top, bot = [], []
            for part in self.content:
                top.append(part.height * part.midline)
                bot.append(part.height - top[-1])
            h_top = max(top) if top else 0
            self.height = h_top + (max(bot) if bot else 0)
            # determine coords
            x = 0
            for part in self.content:
                part.x, part.y = x, h_top - part.midline*part.height
                x += part.width
            self.width = x
        elif self.arrange_direc == 'vert':
            y = 0
            self.width = max([part.width for part in self.content])
            for part in self.content:
                part.x, part.y = (self.width - part.width) / 2, y
                y += part.height
            self.height = y

    def pull_size(self, to):
        # relsize = self.relsize
        # self.relsize = (self.relsize + to) / 2
        # factor = self.relsize / relsize
        factor = to*1.4
        self.width *= factor
        self.height *= factor
        self.x *= factor
        self.y *= factor
        for part in self.content:
            part.pull_size(to)

    def render(self, canvas):
        for part in self.content:
            part.x, part.y = part.x + self.x, part.y + self.y
            part.render(canvas)

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError()
        if self.arrange_direc == 'horiz':
            if isinstance(other, Entity) and other.arrange_direc == 'horiz':
                return Entity([*self.content, *other.content])
            return Entity([*self.content, other])
        return Entity([self, other])

    def __repr__(self):
        return f'Entity({", ".join([str(c) for c in self.content])})'

class syntax:

    # some symbols
    minus = '−'
    times = '×'
    div = '÷'
    cdot = '⋅'
    halfsp = ' '
    neg = '¬'
    gt = '&gt;'
    lt = '&lt;'
    gte = '&ge;'
    lte = '&le;'
    cdots = '⋯'
    vdots = '⋮'
    ddots = '⋱'

    greek_letters = GREEK_LETTERS
    math_accents = MATH_ACCENTS
    primes = PRIMES

    # things that are transformed, used for units and such
    @property
    def transformed(self):
        return {
            'degC': self.sup(self.txt(' '), self.txt('∘')) + self.txt('C'),
            'degF': self.sup(self.txt(' '), self.txt('∘')) + self.txt('F'),
            'deg': self.sup(self.txt(' '), self.txt('∘'))
        }

    def txt(self, text):
        if text in [self.times, self.div, self.cdot, '+', self.minus, '=']:
            text = f' {text} '
        if text.isalpha():
            slant = 'italic'
        else:
            slant = 'roman'
        return Primitive(text, 't', slant=slant)

    def txt_rom(self, text):
        return Primitive(text, 't', slant='roman')

    def txt_math(self, text):
        return self.txt_rom(text)

    def sup(self, base, s):
        s.pull_size(.5)
        s.x = base.width * 1.2  # s.y = 0
        base.y = s.height - 0.5*base.height  # base.x = 0
        sup = Entity([base, s], False)
        sup.width = s.x + s.width
        sup.height = base.y + base.height
        sup.midline = (base.y + base.midline * base.height) / sup.height
        return sup

    def sub(self, base, s):
        s.pull_size(.5)
        s.x = base.width
        s.y = 0.5 * base.height
        sub = Entity([base, s], False)
        sub.width = s.x + s.width
        sub.height = s.y + s.height
        sub.midline = base.height*base.midline / sub.height
        return sub


    def rad(self, base):
        if base.height < OVERRIDE_LINESPACE*1.4:
            char = Primitive('√')
        else:
            width, height = OVERRIDE_LINESPACE * 0.7, base.height
            char = Primitive([
                0,
                height/2,
                0.1 * width,
                height*0.45,
                width/2,
                height,
                width,
                0], 'l', linewidth=1.2)
        line = Primitive([0, 0, base.width + OVERRIDE_LINESPACE/2, 0], 'l')
        return Entity([char, Entity([line, base], 'vert')])

    def summation(self, base, end):
        start = Entity([self.txt('i'), self.txt('='), self.txt('1')])
        start.pull_size(.5)
        mark = Primitive('∑', relsize=1.5)
        end = Primitive(str(end), relsize=0.7)
        notation = Entity([end, mark, start], 'vert')
        return Entity([notation, base])

    def func_name(self, name):
        return self.txt_rom(name + ' ')

    def frac(self, num, den):
        wmax = max([num.width, den.width])
        line = Primitive([0, 0, wmax*1.2, 0], 'l')
        part = Entity([num, line, den], 'vert')
        part.midline = num.height / (num.height + den.height)
        return part

    def math_disp(self, math):
        return math

    def math_inln(self, math):
        return math

    def greek(self, name):
        return self.txt(GREEK_LETTERS[name])

    def accent(self, acc, base):
        acc = Primitive(MATH_ACCENTS[acc])
        acc.x = (base.width*1.5 - acc.width) / 2
        base.y = 0.2*acc.height
        part = Entity([acc, base], False)
        part.width, part.height = base.width, base.y + base.height
        return part

    def prime(self, base, prime):
        return self.sup(base, self.txt(PRIMES[prime]))

    def delmtd(self, contained, kind=0):
        if contained.height < OVERRIDE_LINESPACE*1.4:
            brackets = BRACKETS[kind]
            surround = [Primitive(brackets[0]), Primitive(brackets[1])]
            return Entity([surround[0], contained, surround[1]])

        width, height = OVERRIDE_LINESPACE*2/3, contained.height
        smooth = True
        w = width/2  # width of the horizontal bar
        points = [[width, 0, w, 0, w, height, width, height], [0, 0, w, 0, w, height, 0, height]]
        if kind == 1:  # []
            smooth = False
        elif kind == 2:  # {}
            w, mid_point = width*2/5, height/2  # width and height of the chamfers
            x_mid, x_offset = width - w, width - 2*w
            points = [[width, 0, x_mid, 0, x_mid, mid_point, width-2*w, mid_point, x_mid, mid_point, x_mid, height, width, height],
                      [0, 0, w, 0, w, mid_point, w*2, mid_point, w, mid_point, w, height, 0, height]]
        elif kind == 3:  # ⌊⌋
            smooth = False
            points[0], points[1] = points[0][2:], points[1][2:]
        left = Primitive(points[0], 'l',
                         smooth=smooth,
                         linewidth=2,
                         x=width,
                         y=height*25,
                         width=width,
                         height=height*1.05)
        right = Primitive(points[1], 'l',
                          smooth=smooth,
                          linewidth=2,
                          width=width,
                         y=height*0.025,
                          height=height*1.05)
        return Entity([left, contained, right])

    def matrix(self, elmts, full=False):
        if not full:  # just a row
            return elmts

        # top level, full matrix
        if type(elmts[0]) != list:
            return self.delmtd(Entity(elmts, 'vert'), 1)
        heights = []
        # get the max params
        widths = [[] for _ in elmts[0]]
        for row in elmts:
            row_heights = []
            for i, elt in enumerate(row):
                widths[i].append(elt.width)
                row_heights.append(elt.height)
            heights.append(max(row_heights))
        widths = [max(w) for w in widths]
        elements = []  # entity members
        y = 0
        colgap = OVERRIDE_LINESPACE*0.5
        for i_r, row in enumerate(elmts):
            x = 0
            for i_e, elt in enumerate(row):
                elt.x = x + (widths[i_e] - elt.width) / 2
                elt.y = y + (heights[i_r] - elt.height) / 2
                elements.append(elt)
                x += widths[i_e] + colgap
            y += heights[i_r]
        part = Entity(elements, False)
        part.width, part.height = sum(widths) + colgap*(len(widths) - 1), sum(heights)
        return self.delmtd(part, 1)
      
    def eqarray(self, eqns: list):
        # get max dims: widths1 = widths2, heights
        w_lefts, w_rights, h_top, h_bot = [], [], [], []
        # to get the height above/below the midline
        h = lambda x, top=True: x.height*(x.midline if top else 1-x.midline)
        for line in eqns:
            h_top.append(max([h(line[0]), h(line[1])]))
            h_bot.append(max([h(line[0], False), h(line[1], False)]))
            w_lefts.append(line[0].width)
            if len(line) > 1:
                w_rights.append(line[1].width)
        w_left, w_right = max(w_lefts), max(w_rights)
        # align them to the =
        lines = []
        for i, line in enumerate(eqns):
            elts = [line[0]]
            width = w_left
            line[0].x, line[0].y = w_left - line[0].width, h_top[i] - h(line[0])
            if len(line) > 1:
                equals = Primitive(' = ')
                equals.x, equals.y = w_left, h_top[i] - h(equals)
                line[1].x, line[1].y = w_left + equals.width, h_top[i] - h(line[1])
                elts += [equals, line[1]]
                width += equals.width + w_right
            ent = Entity(elts, False)
            ent.width, ent.height = width, h_top[i] + h_bot[i]
            lines.append(ent)
        return Entity(lines, 'vert')


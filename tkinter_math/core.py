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
    def __init__(self, content, kind='t', slant='roman'):
        self.coords = (0, 0)
        self.content = content
        self.kind = kind
        self.relsize = 1
        if self.kind == 't':
            self.slant = slant
            self.size = (MEASURE(self.content), OVERRIDE_LINESPACE)
        else:
            self.size = (content[2] - content[0], content[3] - content[1])
        self.midline = 0.5

    def resize(self, factor):
        self.relsize *= factor
        self.size = (self.size[0]*factor, self.size[1]*factor)
        self.coords = (self.coords[0]*factor, self.coords[1]*factor)

    def render(self, canvas):
        if self.kind == 't':
            y = self.coords[1] - (LINESPACE - OVERRIDE_LINESPACE) * self.relsize / 2
            font = (FONT[0], round(FONT[1] * self.relsize), self.slant)
            canvas.create_text((self.coords[0], y), text=self.content, font=font, anchor='nw')
        elif self.kind == 'l':
            self.content[2] *= self.relsize
            self.content[3] *= self.relsize
            canvas.create_line([
                self.content[0] + self.coords[0],
                self.content[1] + self.coords[1],
                self.content[2] + self.coords[0],
                self.content[3] + self.coords[1],
            ])

    def split(self, string):
        if self.kind != 't':
            return
        return [Primitive(part, 't', self.font_props['slant']) for part in self.content.split(string)]

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError(type(other))
        if isinstance(other, Entity):
            if other.arrange_direc == 'horiz':
                other.content = [self] + other.content
                other.arrange()
                return other
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
        self.coords = (0, 0)
        self.content = content
        self.size = (0, 0)
        self.arrange_direc = arrange
        self.midline = 0.5
        self.arrange()

    def arrange(self):
        if not self.arrange_direc:
            return
        if self.arrange_direc == 'horiz':
            # calculate the height
            top, bot = [], []
            for part in self.content:
                h = part.size[1]
                top.append(h*part.midline)
                bot.append(h*(1-part.midline))
            top, bot = (max(top) if top else 0), (max(bot) if bot else 0)
            height = top + bot
            # determine coords
            x = 0
            for part in self.content:
                part.coords = (x, top - part.midline*part.size[1])
                x += part.size[0]
            self.size = (x, height)
        elif self.arrange_direc == 'vert':
            y = 0
            width = max([part.size[0] for part in self.content])
            for part in self.content:
                part.coords = ((width - part.size[0]) / 2, y)
                y += part.size[1]
            self.size = (width, y)

    def resize(self, factor):
        self.size = (self.size[0]*factor, self.size[1]*factor)
        self.coords = (self.coords[0]*factor, self.coords[1]*factor)
        for part in self.content:
            part.resize(factor)

    def render(self, canvas):
        for part in self.content:
            part.coords = (part.coords[0] + self.coords[0], part.coords[1] + self.coords[1])
            part.render(canvas)

    def __add__(self, other):
        if type(other) not in [Primitive, Entity]:
            raise TypeError()
        if self.arrange_direc == 'horiz':
            if isinstance(other, Entity):
                if other.arrange_direc == 'horiz':
                    self.content += other.content
                    self.arrange()
                    return self
            self.content.append(other)
            self.arrange()
            return self
        return Entity([self, other])

    def __repr__(self):
        return f'Entity({self.content})'

class syntax:

    # things that are transformed, used for units and such
    transformed = {
        'degC': '<m:sSup><m:e><m:r><m:t> </m:t></m:r></m:e><m:sup><m:r><m:t>∘</m:t></m:r></m:sup></m:sSup><m:r><m:rPr><m:nor/></m:rPr><m:t>C</m:t></m:r>',
        'degF': '<m:sSup><m:e><m:r><m:t> </m:t></m:r></m:e><m:sup><m:r><m:t>∘</m:t></m:r></m:sup></m:sSup><m:r><m:rPr><m:nor/></m:rPr><m:t>F</m:t></m:r>',
        'deg': '<m:sSup><m:e><m:r><m:t> </m:t></m:r></m:e><m:sup><m:r><m:t>∘</m:t></m:r></m:sup></m:sSup>'
    }

    # some symbols
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

    def txt(self, text):
        if text in [self.times, self.div, self.cdot, '+', '-']:
            text = f' {text} '
        if text.isalpha():
            slant = 'italic'
        else:
            slant = 'roman'
        return Primitive(text, 't', slant)

    def txt_rom(self, text):
        return Primitive(text, 't', 'roman')

    def txt_math(self, text):
        return self.txt_rom(text)

    def sup(self, base, s):
        s.resize(0.7)
        sup_x_offset = 1.2
        top_offset = s.size[1] - 0.5*base.size[1]
        base.coords = (0, top_offset)
        s.coords = (base.size[0]*sup_x_offset, 0)
        sup = Entity([base, s], False)
        wmax = base.size[0]*sup_x_offset + s.size[0]
        hmax = base.size[1] + top_offset
        sup.size = (wmax, hmax)
        sup.midline = (hmax - base.size[1]*(1-base.midline)) / hmax
        return sup

    def sub(self, base, s):
        s.resize(0.7)
        sub_x_offset = 1.0
        top_offset = 0.5*base.size[1]
        base.coords = (0, 0)
        s.coords = (base.size[0]*sub_x_offset, top_offset)
        sub = Entity([base, s], False)
        wmax = base.size[0]*sub_x_offset + s.size[0]
        hmax = base.size[1] + s.size[1] - top_offset
        sub.size = (wmax, hmax)
        sub.midline = base.size[1]*base.midline / hmax
        return sub


    def rad(self, base):
        char = Primitive('√')
        char.resize(base.size[1]/char.size[1])
        line = Primitive([0, 0, base.size[0], 0], 'l')
        return Entity([char, Entity([line, base], 'vert')])

    def summation(self, base, end):
        start = Entity([Primitive('i'), Primitive('='), Primitive('1')])
        start.resize(0.7)
        mark = Primitive('∑')
        mark.resize(1.5)
        end = Primitive(str(end))
        end.resize(0.7)
        notation = Entity([start, mark, end], 'vert')
        return Entity([notation, base])

    def func_name(self, name):
        return self.txt_rom(name + ' ')

    def frac(self, num, den):
        linewidth = 1.2
        wmax = max([num.size[0], den.size[0]])
        line = Primitive([0, 0, wmax*linewidth, 0], 'l')
        part = Entity([num, line, den], 'vert')
        part.midline = num.size[1] / (num.size[1] + den.size[1])
        return part

    def math_disp(self, math):
        return math

    def math_inln(self, math):
        return math

    def greek(self, name):
        return self.txt(GREEK_LETTERS[name])

    def accent(self, acc, base):
        acc = Primitive(MATH_ACCENTS[acc])
        acc.coords = ((base.size[0]*1.5 - acc.size[0]) / 2, 0)
        top_offset = 0.2*acc.size[1]
        base.coords = (0, top_offset)
        part = Entity([acc, base], False)
        part.size = (base.size[0], base.size[1] + top_offset)
        return part

    def prime(self, base, prime):
        return self.sup(base, self.txt(PRIMES[prime]))

    def delmtd(self, contained, kind=0):
        if contained.size[1] < OVERRIDE_LINESPACE*1.4:
            brackets = BRACKETS[kind][0]
            surround = [Primitive(brackets[0]), Primitive(brackets[1])]
            return Entity([surround[0], contained, surround[1]])
        extensions = round(contained.size[1]/OVERRIDE_LINESPACE) - 2
        brackets = [BRACKETS[kind][1], BRACKETS[kind][2]]
        # construct the left and right from primitives
        left = [Primitive(brackets[0][0])]
        right = [Primitive(brackets[1][0])]
        for _ in range(extensions):
            left.append(Primitive(brackets[0][1]))
            right.append(Primitive(brackets[1][1]))
        left.append(Primitive(brackets[0][2]))
        right.append(Primitive(brackets[1][2]))
        left = Entity(left, 'vert')
        right = Entity(right, 'vert')
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
            hs = []
            for i, elt in enumerate(row):
                widths[i].append(elt.size[0])
                hs.append(elt.size[1])
            heights.append(max(hs))
        widths = [max(w) for w in widths]
        elements = []
        y = 0
        colgap = LINESPACE*0.5
        for i_r, row in enumerate(elmts):
            x = 0
            for i_e, elt in enumerate(row):
                elt.coords = (x + (widths[i_e] - elt.size[0]) / 2, y + (heights[i_r] - elt.size[1]) / 2)
                elements.append(elt)
                x += widths[i_e] + colgap
            y += heights[i_r]
        part = Entity(elements, False)
        part.size = (sum(widths) + colgap*(len(widths) - 1), sum(heights))
        return self.delmtd(part, 1)
      
    def eqarray(self, eqns: list):
        # get max dims: widths1 = widths2, heights
        w_lefts, w_rights, h_top, h_bot = [], [], [], []
        # to get the height above/below the midline
        h = lambda x, top=True: x.size[1]*(x.midline if top else 1-x.midline)
        for line in eqns:
            h_top.append(max([h(line[0]), h(line[1])]))
            h_bot.append(max([h(line[0], False), h(line[1], False)]))
            w_lefts.append(line[0].size[0])
            if len(line) > 1:
                w_rights.append(line[1].size[0])
        w_left = max(w_lefts)
        w_right = max(w_rights)
        # align them to the =
        lines = []
        for i, line in enumerate(eqns):
            elts = [line[0]]
            width = w_left
            line[0].coords = (w_left - line[0].size[0], h_top[i] - h(line[0]))
            if len(line) > 1:
                equals = Primitive(' = ')
                equals.coords = (w_left, h_top[i] - h(equals))
                line[1].coords = (w_left + equals.size[0], h_top[i] - h(line[1]))
                elts += [equals, line[1]]
                width += equals.size[0] + w_right
            ent = Entity(elts, False)
            ent.size = (width, h_top[i] + h_bot[i])
            lines.append(ent)
        return Entity(lines, 'vert')


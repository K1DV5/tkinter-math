"""
Easy classes for renderring maths using Python.

Example:

fraction = Frac(Prime(3), Sum(3, Pow(5, 6)))  # (3'/3+5^6)
fraction.render(canvas)
"""

from abc import ABC
from functools import cache, wraps

from . import core, data
from .core import select_font


class Math(ABC):
    """Just math base class for Other classes."""

    _syntax = None

    @classmethod
    @cache
    def syntax(cls):
        return core.syntax()

    def normalize(obj):
        if isinstance(obj, str):
            if obj.isalpha():
                return Variable(obj).entity
            elif obj.isnumeric():
                return Literal(obj).entity
            else:
                return Primitive(obj)
        elif isinstance(obj, int):
            return core.Primitive(obj)
        elif isinstance(obj, Math):
            return obj.entity
        else:
            return obj

    @property
    def entity(self):
        self.update()
        return self.raw

    def render(self, canv):
        self.update()
        self.raw.render(canv)


class SimpleOperation(Math):
    sign = None
    kind = 0

    def normalize(self, obj):
        if (
            isinstance(obj, Math)
            and not isinstance(obj, BaseLiteral)
            and (not isinstance(obj, SimpleOperation) or obj.kind != self.kind)
        ):
            return Bracket(obj).entity
        else:
            return Math.normalize(obj)

    def __init__(self, *args):
        self.args = args
        self.update()

    def update(self):
        self.raw = core.Primitive(self.sign).join(
            self.normalize(arg) for arg in self.args
        )


class BaseLiteral(Math):
    pass


class Literal(BaseLiteral):
    def __init__(self, val):
        self.val = val

    def update(self):
        self.raw = Primitive(self.val)


class Variable(BaseLiteral):
    def __init__(self, name):
        self.name = name

    def update(self):
        self.raw = Math.syntax().txt(self.name)


class Plus(SimpleOperation):
    sign = core.syntax.plus
    kind = 1


class Minus(SimpleOperation):
    sign = core.syntax.minus
    kind = 1


class Times(SimpleOperation):
    sign = core.syntax.times
    kind = 2


class Div(SimpleOperation):
    sign = core.syntax.div
    kind = 2


class Bracket(Math):
    def __init__(self, content):
        self.content = content

    def update(self):
        self.raw = Math.syntax().delmtd(Math.normalize(self.content))


class Frac(BaseLiteral):
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def update(self):
        self.raw = Math.syntax().frac(
            Math.normalize(self.num), Math.normalize(self.den)
        )


class Pow(BaseLiteral):
    def __init__(self, base, pow):
        self.base = base
        self.pow = pow

    def update(self):
        self.raw = Math.syntax().sup(
            Math.normalize(self.base), Math.normalize(self.pow)
        )


class Prime(BaseLiteral):
    PRIMES = {
        1: "prime",
        2: "2prime",
        3: "3prime",
    }

    def __init__(self, content, level: int = 1):
        self.content = content
        self.level = level

    def update(self):
        self.raw = Math.syntax().prime(
            Math.normalize(self.content), self.PRIMES[self.level]
        )


class Accent(BaseLiteral):
    def __init__(self, base, accent):
        if not accent in data.MATH_ACCENTS:
            raise ValueError(
                f"Wrong accent {accent!r}, must be one of "
                f"{tuple(data.MATH_ACCENTS.keys())!r}"
            )
        self.base = base
        self.accent = accent

    def update(self):
        self.raw = Math.syntax().accent(self.accent, Math.normalize(self.base))


class Eq(Math):
    def __init__(self, *sides):
        if len(sides) < 2:
            raise ValueError(
                f"Eq should receive at least to equation sides, not {len(sides)}"
            )
        self.sides = sides

    def update(self):
        self.raw = Math.syntax().eqarray([map(Math.normalize, self.sides)])

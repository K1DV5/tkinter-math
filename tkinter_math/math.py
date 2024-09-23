"""
Easy classes for rendering maths using Python.

Example:

fraction = Frac(Prime(3), Sum(3, Pow(5, 6)))  # (3'/3+5^6)
fraction.render(canvas)
"""

from abc import ABC
from functools import cache
from typing import Any, Iterable, Union

from . import core, data
from .core import select_font


def set_font(**params):
    """Shorthand to set font."""
    from tkinter.font import Font

    select_font(Font(**params))


class Math(ABC):
    """Base class for mathematical entities."""

    _syntax = None

    @classmethod
    @cache
    def syntax(cls) -> Any:
        """Return the syntax object for mathematical rendering."""
        return core.syntax()

    @staticmethod
    def normalize(obj: Union[str, int, "Math", Any]) -> Any:
        """
        Normalize various input types to a consistent representation.

        :param obj: The object to normalize.

        :returns: Normalized representation of the input object.
        """
        if isinstance(obj, str):
            if obj.isalpha():
                return Variable(obj).entity
            elif obj.isnumeric():
                return Literal(obj).entity
            else:
                return core.Primitive(obj)
        elif isinstance(obj, int):
            return core.Primitive(obj)
        elif isinstance(obj, Math):
            return obj.entity
        else:
            return obj

    @property
    def entity(self) -> Any:
        """Return the underlying entity representation."""
        self.update()
        return self.raw

    def render(self, canv: Any) -> None:
        """
        Render the mathematical entity on the given canvas.

        Args:
            canv: The canvas object to render on.
        """
        self.update()
        self.raw.render(canv)

    def update(self) -> None:
        """Update the internal representation of the mathematical entity."""
        pass


class SimpleOperation(Math):
    """Base class for simple mathematical operations."""

    sign: str = None
    kind: int = 0

    def normalize(self, obj: Any) -> Any:
        """
        Normalize the input object, potentially wrapping it in brackets.

        :param obj: The object to normalize.

        :returns: Normalized representation of the input object.
        """
        if (
            isinstance(obj, Math)
            and not isinstance(obj, BaseLiteral)
            and (not isinstance(obj, SimpleOperation) or obj.kind != self.kind)
        ):
            return Bracket(obj).entity
        else:
            return Math.normalize(obj)

    def __init__(self, *args: Any):
        """
        Initialize the SimpleOperation with given arguments.

        :param *args: Variable number of arguments for the operation.
        """
        self.args = args
        self.update()

    def update(self) -> None:
        """Update the internal representation of the operation."""
        self.raw = core.Primitive(self.sign).join(
            self.normalize(arg) for arg in self.args
        )


class BaseLiteral(Math):
    """Base class for literal mathematical entities."""

    pass


class Literal(BaseLiteral):
    """Represents a literal value in mathematical expressions."""

    def __init__(self, val: Any):
        """
        Initialize the Literal with a given value.

        Args:
            val: The literal value.
        """
        self.val = val

    def update(self) -> None:
        """Update the internal representation of the literal."""
        self.raw = core.Primitive(self.val)


class Variable(BaseLiteral):
    """Represents a variable in mathematical expressions."""

    def __init__(self, name: str):
        """
        Initialize the Variable with a given name.

        Args:
            name: The name of the variable.
        """
        self.name = name

    def update(self) -> None:
        """Update the internal representation of the variable."""
        self.raw = Math.syntax().txt(self.name)


class Greek(Variable):
    """Represents a Greek letter in mathematical expressions."""

    def __init__(self, name: str):
        """
        Initialize the Greek letter with a given name.

        :param name: The name of the Greek letter.

        :raises: ValueError: If the provided name is not a valid Greek letter.
        """
        if name not in data.GREEK_LETTERS:
            raise ValueError(
                f"Invalid Greek letter {name!r} must be one of "
                f"{tuple(data.GREEK_LETTERS.keys())!r}"
            )
        self.name = data.GREEK_LETTERS[name]


class Func(Variable):
    """Represents a function in mathematical expressions."""

    def __init__(self, name: str):
        """
        Initialize the function with a given name.

        Args:
            name: The name of the function.
        """
        self.name = name

    def update(self) -> None:
        """Update the internal representation of the function."""
        self.raw = Math.syntax().func_name(self.name)


class Plus(SimpleOperation):
    """Represents addition in mathematical expressions."""

    sign = core.syntax.plus
    kind = 1


class Minus(SimpleOperation):
    """Represents subtraction in mathematical expressions."""

    sign = core.syntax.minus
    kind = 1


class Times(SimpleOperation):
    """Represents multiplication in mathematical expressions."""

    sign = core.syntax.times
    kind = 2


class Div(SimpleOperation):
    """Represents division in mathematical expressions."""

    sign = core.syntax.div
    kind = 2


class Bracket(Math):
    """Represents bracketed content in mathematical expressions."""

    def __init__(self, content: Any):
        """
        Initialize the Bracket with given content.

        Args:
            content: The content to be enclosed in brackets.
        """
        self.content = content

    def update(self) -> None:
        """Update the internal representation of the bracketed content."""
        self.raw = Math.syntax().delmtd(Math.normalize(self.content))


class Frac(BaseLiteral):
    """Represents a fraction in mathematical expressions."""

    def __init__(self, num: Any, den: Any):
        """
        Initialize the Fraction with numerator and denominator.

        Args:
            num: The numerator of the fraction.
            den: The denominator of the fraction.
        """
        self.num = num
        self.den = den

    def update(self) -> None:
        """Update the internal representation of the fraction."""
        self.raw = Math.syntax().frac(
            Math.normalize(self.num), Math.normalize(self.den)
        )


class Pow(BaseLiteral):
    """Represents exponentiation in mathematical expressions."""

    def __init__(self, base: Any, pow: Any):
        """
        Initialize the Power with base and exponent.

        Args:
            base: The base of the power.
            pow: The exponent of the power.
        """
        self.base = base
        self.pow = pow

    def update(self) -> None:
        """Update the internal representation of the power."""
        base = self.base
        if not isinstance(base, (Prime, Bracket, Func, Greek, Matrix)):
            base = Bracket(base)
        self.raw = Math.syntax().sup(
            Math.normalize(base), Math.normalize(self.pow)
        )


class Prime(BaseLiteral):
    """Represents prime notation in mathematical expressions."""

    PRIMES = {
        1: "prime",
        2: "2prime",
        3: "3prime",
    }

    def __init__(self, content: Any, level: int = 1):
        """
        Initialize the Prime notation.

        Args:
            content: The content to be primed.
            level: The level of prime notation (default is 1).
        """
        self.content = content
        self.level = level

    def update(self) -> None:
        """Update the internal representation of the prime notation."""
        self.raw = Math.syntax().prime(
            Math.normalize(self.content), self.PRIMES[self.level]
        )


class Accent(BaseLiteral):
    """Represents accented symbols in mathematical expressions."""

    def __init__(self, base: Any, accent: str):
        """
        Initialize the Accent.

        :param base: The base symbol to be accented.
        :param accent: The type of accent to apply.

        :raises: ValueError: If the provided accent is not valid.
        """
        if accent not in data.MATH_ACCENTS:
            raise ValueError(
                f"Wrong accent {accent!r}, must be one of "
                f"{tuple(data.MATH_ACCENTS.keys())!r}"
            )
        self.base = base
        self.accent = accent

    def update(self) -> None:
        """Update the internal representation of the accented symbol."""
        self.raw = Math.syntax().accent(self.accent, Math.normalize(self.base))


class Eq(Math):
    """Represents an equation in mathematical expressions."""

    def __init__(self, *sides: Any):
        """
        Initialize the Equation.

        :param *sides: The sides of the equation.

        :raises: ValueError: If fewer than 2 sides are provided or if more than
        2 sides are provided.
        """
        if len(sides) < 2:
            raise ValueError(
                "Eq should receive at least two equation sides, not "
                f"{len(sides)}"
            )
        elif len(sides) > 2:
            raise ValueError(
                "Several sides equations are not yet supported, sorry (╯︿╰)."
            )
        self.sides = sides

    def update(self) -> None:
        """Update the internal representation of the equation."""
        self.raw = Math.syntax().eqarray([map(Math.normalize, self.sides)])


class Matrix(BaseLiteral):
    """Represents a matrix in mathematical expressions."""

    def __init__(self, *rows: Iterable[Iterable[Any]]):
        """
        Initialize the Matrix.

        Args:
            *rows: The rows of the matrix.

        Raises:
            ValueError: If the matrix has inconsistent row lengths.
        """
        size = -1
        try:
            enum_rows = enumerate(rows)
        except TypeError as e:
            raise ValueError(f"Wrong matrix {rows!r}", e) from e
        for idx, row in enum_rows:
            if size == -1:
                size = len(row)
            elif len(row) != size:
                raise ValueError(f"Wrongly shaped matrix row {idx}, {rows!r}.")
        self.rows = rows

    def update(self) -> None:
        """Update the internal representation of the matrix."""
        self.raw = Math.syntax().matrix(
            [[Math.normalize(x) for x in row] for row in self.rows], full=True
        )


class Sigma(BaseLiteral):
    """Represents a summation in mathematical expressions."""

    def __init__(self, base: Any, end: Any):
        """
        Initialize the Summation.

        Args:
            base: The base of the summation.
            end: The end condition of the summation.
        """
        self.base = base
        self.end = end

    def update(self) -> None:
        """Update the internal representation of the summation."""
        self.raw = Math.syntax().summation(
            Math.normalize(self.base), Math.normalize(self.end)
        )


class Sqrt(BaseLiteral):
    """Represents a square root in mathematical expressions."""

    def __init__(self, content: Any):
        """
        Initialize the Square Root.

        Args:
            content: The content under the square root.
        """
        self.content = content

    def update(self) -> None:
        """Update the internal representation of the square root."""
        self.raw = Math.syntax().rad(Math.normalize(self.content))


class Sub(Math):
    """Subscript value."""

    def __init__(self, base: Any, sub: Any):
        self.base = base
        self.sub = sub

    def update(self):
        self.raw = Math.syntax().sub(Math.normalize(self.base), Math.normalize(self.sub))
class Sup(Math):
    """Superscript value."""

    def __init__(self, base: Any, sup: Any):
        self.base = base
        self.sup = sup

    def update(self):
        self.raw = Math.syntax().sup(Math.normalize(self.base), Math.normalize(self.sup))

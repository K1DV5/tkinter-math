# Math

[tkinter_math Index](../README.md#tkinter_math-index) / [Tkinter Math](./index.md#tkinter-math) / Math

> Auto-generated documentation for [tkinter_math.math](../../tkinter_math/math.py) module.

- [Math](#math)
  - [Accent](#accent)
    - [Accent().update](#accent()update)
  - [BaseLiteral](#baseliteral)
  - [Bracket](#bracket)
    - [Bracket().update](#bracket()update)
  - [Div](#div)
  - [Eq](#eq)
    - [Eq().update](#eq()update)
  - [Frac](#frac)
    - [Frac().update](#frac()update)
  - [Func](#func)
    - [Func().update](#func()update)
  - [Greek](#greek)
  - [Literal](#literal)
    - [Literal().update](#literal()update)
  - [Math](#math-1)
    - [Math().entity](#math()entity)
    - [Math.normalize](#mathnormalize)
    - [Math().render](#math()render)
    - [Math.syntax](#mathsyntax)
    - [Math().update](#math()update)
  - [Matrix](#matrix)
    - [Matrix().update](#matrix()update)
  - [Minus](#minus)
  - [Plus](#plus)
  - [Pow](#pow)
    - [Pow().update](#pow()update)
  - [Prime](#prime)
    - [Prime().update](#prime()update)
  - [Sigma](#sigma)
    - [Sigma().update](#sigma()update)
  - [SimpleOperation](#simpleoperation)
    - [SimpleOperation().normalize](#simpleoperation()normalize)
    - [SimpleOperation().update](#simpleoperation()update)
  - [Sqrt](#sqrt)
    - [Sqrt().update](#sqrt()update)
  - [Sub](#sub)
    - [Sub().update](#sub()update)
  - [Sup](#sup)
    - [Sup().update](#sup()update)
  - [Times](#times)
  - [Variable](#variable)
    - [Variable().update](#variable()update)
  - [set_font](#set_font)

## Accent

[Show source in math.py:312](../../tkinter_math/math.py#L312)

Represents accented symbols in mathematical expressions.

#### Signature

```python
class Accent(BaseLiteral):
    def __init__(self, base: Any, accent: str): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Accent().update

[Show source in math.py:332](../../tkinter_math/math.py#L332)

Update the internal representation of the accented symbol.

#### Signature

```python
def update(self) -> None: ...
```



## BaseLiteral

[Show source in math.py:119](../../tkinter_math/math.py#L119)

Base class for literal mathematical entities.

#### Signature

```python
class BaseLiteral(Math): ...
```

#### See also

- [Math](#math)



## Bracket

[Show source in math.py:223](../../tkinter_math/math.py#L223)

Represents bracketed content in mathematical expressions.

#### Signature

```python
class Bracket(Math):
    def __init__(self, content: Any): ...
```

#### See also

- [Math](#math)

### Bracket().update

[Show source in math.py:235](../../tkinter_math/math.py#L235)

Update the internal representation of the bracketed content.

#### Signature

```python
def update(self) -> None: ...
```



## Div

[Show source in math.py:216](../../tkinter_math/math.py#L216)

Represents division in mathematical expressions.

#### Signature

```python
class Div(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Eq

[Show source in math.py:337](../../tkinter_math/math.py#L337)

Represents an equation in mathematical expressions.

#### Signature

```python
class Eq(Math):
    def __init__(self, *sides: Any): ...
```

#### See also

- [Math](#math)

### Eq().update

[Show source in math.py:360](../../tkinter_math/math.py#L360)

Update the internal representation of the equation.

#### Signature

```python
def update(self) -> None: ...
```



## Frac

[Show source in math.py:240](../../tkinter_math/math.py#L240)

Represents a fraction in mathematical expressions.

#### Signature

```python
class Frac(BaseLiteral):
    def __init__(self, num: Any, den: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Frac().update

[Show source in math.py:254](../../tkinter_math/math.py#L254)

Update the internal representation of the fraction.

#### Signature

```python
def update(self) -> None: ...
```



## Func

[Show source in math.py:178](../../tkinter_math/math.py#L178)

Represents a function in mathematical expressions.

#### Signature

```python
class Func(Variable):
    def __init__(self, name: str): ...
```

#### See also

- [Variable](#variable)

### Func().update

[Show source in math.py:190](../../tkinter_math/math.py#L190)

Update the internal representation of the function.

#### Signature

```python
def update(self) -> None: ...
```



## Greek

[Show source in math.py:159](../../tkinter_math/math.py#L159)

Represents a Greek letter in mathematical expressions.

#### Signature

```python
class Greek(Variable):
    def __init__(self, name: str): ...
```

#### See also

- [Variable](#variable)



## Literal

[Show source in math.py:125](../../tkinter_math/math.py#L125)

Represents a literal value in mathematical expressions.

#### Signature

```python
class Literal(BaseLiteral):
    def __init__(self, val: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Literal().update

[Show source in math.py:137](../../tkinter_math/math.py#L137)

Update the internal representation of the literal.

#### Signature

```python
def update(self) -> None: ...
```



## Math

[Show source in math.py:25](../../tkinter_math/math.py#L25)

Base class for mathematical entities.

#### Signature

```python
class Math(ABC): ...
```

### Math().entity

[Show source in math.py:59](../../tkinter_math/math.py#L59)

Return the underlying entity representation.

#### Signature

```python
@property
def entity(self) -> Any: ...
```

### Math.normalize

[Show source in math.py:36](../../tkinter_math/math.py#L36)

Normalize various input types to a consistent representation.

#### Arguments

- `obj` - The object to normalize.

#### Returns

Normalized representation of the input object.

#### Signature

```python
@staticmethod
def normalize(obj: Union[str, int, "Math", Any]) -> Any: ...
```

### Math().render

[Show source in math.py:65](../../tkinter_math/math.py#L65)

Render the mathematical entity on the given canvas.

#### Arguments

- `canv` - The canvas object to render on.

#### Signature

```python
def render(self, canv: Any) -> None: ...
```

### Math.syntax

[Show source in math.py:30](../../tkinter_math/math.py#L30)

Return the syntax object for mathematical rendering.

#### Signature

```python
@classmethod
@cache
def syntax(cls) -> Any: ...
```

### Math().update

[Show source in math.py:75](../../tkinter_math/math.py#L75)

Update the internal representation of the mathematical entity.

#### Signature

```python
def update(self) -> None: ...
```



## Matrix

[Show source in math.py:365](../../tkinter_math/math.py#L365)

Represents a matrix in mathematical expressions.

#### Signature

```python
class Matrix(BaseLiteral):
    def __init__(self, *rows: Iterable[Iterable[Any]]): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Matrix().update

[Show source in math.py:390](../../tkinter_math/math.py#L390)

Update the internal representation of the matrix.

#### Signature

```python
def update(self) -> None: ...
```



## Minus

[Show source in math.py:202](../../tkinter_math/math.py#L202)

Represents subtraction in mathematical expressions.

#### Signature

```python
class Minus(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Plus

[Show source in math.py:195](../../tkinter_math/math.py#L195)

Represents addition in mathematical expressions.

#### Signature

```python
class Plus(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Pow

[Show source in math.py:261](../../tkinter_math/math.py#L261)

Represents exponentiation in mathematical expressions.

#### Signature

```python
class Pow(BaseLiteral):
    def __init__(self, base: Any, pow: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Pow().update

[Show source in math.py:275](../../tkinter_math/math.py#L275)

Update the internal representation of the power.

#### Signature

```python
def update(self) -> None: ...
```



## Prime

[Show source in math.py:285](../../tkinter_math/math.py#L285)

Represents prime notation in mathematical expressions.

#### Signature

```python
class Prime(BaseLiteral):
    def __init__(self, content: Any, level: int = 1): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Prime().update

[Show source in math.py:305](../../tkinter_math/math.py#L305)

Update the internal representation of the prime notation.

#### Signature

```python
def update(self) -> None: ...
```



## Sigma

[Show source in math.py:397](../../tkinter_math/math.py#L397)

Represents a summation in mathematical expressions.

#### Signature

```python
class Sigma(BaseLiteral):
    def __init__(self, base: Any, end: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Sigma().update

[Show source in math.py:411](../../tkinter_math/math.py#L411)

Update the internal representation of the summation.

#### Signature

```python
def update(self) -> None: ...
```



## SimpleOperation

[Show source in math.py:80](../../tkinter_math/math.py#L80)

Base class for simple mathematical operations.

#### Signature

```python
class SimpleOperation(Math):
    def __init__(self, *args: Any): ...
```

#### See also

- [Math](#math)

### SimpleOperation().normalize

[Show source in math.py:86](../../tkinter_math/math.py#L86)

Normalize the input object, potentially wrapping it in brackets.

#### Arguments

- `obj` - The object to normalize.

#### Returns

Normalized representation of the input object.

#### Signature

```python
def normalize(self, obj: Any) -> Any: ...
```

### SimpleOperation().update

[Show source in math.py:112](../../tkinter_math/math.py#L112)

Update the internal representation of the operation.

#### Signature

```python
def update(self) -> None: ...
```



## Sqrt

[Show source in math.py:418](../../tkinter_math/math.py#L418)

Represents a square root in mathematical expressions.

#### Signature

```python
class Sqrt(BaseLiteral):
    def __init__(self, content: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Sqrt().update

[Show source in math.py:430](../../tkinter_math/math.py#L430)

Update the internal representation of the square root.

#### Signature

```python
def update(self) -> None: ...
```



## Sub

[Show source in math.py:435](../../tkinter_math/math.py#L435)

Subscript value.

#### Signature

```python
class Sub(Math):
    def __init__(self, base: Any, sub: Any): ...
```

#### See also

- [Math](#math)

### Sub().update

[Show source in math.py:442](../../tkinter_math/math.py#L442)

#### Signature

```python
def update(self): ...
```



## Sup

[Show source in math.py:444](../../tkinter_math/math.py#L444)

Superscript value.

#### Signature

```python
class Sup(Math):
    def __init__(self, base: Any, sup: Any): ...
```

#### See also

- [Math](#math)

### Sup().update

[Show source in math.py:451](../../tkinter_math/math.py#L451)

#### Signature

```python
def update(self): ...
```



## Times

[Show source in math.py:209](../../tkinter_math/math.py#L209)

Represents multiplication in mathematical expressions.

#### Signature

```python
class Times(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Variable

[Show source in math.py:142](../../tkinter_math/math.py#L142)

Represents a variable in mathematical expressions.

#### Signature

```python
class Variable(BaseLiteral):
    def __init__(self, name: str): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Variable().update

[Show source in math.py:154](../../tkinter_math/math.py#L154)

Update the internal representation of the variable.

#### Signature

```python
def update(self) -> None: ...
```



## set_font

[Show source in math.py:18](../../tkinter_math/math.py#L18)

Shorthand to set font.

#### Signature

```python
def set_font(**params): ...
```
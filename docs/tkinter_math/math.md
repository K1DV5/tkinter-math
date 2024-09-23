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
  - [Times](#times)
  - [Variable](#variable)
    - [Variable().update](#variable()update)

## Accent

[Show source in math.py:308](../../tkinter_math/math.py#L308)

Represents accented symbols in mathematical expressions.

#### Signature

```python
class Accent(BaseLiteral):
    def __init__(self, base: Any, accent: str): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Accent().update

[Show source in math.py:330](../../tkinter_math/math.py#L330)

Update the internal representation of the accented symbol.

#### Signature

```python
def update(self) -> None: ...
```



## BaseLiteral

[Show source in math.py:117](../../tkinter_math/math.py#L117)

Base class for literal mathematical entities.

#### Signature

```python
class BaseLiteral(Math): ...
```

#### See also

- [Math](#math)



## Bracket

[Show source in math.py:222](../../tkinter_math/math.py#L222)

Represents bracketed content in mathematical expressions.

#### Signature

```python
class Bracket(Math):
    def __init__(self, content: Any): ...
```

#### See also

- [Math](#math)

### Bracket().update

[Show source in math.py:234](../../tkinter_math/math.py#L234)

Update the internal representation of the bracketed content.

#### Signature

```python
def update(self) -> None: ...
```



## Div

[Show source in math.py:215](../../tkinter_math/math.py#L215)

Represents division in mathematical expressions.

#### Signature

```python
class Div(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Eq

[Show source in math.py:335](../../tkinter_math/math.py#L335)

Represents an equation in mathematical expressions.

#### Signature

```python
class Eq(Math):
    def __init__(self, *sides: Any): ...
```

#### See also

- [Math](#math)

### Eq().update

[Show source in math.py:358](../../tkinter_math/math.py#L358)

Update the internal representation of the equation.

#### Signature

```python
def update(self) -> None: ...
```



## Frac

[Show source in math.py:239](../../tkinter_math/math.py#L239)

Represents a fraction in mathematical expressions.

#### Signature

```python
class Frac(BaseLiteral):
    def __init__(self, num: Any, den: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Frac().update

[Show source in math.py:253](../../tkinter_math/math.py#L253)

Update the internal representation of the fraction.

#### Signature

```python
def update(self) -> None: ...
```



## Func

[Show source in math.py:177](../../tkinter_math/math.py#L177)

Represents a function in mathematical expressions.

#### Signature

```python
class Func(Variable):
    def __init__(self, name: str): ...
```

#### See also

- [Variable](#variable)

### Func().update

[Show source in math.py:189](../../tkinter_math/math.py#L189)

Update the internal representation of the function.

#### Signature

```python
def update(self) -> None: ...
```



## Greek

[Show source in math.py:157](../../tkinter_math/math.py#L157)

Represents a Greek letter in mathematical expressions.

#### Signature

```python
class Greek(Variable):
    def __init__(self, name: str): ...
```

#### See also

- [Variable](#variable)



## Literal

[Show source in math.py:123](../../tkinter_math/math.py#L123)

Represents a literal value in mathematical expressions.

#### Signature

```python
class Literal(BaseLiteral):
    def __init__(self, val: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Literal().update

[Show source in math.py:135](../../tkinter_math/math.py#L135)

Update the internal representation of the literal.

#### Signature

```python
def update(self) -> None: ...
```



## Math

[Show source in math.py:18](../../tkinter_math/math.py#L18)

Base class for mathematical entities.

#### Signature

```python
class Math(ABC): ...
```

### Math().entity

[Show source in math.py:54](../../tkinter_math/math.py#L54)

Return the underlying entity representation.

#### Signature

```python
@property
def entity(self) -> Any: ...
```

### Math.normalize

[Show source in math.py:29](../../tkinter_math/math.py#L29)

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

[Show source in math.py:60](../../tkinter_math/math.py#L60)

Render the mathematical entity on the given canvas.

#### Arguments

- `canv` - The canvas object to render on.

#### Signature

```python
def render(self, canv: Any) -> None: ...
```

### Math.syntax

[Show source in math.py:23](../../tkinter_math/math.py#L23)

Return the syntax object for mathematical rendering.

#### Signature

```python
@classmethod
@cache
def syntax(cls) -> Any: ...
```

### Math().update

[Show source in math.py:70](../../tkinter_math/math.py#L70)

Update the internal representation of the mathematical entity.

#### Signature

```python
def update(self) -> None: ...
```



## Matrix

[Show source in math.py:363](../../tkinter_math/math.py#L363)

Represents a matrix in mathematical expressions.

#### Signature

```python
class Matrix(BaseLiteral):
    def __init__(self, *rows: Tuple[Any, ...]): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Matrix().update

[Show source in math.py:388](../../tkinter_math/math.py#L388)

Update the internal representation of the matrix.

#### Signature

```python
def update(self) -> None: ...
```



## Minus

[Show source in math.py:201](../../tkinter_math/math.py#L201)

Represents subtraction in mathematical expressions.

#### Signature

```python
class Minus(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Plus

[Show source in math.py:194](../../tkinter_math/math.py#L194)

Represents addition in mathematical expressions.

#### Signature

```python
class Plus(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Pow

[Show source in math.py:260](../../tkinter_math/math.py#L260)

Represents exponentiation in mathematical expressions.

#### Signature

```python
class Pow(BaseLiteral):
    def __init__(self, base: Any, pow: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Pow().update

[Show source in math.py:274](../../tkinter_math/math.py#L274)

Update the internal representation of the power.

#### Signature

```python
def update(self) -> None: ...
```



## Prime

[Show source in math.py:281](../../tkinter_math/math.py#L281)

Represents prime notation in mathematical expressions.

#### Signature

```python
class Prime(BaseLiteral):
    def __init__(self, content: Any, level: int = 1): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Prime().update

[Show source in math.py:301](../../tkinter_math/math.py#L301)

Update the internal representation of the prime notation.

#### Signature

```python
def update(self) -> None: ...
```



## Sigma

[Show source in math.py:395](../../tkinter_math/math.py#L395)

Represents a summation in mathematical expressions.

#### Signature

```python
class Sigma(BaseLiteral):
    def __init__(self, base: Any, end: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Sigma().update

[Show source in math.py:409](../../tkinter_math/math.py#L409)

Update the internal representation of the summation.

#### Signature

```python
def update(self) -> None: ...
```



## SimpleOperation

[Show source in math.py:75](../../tkinter_math/math.py#L75)

Base class for simple mathematical operations.

#### Signature

```python
class SimpleOperation(Math):
    def __init__(self, *args: Any): ...
```

#### See also

- [Math](#math)

### SimpleOperation().normalize

[Show source in math.py:81](../../tkinter_math/math.py#L81)

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

[Show source in math.py:110](../../tkinter_math/math.py#L110)

Update the internal representation of the operation.

#### Signature

```python
def update(self) -> None: ...
```



## Sqrt

[Show source in math.py:416](../../tkinter_math/math.py#L416)

Represents a square root in mathematical expressions.

#### Signature

```python
class Sqrt(BaseLiteral):
    def __init__(self, content: Any): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Sqrt().update

[Show source in math.py:428](../../tkinter_math/math.py#L428)

Update the internal representation of the square root.

#### Signature

```python
def update(self) -> None: ...
```



## Times

[Show source in math.py:208](../../tkinter_math/math.py#L208)

Represents multiplication in mathematical expressions.

#### Signature

```python
class Times(SimpleOperation): ...
```

#### See also

- [SimpleOperation](#simpleoperation)



## Variable

[Show source in math.py:140](../../tkinter_math/math.py#L140)

Represents a variable in mathematical expressions.

#### Signature

```python
class Variable(BaseLiteral):
    def __init__(self, name: str): ...
```

#### See also

- [BaseLiteral](#baseliteral)

### Variable().update

[Show source in math.py:152](../../tkinter_math/math.py#L152)

Update the internal representation of the variable.

#### Signature

```python
def update(self) -> None: ...
```
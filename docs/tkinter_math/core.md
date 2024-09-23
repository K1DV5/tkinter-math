# Core

[tkinter_math Index](../README.md#tkinter_math-index) / [Tkinter Math](./index.md#tkinter-math) / Core

> Auto-generated documentation for [tkinter_math.core](../../tkinter_math/core.py) module.

- [Core](#core)
  - [Entity](#entity)
    - [Entity().__add__](#entity()__add__)
    - [Entity().__repr__](#entity()__repr__)
    - [Entity().arrange](#entity()arrange)
    - [Entity().pull_size](#entity()pull_size)
    - [Entity().render](#entity()render)
  - [Primitive](#primitive)
    - [Primitive().__add__](#primitive()__add__)
    - [Primitive().__repr__](#primitive()__repr__)
    - [Primitive().join](#primitive()join)
    - [Primitive().pull_size](#primitive()pull_size)
    - [Primitive().render](#primitive()render)
    - [Primitive().set_size](#primitive()set_size)
    - [Primitive().split](#primitive()split)
  - [syntax](#syntax)
    - [syntax()._arrange_matrix](#syntax()_arrange_matrix)
    - [syntax().accent](#syntax()accent)
    - [syntax().arrange_accent](#syntax()arrange_accent)
    - [syntax().arrange_eqarray](#syntax()arrange_eqarray)
    - [syntax().arrange_frac](#syntax()arrange_frac)
    - [syntax().arrange_rad](#syntax()arrange_rad)
    - [syntax().arrange_sub](#syntax()arrange_sub)
    - [syntax().arrange_sup](#syntax()arrange_sup)
    - [syntax().delmtd](#syntax()delmtd)
    - [syntax().eqarray](#syntax()eqarray)
    - [syntax().frac](#syntax()frac)
    - [syntax().func_name](#syntax()func_name)
    - [syntax().greek](#syntax()greek)
    - [syntax().math_disp](#syntax()math_disp)
    - [syntax().math_inln](#syntax()math_inln)
    - [syntax().matrix](#syntax()matrix)
    - [syntax().prime](#syntax()prime)
    - [syntax().rad](#syntax()rad)
    - [syntax().sub](#syntax()sub)
    - [syntax().summation](#syntax()summation)
    - [syntax().sup](#syntax()sup)
    - [syntax().transformed](#syntax()transformed)
    - [syntax().txt](#syntax()txt)
    - [syntax().txt_math](#syntax()txt_math)
    - [syntax().txt_rom](#syntax()txt_rom)
  - [calculate_linespace](#calculate_linespace)
  - [select_font](#select_font)

## Entity

[Show source in core.py:208](../../tkinter_math/core.py#L208)

combination of text, line, (primitives) or other entities

#### Signature

```python
class Entity:
    def __init__(self, content: Iterable, arrange: Arrangement = "horiz"): ...
```

#### See also

- [Arrangement](#arrangement)

### Entity().__add__

[Show source in core.py:268](../../tkinter_math/core.py#L268)

Merge other Entity or add other primitive.

#### Signature

```python
def __add__(self, other: "Primitive | Entity") -> "Entity": ...
```

### Entity().__repr__

[Show source in core.py:278](../../tkinter_math/core.py#L278)

Reproducs the entity as string.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Entity().arrange

[Show source in core.py:225](../../tkinter_math/core.py#L225)

Arrange entity's content deppending on arrangement.

#### Signature

```python
def arrange(self): ...
```

### Entity().pull_size

[Show source in core.py:256](../../tkinter_math/core.py#L256)

Pull contents sizes and arranges entity.

#### Signature

```python
def pull_size(self, to: int | float): ...
```

### Entity().render

[Show source in core.py:262](../../tkinter_math/core.py#L262)

Render the Entities on specified canvas.

#### Signature

```python
def render(self, canvas): ...
```



## Primitive

[Show source in core.py:38](../../tkinter_math/core.py#L38)

Text and line.

#### Signature

```python
class Primitive:
    def __init__(self, content: str, kind: PrimitiveKind = "t", **kwargs): ...
```

#### See also

- [PrimitiveKind](#primitivekind)

### Primitive().__add__

[Show source in core.py:186](../../tkinter_math/core.py#L186)

Add other primitive or entity.

#### Signature

```python
def __add__(self, other: "Primitive | Entity") -> "Entity": ...
```

### Primitive().__repr__

[Show source in core.py:202](../../tkinter_math/core.py#L202)

Reproduce the primitive as string.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Primitive().join

[Show source in core.py:195](../../tkinter_math/core.py#L195)

Join the passed Primitives or Entities.

#### Signature

```python
def join(self, others: "Iterable[Primitive | Entity]") -> "Entity": ...
```

### Primitive().pull_size

[Show source in core.py:102](../../tkinter_math/core.py#L102)

Pull the primitive size and position to specified value.

#### Signature

```python
def pull_size(self, to: int | float): ...
```

### Primitive().render

[Show source in core.py:130](../../tkinter_math/core.py#L130)

Render the primitive on canvas.

#### Signature

```python
def render(self, canvas: Any): ...
```

### Primitive().set_size

[Show source in core.py:112](../../tkinter_math/core.py#L112)

Resize the primitive coords size modifying width or height.

#### Signature

```python
def set_size(
    self, width: Optional[int | float] = None, height: Optional[int | float] = None
): ...
```

### Primitive().split

[Show source in core.py:177](../../tkinter_math/core.py#L177)

Split primitive content to create other primitives.

#### Signature

```python
def split(self, string: str) -> "Optional[list[Primitive]]": ...
```



## syntax

[Show source in core.py:283](../../tkinter_math/core.py#L283)

Some symbols and helper methods.

#### Signature

```python
class syntax: ...
```

### syntax()._arrange_matrix

[Show source in core.py:552](../../tkinter_math/core.py#L552)

Arrange matrix Primitive or Entity.

#### Signature

```python
def _arrange_matrix(self, matrix, cols): ...
```

### syntax().accent

[Show source in core.py:461](../../tkinter_math/core.py#L461)

Create a mathematical accent.

#### Signature

```python
def accent(self, acc: str, base: Primitive | Entity) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().arrange_accent

[Show source in core.py:453](../../tkinter_math/core.py#L453)

Arrange an accent Primitive.

#### Signature

```python
def arrange_accent(self, accent: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_eqarray

[Show source in core.py:605](../../tkinter_math/core.py#L605)

#### Signature

```python
def arrange_eqarray(self, eqarray): ...
```

### syntax().arrange_frac

[Show source in core.py:419](../../tkinter_math/core.py#L419)

Arrange a fraction primitive.

#### Signature

```python
def arrange_frac(self, frac: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_rad

[Show source in core.py:364](../../tkinter_math/core.py#L364)

Arrange radian Primitive.

#### Signature

```python
def arrange_rad(self, rad: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_sub

[Show source in core.py:350](../../tkinter_math/core.py#L350)

Arrange subscript primitive.

#### Signature

```python
def arrange_sub(self, sub: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_sup

[Show source in core.py:332](../../tkinter_math/core.py#L332)

Arrange superscript Primitive.

#### Signature

```python
def arrange_sup(self, sup: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().delmtd

[Show source in core.py:470](../../tkinter_math/core.py#L470)

Wrap `contained` into brackets specified by `kind`

#### Signature

```python
def delmtd(self, contained, kind: BracketKind = 0) -> Entity: ...
```

#### See also

- [BracketKind](#bracketkind)
- [Entity](#entity)

### syntax().eqarray

[Show source in core.py:641](../../tkinter_math/core.py#L641)

#### Signature

```python
def eqarray(self, eqns: list): ...
```

### syntax().frac

[Show source in core.py:435](../../tkinter_math/core.py#L435)

Create a fraction Entity.

#### Signature

```python
def frac(self, num: Entity | Primitive, den: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().func_name

[Show source in core.py:415](../../tkinter_math/core.py#L415)

Create a function name entity.

#### Signature

```python
def func_name(self, name: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)

### syntax().greek

[Show source in core.py:449](../../tkinter_math/core.py#L449)

Create greek letter Primitive.

#### Signature

```python
def greek(self, name: str): ...
```

### syntax().math_disp

[Show source in core.py:443](../../tkinter_math/core.py#L443)

#### Signature

```python
def math_disp(self, math): ...
```

### syntax().math_inln

[Show source in core.py:446](../../tkinter_math/core.py#L446)

#### Signature

```python
def math_inln(self, math): ...
```

### syntax().matrix

[Show source in core.py:584](../../tkinter_math/core.py#L584)

#### Signature

```python
def matrix(
    self, elmts: list[list[Entity | Primitive]] | list[Entity | Primitive], full=False
): ...
```

### syntax().prime

[Show source in core.py:466](../../tkinter_math/core.py#L466)

Create a primed Entity or Primitive.

#### Signature

```python
def prime(self, base: Primitive | Entity, prime: str) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().rad

[Show source in core.py:374](../../tkinter_math/core.py#L374)

Create a radian from primitive.

#### Signature

```python
def rad(self, base: Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)
- [Primitive](#primitive)

### syntax().sub

[Show source in core.py:359](../../tkinter_math/core.py#L359)

Convert to subscript.

#### Signature

```python
def sub(self, base: Entity | Primitive, sub: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().summation

[Show source in core.py:397](../../tkinter_math/core.py#L397)

Create summation entity.

#### Signature

```python
def summation(
    self,
    base: Entity | Primitive,
    end: Entity | Primitive,
    begin: Primitive | Entity | type(None) = None,
) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().sup

[Show source in core.py:345](../../tkinter_math/core.py#L345)

Converts to superscript.

#### Signature

```python
def sup(self, base: Entity | Primitive, sup: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().transformed

[Show source in core.py:305](../../tkinter_math/core.py#L305)

Things that are transformed, used for units and such.

#### Signature

```python
@property
def transformed(self) -> dict[str]: ...
```

### syntax().txt

[Show source in core.py:315](../../tkinter_math/core.py#L315)

The primitive representation of `text`.

#### Signature

```python
def txt(self, text: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)

### syntax().txt_math

[Show source in core.py:329](../../tkinter_math/core.py#L329)

#### Signature

```python
def txt_math(self, text: str): ...
```

### syntax().txt_rom

[Show source in core.py:325](../../tkinter_math/core.py#L325)

Primitive of the text with slant='roman'.

#### Signature

```python
def txt_rom(self, text: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)



## calculate_linespace

[Show source in core.py:19](../../tkinter_math/core.py#L19)

Calculate linespace for a font.

#### Signature

```python
def calculate_linespace(font: Font) -> list: ...
```

#### See also

- [Font](#font)



## select_font

[Show source in core.py:29](../../tkinter_math/core.py#L29)

Use this before doing anything using this module.

#### Signature

```python
def select_font(font: Font): ...
```

#### See also

- [Font](#font)
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

[Show source in core.py:206](../../tkinter_math/core.py#L206)

combination of text, line, (primitives) or other entities

#### Signature

```python
class Entity:
    def __init__(self, content: Iterable, arrange: Arrangement = "horiz"): ...
```

#### See also

- [Arrangement](#arrangement)

### Entity().__add__

[Show source in core.py:266](../../tkinter_math/core.py#L266)

Merge other Entity or add other primitive.

#### Signature

```python
def __add__(self, other: "Primitive | Entity") -> "Entity": ...
```

### Entity().__repr__

[Show source in core.py:276](../../tkinter_math/core.py#L276)

Reproducs the entity as string.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Entity().arrange

[Show source in core.py:223](../../tkinter_math/core.py#L223)

Arrange entity's content deppending on arrangement.

#### Signature

```python
def arrange(self): ...
```

### Entity().pull_size

[Show source in core.py:254](../../tkinter_math/core.py#L254)

Pull contents sizes and arranges entity.

#### Signature

```python
def pull_size(self, to: int | float): ...
```

### Entity().render

[Show source in core.py:260](../../tkinter_math/core.py#L260)

Render the Entities on specified canvas.

#### Signature

```python
def render(self, canvas): ...
```



## Primitive

[Show source in core.py:37](../../tkinter_math/core.py#L37)

Text and line.

#### Signature

```python
class Primitive:
    def __init__(self, content: str, kind: PrimitiveKind = "t", **kwargs): ...
```

#### See also

- [PrimitiveKind](#primitivekind)

### Primitive().__add__

[Show source in core.py:184](../../tkinter_math/core.py#L184)

Add other primitive or entity.

#### Signature

```python
def __add__(self, other: "Primitive | Entity") -> "Entity": ...
```

### Primitive().__repr__

[Show source in core.py:200](../../tkinter_math/core.py#L200)

Reproduce the primitive as string.

#### Signature

```python
def __repr__(self) -> str: ...
```

### Primitive().join

[Show source in core.py:193](../../tkinter_math/core.py#L193)

Join the passed Primitives or Entities.

#### Signature

```python
def join(self, others: "Iterable[Primitive | Entity]") -> "Entity": ...
```

### Primitive().pull_size

[Show source in core.py:100](../../tkinter_math/core.py#L100)

Pull the primitive size and position to specified value.

#### Signature

```python
def pull_size(self, to: int | float): ...
```

### Primitive().render

[Show source in core.py:128](../../tkinter_math/core.py#L128)

Render the primitive on canvas.

#### Signature

```python
def render(self, canvas: Any): ...
```

### Primitive().set_size

[Show source in core.py:110](../../tkinter_math/core.py#L110)

Resize the primitive coords size modifying width or height.

#### Signature

```python
def set_size(
    self, width: Optional[int | float] = None, height: Optional[int | float] = None
): ...
```

### Primitive().split

[Show source in core.py:175](../../tkinter_math/core.py#L175)

Split primitive content to create other primitives.

#### Signature

```python
def split(self, string: str) -> "Optional[list[Primitive]]": ...
```



## syntax

[Show source in core.py:281](../../tkinter_math/core.py#L281)

Some symbols and helper methods.

#### Signature

```python
class syntax: ...
```

### syntax()._arrange_matrix

[Show source in core.py:546](../../tkinter_math/core.py#L546)

Arrange matrix Primitive or Entity.

#### Signature

```python
def _arrange_matrix(self, matrix, cols): ...
```

### syntax().accent

[Show source in core.py:455](../../tkinter_math/core.py#L455)

Create a mathematical accent.

#### Signature

```python
def accent(self, acc: str, base: Primitive | Entity) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().arrange_accent

[Show source in core.py:447](../../tkinter_math/core.py#L447)

Arrange an accent Primitive.

#### Signature

```python
def arrange_accent(self, accent: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_eqarray

[Show source in core.py:599](../../tkinter_math/core.py#L599)

#### Signature

```python
def arrange_eqarray(self, eqarray): ...
```

### syntax().arrange_frac

[Show source in core.py:413](../../tkinter_math/core.py#L413)

Arrange a fraction primitive.

#### Signature

```python
def arrange_frac(self, frac: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_rad

[Show source in core.py:362](../../tkinter_math/core.py#L362)

Arrange radian Primitive.

#### Signature

```python
def arrange_rad(self, rad: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_sub

[Show source in core.py:348](../../tkinter_math/core.py#L348)

Arrange subscript primitive.

#### Signature

```python
def arrange_sub(self, sub: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().arrange_sup

[Show source in core.py:330](../../tkinter_math/core.py#L330)

Arrange superscript Primitive.

#### Signature

```python
def arrange_sup(self, sup: Primitive): ...
```

#### See also

- [Primitive](#primitive)

### syntax().delmtd

[Show source in core.py:464](../../tkinter_math/core.py#L464)

Wrap `contained` into brackets specified by `kind`

#### Signature

```python
def delmtd(self, contained, kind: BracketKind = 0) -> Entity: ...
```

#### See also

- [BracketKind](#bracketkind)
- [Entity](#entity)

### syntax().eqarray

[Show source in core.py:635](../../tkinter_math/core.py#L635)

#### Signature

```python
def eqarray(self, eqns: list): ...
```

### syntax().frac

[Show source in core.py:429](../../tkinter_math/core.py#L429)

Create a fraction Entity.

#### Signature

```python
def frac(self, num: Entity | Primitive, den: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().func_name

[Show source in core.py:409](../../tkinter_math/core.py#L409)

Create a function name entity.

#### Signature

```python
def func_name(self, name: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)

### syntax().greek

[Show source in core.py:443](../../tkinter_math/core.py#L443)

Create greek letter Primitive.

#### Signature

```python
def greek(self, name: str): ...
```

### syntax().math_disp

[Show source in core.py:437](../../tkinter_math/core.py#L437)

#### Signature

```python
def math_disp(self, math): ...
```

### syntax().math_inln

[Show source in core.py:440](../../tkinter_math/core.py#L440)

#### Signature

```python
def math_inln(self, math): ...
```

### syntax().matrix

[Show source in core.py:578](../../tkinter_math/core.py#L578)

#### Signature

```python
def matrix(
    self, elmts: list[list[Entity | Primitive]] | list[Entity | Primitive], full=False
): ...
```

### syntax().prime

[Show source in core.py:460](../../tkinter_math/core.py#L460)

Create a primed Entity or Primitive.

#### Signature

```python
def prime(self, base: Primitive | Entity, prime: str) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().rad

[Show source in core.py:372](../../tkinter_math/core.py#L372)

Create a radian from primitive.

#### Signature

```python
def rad(self, base: Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)
- [Primitive](#primitive)

### syntax().sub

[Show source in core.py:357](../../tkinter_math/core.py#L357)

Convert to subscript.

#### Signature

```python
def sub(self, base: Entity | Primitive, sub: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().summation

[Show source in core.py:395](../../tkinter_math/core.py#L395)

Create summation entity.

#### Signature

```python
def summation(self, base: Entity | Primitive, end: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().sup

[Show source in core.py:343](../../tkinter_math/core.py#L343)

Converts to superscript.

#### Signature

```python
def sup(self, base: Entity | Primitive, sup: Entity | Primitive) -> Entity: ...
```

#### See also

- [Entity](#entity)

### syntax().transformed

[Show source in core.py:303](../../tkinter_math/core.py#L303)

Things that are transformed, used for units and such.

#### Signature

```python
@property
def transformed(self) -> dict[str]: ...
```

### syntax().txt

[Show source in core.py:313](../../tkinter_math/core.py#L313)

The primitive representation of `text`.

#### Signature

```python
def txt(self, text: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)

### syntax().txt_math

[Show source in core.py:327](../../tkinter_math/core.py#L327)

#### Signature

```python
def txt_math(self, text: str): ...
```

### syntax().txt_rom

[Show source in core.py:323](../../tkinter_math/core.py#L323)

Primitive of the text with slant='roman'.

#### Signature

```python
def txt_rom(self, text: str) -> Primitive: ...
```

#### See also

- [Primitive](#primitive)



## calculate_linespace

[Show source in core.py:18](../../tkinter_math/core.py#L18)

Calculate linespace for a font.

#### Signature

```python
def calculate_linespace(font: Font) -> list: ...
```

#### See also

- [Font](#font)



## select_font

[Show source in core.py:28](../../tkinter_math/core.py#L28)

Use this before doing anything using this module.

#### Signature

```python
def select_font(font: Font): ...
```

#### See also

- [Font](#font)
---
tag: YWT3N8DA3J
kind: example
name: Over C the forms x² + y² and xy are equivalent
msc: ["11E04", 15A63]
topics: [6TSCEW8QMK]
audience: ug1
instance_of: [0RBQS1JJCR]
illustrates: [0CEX9BRXRZ]
uses: [0CEX9BRXRZ, 0HZNE5QZDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Equivalence of forms
---

## Example

Let $Q_1(x, y) = xy$ and $Q_2(s, t) = s^2 + t^2$ on $\C^2$.

1. Put $x = s + it$ and $y = s - it$.
2. Then $xy = (s + it)(s - it) = s^2 - i^2 t^2 = s^2 + t^2$.
3. The change of variables has matrix $\begin{pmatrix} 1 & i \\ 1 & -i \end{pmatrix}$, with determinant $-i - i = -2i \ne 0$. So it is invertible.
4. So $Q_1$ and $Q_2$ are equivalent over $\C$, as [[the classification by rank|0CEX9BRXRZ]] predicts: both have rank $2$.
5. Check at a vector: $(s, t) = (1, 1)$ gives $(x, y) = (1 + i, 1 - i)$, and $xy = 1 - i^2 = 2 = s^2 + t^2$.

## Remarks

Over $\R$ the two forms are not equivalent: $xy$ has signature $(1, 1, 0)$, and $x^2 + y^2$ has signature $(2, 0, 0)$.
The real change $x = s + t$, $y = s - t$ gives only $xy = s^2 - t^2$.
Over $\C$ the factor $i$ turns $-t^2$ into $+t^2$.
Geometrically, the circle $s^2 + t^2 = 1$ and the hyperbola $xy = 1$ are the same complex curve in different coordinates.
The two lines $s = \pm i t$ of the zero set $s^2 + t^2 = 0$ correspond to the axes $x = 0$ and $y = 0$.

## Explanations

### L1 human

Over the real numbers a circle and a hyperbola are different curves.
Over the complex numbers, the change $x = s + it$, $y = s - it$ turns one into the other.
This works because $i^2 = -1$.

### L2 human

The typical use is to see that, over $\C$, only the rank matters.
A trap: the change of variables has complex coefficients, so it is not a change of variables over $\R$.

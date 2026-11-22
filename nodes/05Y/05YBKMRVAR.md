---
tag: 05YBKMRVAR
kind: definition
name: Composition of linear maps
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 00BKRZKMSS
uses: [0RJF668P1T, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.3
---

## Definition

The composition of two linear maps is the map that applies the first one and then the second one.
Let $F$ be a field, let $U$, $V$ and $W$ be vector spaces over $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0RJF668P1T]].
The *composition* of $T$ and $S$ is the [[composite function|0THBK9V825]]
$$T \circ S \colon U \to W, \qquad (T \circ S)(u) = T(S(u)).$$

## Notation

The composite is also written $TS$.
In both notations the map on the right acts first.

## Remarks

The definition asks that the target of $S$ be the source of $T$, because $T$ must be able to take each output $S(u)$ as its input.
For $S \colon \R^2 \to \R^3$ and $T \colon \R^2 \to \R^2$ this fails, and $T \circ S$ is not defined.

The definition does not ask that $T \circ S$ be linear.
That is a theorem, the [[theorem on composites|FSXBBV9C76]], and it uses the linearity of both maps.
Composition is associative, and the identity maps are neutral for it, as for all functions.
It is not commutative: in general $T \circ S \ne S \circ T$, even when both are defined.

For a small example, take $S(x, y) = (y, x)$ and $T(x, y) = (2x, y)$ on $\R^2$.
Then $(T \circ S)(x, y) = T(y, x) = (2y, x)$, while $(S \circ T)(x, y) = S(2x, y) = (y, 2x)$.
At $(1, 0)$ the first gives $(0, 1)$ and the second gives $(0, 2)$.
The [[concept page|00BKRZKMSS]] links composition with matrix multiplication.

## Explanations

### L1 human

To compose two linear maps, apply one and then the other.
The notation $T \circ S$ means "first $S$, then $T$".
Matrix multiplication is this operation, written in coordinates.

### L2 human

Take $S \colon \R^2 \to \R$, $S(x, y) = x + y$, and $T \colon \R \to \R^2$, $T(t) = (t, -t)$.
Both composites exist, but they live on different spaces.
The composite $T \circ S \colon \R^2 \to \R^2$ sends $(x, y)$ to $(x + y, \; -x - y)$, and $S \circ T \colon \R \to \R$ sends $t$ to $t - t = 0$.
Watch out: when both orders are defined, they need not even be maps between the same spaces.

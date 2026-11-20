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

Let $F$ be a field, let $U$, $V$, $W$ be vector spaces over $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0RJF668P1T]].
The *composition* of $T$ and $S$ is the [[composite function|0THBK9V825]]
$$T \circ S \colon U \to W, \qquad (T \circ S)(u) = T(S(u)).$$

## Notation

The composite is also written $TS$.
In both notations, the map on the right acts first.

## Remarks

- The definition needs the target of $S$ to be the source of $T$.
- The composite of two linear maps is again linear; this is a theorem, not part of the definition.
- Composition is associative, and the identity maps are neutral for it.
- Composition is not commutative: in general $T \circ S \ne S \circ T$, even when both are defined.

## Explanations

### L1 human

To compose two linear maps, apply one and then the other.
The notation $T \circ S$ means "first $S$, then $T$".
Matrix multiplication is this operation, written in coordinates.

### L2 human

For $S(x, y) = (y, x)$ and $T(x, y) = (2x, y)$ on $\R^2$, the composite is $(T \circ S)(x, y) = T(y, x) = (2y, x)$.
The other order gives $(S \circ T)(x, y) = S(2x, y) = (y, 2x)$.
The two composites differ at $(1, 0)$: the first gives $(0, 1)$ and the second gives $(0, 2)$.

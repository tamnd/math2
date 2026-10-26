---
tag: 05YBKMRVAR
kind: definition
name: Composition of linear maps
msc: [15A04]
defines: 00BKRZKMSS
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
---

## Definition

Let $F$ be a field, let $U$, $V$, $W$ be vector spaces over $F$, and let $S \colon U \to V$ and $T \colon V \to W$ be [[linear maps|0NRYHJPQG2]].
The *composition* of $T$ and $S$ is the map
$$T \circ S \colon U \to W, \qquad (T \circ S)(u) = T(S(u)).$$

## Remarks

The composition of linear maps is linear.
Composition is associative, and the identity maps are its identity elements.
The [[matrix of a composition is the product of the matrices|05Q1B7MH0M]], in the same order.
Composition is not commutative: in general $T \circ S \ne S \circ T$, even when both are defined.

## Explanations

### L1 human

To compose two linear maps, we apply one and then the other.
We write $T \circ S$ for "first $S$, then $T$".
Matrix multiplication is exactly this operation, written in coordinates.

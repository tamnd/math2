---
tag: DN2MNQGN4S
kind: definition
name: Transformation semigroup
msc: [20M20]
defines: 7ZB7MRKPQ9
uses: [0SJ3RX9TXA, 0XHDTE5YMZ, 0THBK9V825, 0XMEM406JM, 0N6R902FG1, 0515A6D2Y1]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_semigroup
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
Let $T_X$ be the set of all [[maps|0XHDTE5YMZ]] $X \to X$, with the product $fg = f \circ g$ given by [[composition|0THBK9V825]].
A *transformation semigroup* on $X$ is a nonempty subset $S \subseteq T_X$ such that $f \circ g \in S$ for all $f, g \in S$.
It is often written as the pair $(X, S)$.

## Remarks

Composition of maps is associative, so a transformation semigroup is a [[semigroup|0XMEM406JM]].
The whole set $T_X$ is the full transformation [[monoid|0N6R902FG1]]; for $X$ with $n$ elements it has $n^n$ elements.
Its invertible elements form the [[symmetric group|0515A6D2Y1]] on $X$.
Every semigroup $S$ is isomorphic to a transformation semigroup on the set $S^1$, by sending $a$ to the map $x \mapsto ax$.

Example: the constant maps $c_a \colon x \mapsto a$, for $a \in X$.
For all $a, b$, $c_a \circ c_b = c_a$, so they form a transformation semigroup.

Non-example: on $X = \set{1, 2}$, let $s$ swap $1$ and $2$, and let $c_1$ be the constant map to $1$.
The set $\set{\id, s, c_1}$ is not closed under composition, because $s \circ c_1 = c_2$ is not in it.

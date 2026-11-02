---
tag: Y77K0TEKN7
kind: definition
name: Universal coalgebra
msc: [08C05, 18C10, 68Q55]
defines: 2BG03EJT8D
uses: [28NQ0KRHD3, 0BSJ7RQ9BW, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/F-coalgebra
---

## Definition

Let $F$ be a [[functor|28NQ0KRHD3]] from the category of [[sets|0BSJ7RQ9BW]] to itself.
An *$F$-coalgebra* is a pair $(X, \alpha)$ where $X$ is a set and $\alpha \colon X \to F(X)$ is a [[function|0EPAT51DXQ]].
The set $X$ is the carrier, or set of states, and $\alpha$ is the structure map.
A *homomorphism* of $F$-coalgebras from $(X, \alpha)$ to $(Y, \beta)$ is a function $h \colon X \to Y$ such that $\beta \circ h = F(h) \circ \alpha$.
*Universal coalgebra* is the study of $F$-coalgebras and their homomorphisms, for an arbitrary functor $F$ of this kind.

## Remarks

Example: let $A$ be a set and $F(X) = A \times X$, with $F(h)(a, x) = (a, h(x))$.
An $F$-coalgebra is a set $X$ with a map $\alpha(x) = (o(x), n(x))$, an output $o(x) \in A$ and a next state $n(x) \in X$.
The set $A^{\N}$ of streams with $\beta(s) = (s_0, (s_1, s_2, \dots))$ is such a coalgebra.
For every coalgebra $(X, \alpha)$, the map $h(x) = (o(x), o(n(x)), o(n(n(x))), \dots)$ satisfies $\beta \circ h = F(h) \circ \alpha$, and it is the only such map, so the streams form a final $F$-coalgebra.

Non-example of a homomorphism: let $A = \set{a, b}$, let $X = \set{x}$ with $\alpha(x) = (a, x)$, and let $Y = \set{y_1, y_2}$ with $\beta(y_1) = (a, y_2)$ and $\beta(y_2) = (b, y_2)$.
The map $h(x) = y_1$ keeps the output of $x$, but $\beta(h(x)) = (a, y_2)$ while $F(h)(\alpha(x)) = (a, y_1)$, so the square does not commute.

The same definition, with any category in place of sets, gives the [[F-coalgebra|6BS0300CMV]].

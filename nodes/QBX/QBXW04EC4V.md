---
tag: QBXW04EC4V
kind: definition
name: Hilbertian field
msc: ["12E25", "12E30"]
defines: SFPKB3NC0E
uses: [04C5ZBG1WT, 03FKX7Z5DC, 07GNX8GCYP, N1V3YEYHNP]
sources:
  - url: https://en.wikipedia.org/wiki/Thin_set_(Serre)
---

## Definition

Let $K$ be a [[field|04C5ZBG1WT]], and let $K[T, X]$ be the [[polynomial ring|07GNX8GCYP]] in two variables over $K$.
Consider [[irreducible polynomials|03FKX7Z5DC]] $f_1, \dots, f_m \in K[T, X]$, each of positive degree in $X$ and separable in $X$, and a nonzero $g \in K[T]$.
The field $K$ is *Hilbertian* if, for all such data, there is $a \in K$ such that:

1. $g(a) \ne 0$;
2. for each $i$, the polynomial $f_i(a, X) \in K[X]$ is irreducible over $K$ and has the same degree in $X$ as $f_i$.

## Remarks

If $K$ is Hilbertian, then for such data there are infinitely many $a \in K$ with these properties, since one can add to $g$ factors $T - a$ for the values already found.
A Hilbertian field is infinite, and the same condition then holds with $T$ replaced by several variables $T_1, \dots, T_r$.
In characteristic $0$, the separability condition is automatic, and $K$ is Hilbertian exactly when $K$ itself is not a thin subset of the affine line over $K$.

Example: $\Q$ is Hilbertian by [[Hilbert's irreducibility theorem|N1V3YEYHNP]], and so is every number field.
For any field $k$, the rational function field $k(t)$ is Hilbertian.

Non-example: $\R$ is not Hilbertian.
The polynomial $f = X^2 - T^2 - 1$ is irreducible in $\R[T, X]$, because $T^2 + 1$ is not a square in $\R(T)$.
But for every $a \in \R$ one has $a^2 + 1 > 0$, so $f(a, X) = (X - \sqrt{a^2 + 1})(X + \sqrt{a^2 + 1})$ factors over $\R$.
An algebraically closed field is not Hilbertian either, because every polynomial in $X$ of degree at least $2$ factors over it.

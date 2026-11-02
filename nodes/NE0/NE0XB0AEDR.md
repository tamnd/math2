---
tag: NE0XB0AEDR
kind: definition
name: Algebraic cycle
msc: [14C25]
defines: 9VFWPZEVGN
uses: [HV6YBS0YDH, 36X2WTHYCB, SY2MWC434Z, 0YMSEZE1VH, V6JBKT168T]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_cycle
---

## Definition

Let $X$ be an [[algebraic variety|HV6YBS0YDH]] over a field, or more generally a scheme of finite type over a field.
Let $r \ge 0$ be an integer.
An *$r$-cycle* on $X$ is a finite formal sum $Z = \sum_i n_i [V_i]$.
Here the $n_i$ are integers and the $V_i$ are irreducible closed subvarieties of $X$ of [[dimension|36X2WTHYCB]] $r$.
The $r$-cycles form the [[free abelian group|0YMSEZE1VH]] $Z_r(X)$ on the set of such subvarieties.
An *algebraic cycle* is an element of $Z_*(X) = \bigoplus_{r \ge 0} Z_r(X)$.
If $X$ is equidimensional of dimension $n$, one also writes $Z^j(X) = Z_{n-j}(X)$ for the cycles of codimension $j$.

## Remarks

A cycle is *effective* if all $n_i \ge 0$.
Let $W \subset X$ be a closed subscheme whose [[irreducible components|SY2MWC434Z]] $W_1, \ldots, W_s$ all have dimension $r$.
Its *fundamental cycle* is $[W] = \sum_i m_i [W_i]$, where $m_i$ is the [[length|V6JBKT168T]] of the local ring of $W$ at the generic point of $W_i$.
Example: in $X = \mathbb{P}^2$, with $L$ a line and $C$ a conic, $2[L] - [C]$ is a $1$-cycle.
The subscheme defined by $x^2 = 0$ is the double line, with fundamental cycle $2[L]$ for $L = \set{x = 0}$.
Non-example: the union $L_1 \cup L_2$ of two distinct lines is not one of the generators, since it is not irreducible; its fundamental cycle is $[L_1] + [L_2]$.

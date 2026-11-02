---
tag: K4S9G3AQBM
kind: statement
role: theorem
name: Goldstine theorem
msc: [46B10]
uses: [03J5RAKB30, QKR3D65TTH, P6KHVSTPZV, 0BSJSX7ME2]
about: [QKR3D65TTH]
sources:
  - url: https://en.wikipedia.org/wiki/Goldstine_theorem
same_as:
  wikidata: Q3088644
  wikipedia: Goldstine theorem
---

## Statement

Let $X$ be a [[normed vector space|03J5RAKB30]] over $\R$ or $\C$, with closed unit ball $B_X$.
Let $J \colon X \to X^{**}$ be the [[canonical embedding into the bidual|QKR3D65TTH]].
Let $B_{X^{**}}$ be the closed unit ball of $X^{**}$.
Then $J(B_X)$ is [[dense|0BSJSX7ME2]] in $B_{X^{**}}$ for the weak* topology of $X^{**}$, the [[weak topology|P6KHVSTPZV]] defined by the functionals $\xi \mapsto \xi(f)$ for $f \in X^*$.

## Remarks

The weak* closure $C$ of $J(B_X)$ is convex and lies in $B_{X^{**}}$, since $B_{X^{**}}$ is weak*-closed.
If some $\xi \in B_{X^{**}}$ were not in $C$, the [[Hahn–Banach separation theorem|6GWMGFGFJJ]] in $X^{**}$ with the weak* topology would give $f \in X^*$ with $\operatorname{Re} \xi(f) > \sup_{x \in B_X} \operatorname{Re} f(x) = \norm{f}$.
This contradicts $\norm{\xi} \le 1$.

For $X = c_0$, with $X^{**} = \ell^\infty$, the theorem says that every sequence $y$ with $\sup_n \abs{y_n} \le 1$ is a weak* limit of elements of the unit ball of $c_0$.
Indeed the truncations $(y_1, \ldots, y_n, 0, 0, \ldots)$ converge to $y$ against every element of $\ell^1$.

## Explanations

### L1 human

A normed space may be strictly smaller than its double dual.
The theorem says it is still large in a weak sense.
Every element of the unit ball of the double dual can be approximated, in the weak* topology, by elements of the unit ball of the space itself.
So the double dual adds only limit points of a loose kind.

### L2 human

Combined with the [[Banach–Alaoglu theorem|1BXEJXQ2YT]], the theorem shows that a Banach space is [[reflexive|NN8RWPC8WG]] exactly when its closed unit ball is weakly compact.
It is also the key step in the proof of the [[Milman–Pettis theorem|AJ5RG9XQYZ]].
In general the approximation needs nets, not sequences; for separable $X^*$ sequences suffice.

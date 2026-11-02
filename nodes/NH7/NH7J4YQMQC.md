---
tag: NH7J4YQMQC
kind: statement
role: theorem
name: Liouville's theorem on conformal mappings
msc: [53C18, 30C65]
uses: [0YYT36R4YD, YXST7NGMTC]
about: [0YYT36R4YD, GTVQFG2SH9]
sources:
  - url: https://en.wikipedia.org/wiki/Liouville%27s_theorem_(conformal_mappings)
same_as:
  wikidata: Q4454976
  wikipedia: Liouville's theorem (conformal mappings)
---

## Statement

Let $n \ge 3$, let $U \subseteq \R^n$ be a connected open set, and let $f \colon U \to \R^n$ be a smooth [[conformal map|0YYT36R4YD]].
This means that at each $x \in U$ the derivative is $Df(x) = \lambda(x) A(x)$ with $\lambda(x) > 0$ and $A(x)$ an orthogonal matrix.
Then $f$ is the restriction to $U$ of a Möbius transformation of $\R^n \cup \set{\infty}$.
That is, $f$ is a composition of translations, orthogonal linear maps, dilations $x \mapsto c x$ with $c > 0$, and at most one [[inversion|YXST7NGMTC]] $x \mapsto x_0 + r^2 (x - x_0) / \abs{x - x_0}^2$ in a sphere.

## Remarks

Proof idea: the condition $Df^T Df = \lambda^2 I$ is a system of partial differential equations for $f$.
Differentiating it and using $n \ge 3$ forces the function $1/\lambda$ to be either constant or of the form $a \abs{x - x_0}^2$ with $a > 0$.
In the first case $f$ is a similarity; in the second, composing with an inversion centred at $x_0$ reduces to the first case.
The hypothesis $n \ge 3$ is necessary: in $\R^2 = \C$, every holomorphic function with nonzero derivative is conformal, for example $z \mapsto e^z$, and it is not a Möbius transformation since it is not injective.
The smoothness hypothesis can be weakened a great deal.
By results of Gehring and of Reshetnyak, a map of Sobolev class $W^{1,n}_{\mathrm{loc}}$ whose derivative is conformal almost everywhere is constant or a restricted Möbius transformation.

## Explanations

### L1 human

In the plane there are very many maps that keep angles, such as all the maps used by complex analysis.
In space of three or more dimensions, Liouville's theorem says there are very few.
Every angle-preserving map of a region of space is built from moves, rotations, scalings and reflections in spheres.
So in three dimensions there is no freedom to make conformal maps of arbitrary shapes, unlike in the plane.

### L2 human

The theorem explains why conformal geometry in dimension $n \ge 3$ is rigid: the conformal maps form the finite-dimensional group of Möbius transformations, of dimension $(n+1)(n+2)/2$.
In dimension $2$, by contrast, the Riemann mapping theorem gives a conformal map between any two simply connected proper open subsets of the plane.
The result is the local form of the fact that the conformal group of the round sphere $S^n$, $n \ge 3$, is the Möbius group.
It is a starting point for the theory of quasiconformal maps in higher dimensions.

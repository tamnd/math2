---
tag: FSGES670AZ
kind: statement
role: theorem
name: Hartogs's extension theorem
msc: [32D15, 32D20]
uses: [507C34W0ZT, 0R6EWFKRCF, 0SPE8WNWFV, 02BH3MCBQB]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Hartogs%27s_extension_theorem
same_as:
  wikidata: Q383238
  wikipedia: Hartogs's extension theorem
---

## Statement

Let $n \ge 2$, let $D \subseteq \C^n$ be a connected [[open set|02BH3MCBQB]], and let $K \subseteq D$ be a [[compact set|0R6EWFKRCF]] such that $D \setminus K$ is [[connected|0SPE8WNWFV]].
Then every [[holomorphic function|507C34W0ZT]] $f$ on $D \setminus K$ is the restriction of a unique holomorphic function $F$ on $D$.

## Remarks

A short proof uses the [[$\bar\partial$ operator|M1VKCW3RFW]].
Choose a smooth function $\chi$ with compact support in $D$ that equals $1$ near $K$, and let $g = (1 - \chi) f$, extended by $0$ on $K$.
The form $\bar\partial g = -f \, \bar\partial \chi$ is smooth with compact support in $\C^n$, and for $n \ge 2$ the equation $\bar\partial u = \bar\partial g$ has a solution $u$ with compact support.
Then $F = g - u$ is holomorphic on $D$.
The function $u$ vanishes on the unbounded component of the complement of the support of $\bar\partial g$.
So $F = f$ on a nonempty open subset of $D \setminus K$, hence on all of $D \setminus K$ by the identity theorem.

The hypothesis $n \ge 2$ is necessary: $1/z$ is holomorphic on $\C \setminus \set{0}$ and does not extend to $\C$.
Connectedness of $D \setminus K$ is also necessary.
In the unit ball of $\C^n$ let $K$ be the sphere $\abs{z} = 1/2$.
The function equal to $0$ inside $K$ and to $1$ outside is holomorphic on the ball minus $K$, but it has no holomorphic extension.

Example: every holomorphic function on the punctured ball $\set{0 < \abs{z} < 1}$ in $\C^2$ extends holomorphically over the origin.

## Explanations

### L1 human

In several complex variables a holomorphic function cannot have a compact hole of singularities.
If it is defined everywhere except on a compact set, it automatically extends across that set.
This is very different from one variable, where $1/z$ has an isolated singularity at $0$.

### L2 human

The theorem is the first sign that domains in $\C^n$, $n \ge 2$, carry hidden constraints for holomorphic functions.
It implies that the zeros and the singularities of holomorphic functions are never isolated when $n \ge 2$.
It leads to the notions of domain of holomorphy and envelope of holomorphy, which describe how far all holomorphic functions on a domain extend.
The proof sketched above shows the role of the compactly supported solution of $\bar\partial u = v$, which exists only when $n \ge 2$.

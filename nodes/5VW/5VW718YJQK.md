---
tag: 5VW718YJQK
kind: statement
role: theorem
name: Riemann extension theorem in several variables
msc: [32D20]
uses: [507C34W0ZT, 09R8GC85RB, 02BH3MCBQB]
about: [507C34W0ZT, 09R8GC85RB]
sources:
  - url: https://en.wikipedia.org/wiki/Removable_singularity
---

## Statement

Let $D \subseteq \C^n$ be a connected [[open set|02BH3MCBQB]].
Let $A \subseteq D$ be a closed subset with the following property.
Each point $p \in D$ has a connected open neighbourhood $U \subseteq D$ and a [[holomorphic function|507C34W0ZT]] $h \not\equiv 0$ on $U$ with $A \cap U \subseteq \set{z \in U : h(z) = 0}$.

1. Let $f$ be holomorphic on $D \setminus A$, and let each point of $A$ have a neighbourhood $V$ with $f$ bounded on $V \setminus A$. Then $f$ extends uniquely to a holomorphic function on $D$.
2. Let $A$ be moreover a complex analytic subset of $D$ of dimension at most $n - 2$. Then every holomorphic function on $D \setminus A$ extends uniquely to a holomorphic function on $D$.

## Remarks

Under the hypothesis, $D \setminus A$ is dense in $D$ and connected, which gives uniqueness by the identity theorem.
For part 1, take a point of $A$ and choose coordinates and a small polydisc around it.
They can be chosen so that $h$ has no zeros on the part of the boundary where $\abs{z_n}$ equals the radius.
The Cauchy integral in $z_n$ over that circle defines a holomorphic function $F$.
On each line where $z'$ is fixed, $f$ is a bounded holomorphic function of $z_n$ off finitely many points, so by the one-variable [[removable singularity|09R8GC85RB]] theorem $F = f$ there.
Part 2 is proved with Hartogs figures.
Near a point of a set of codimension at least $2$, one finds Hartogs figures in $D \setminus A$ whose filled-in polydiscs cover a neighbourhood of the point.

Example: every holomorphic function on $\C^2 \setminus \set{0}$ extends to $\C^2$, by part 2 with $A = \set{0}$.

The boundedness in part 1 cannot be dropped when $A$ has codimension $1$.
The function $1/z_1$ is holomorphic on $\C^2 \setminus \set{z_1 = 0}$ but unbounded near that line, and it has no holomorphic extension.

## Explanations

### L1 human

A holomorphic function that stays bounded near a thin bad set, such as a complex curve or a point, can be extended across that set.
If the bad set is very thin, of complex codimension at least two, no boundedness is needed at all.
This generalises Riemann's theorem on removable singularities from one variable.

### L2 human

Part 1 is used constantly when holomorphic functions are defined only off an analytic set, for example off the singular points of an analytic variety.
Part 2 is a form of the Hartogs phenomenon: a holomorphic function cannot have a singular set that is an analytic set of codimension two or more.
Part 1 is also the reason why a continuous function on $D$ that is holomorphic off such a set $A$ is holomorphic on all of $D$.

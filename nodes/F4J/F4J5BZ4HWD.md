---
tag: F4J5BZ4HWD
kind: definition
name: Minkowski addition
msc: [52A20, 52A05]
defines: SXS6D87PHE
uses: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_addition
---

## Definition

Let $V$ be a real [[vector space|000AYPA9AJ]] and let $A, B \subseteq V$.
The *Minkowski sum* of $A$ and $B$ is the set
$$A + B = \set{a + b : a \in A, \ b \in B}.$$
For a real number $\lambda$, the *dilate* of $A$ is $\lambda A = \set{\lambda a : a \in A}$.
The operation $(A, B) \mapsto A + B$ is *Minkowski addition*.

## Remarks

Example: in $\R^2$, let $A = [0,1] \times \set{0}$ and $B = \set{0} \times [0, 1]$.
A point $(s, 0) + (0, t)$ with $s, t \in [0, 1]$ is $(s, t)$, so $A + B$ is the unit square $[0,1]^2$.

Minkowski addition is associative and commutative, with neutral element $\set{0}$, and $A + \emptyset = \emptyset$.
If $A$ and $B$ are convex, then $A + B$ is convex; if they are compact, then $A + B$ is compact.

Non-example of a familiar rule: $A + A = 2A$ can fail.
For $A = \set{0, 1} \subseteq \R$ one has $A + A = \set{0, 1, 2}$ but $2A = \set{0, 2}$.
For convex $A$ and $\lambda, \mu \ge 0$ one has $\lambda A + \mu A = (\lambda + \mu) A$.
In terms of [[support functions|1H92CYA4ZC]], $h_{A + B} = h_A + h_B$ for nonempty compact convex $A, B \subseteq \R^n$.
For polytopes, see the [[Minkowski sum of polytopes|7GK5417BJF]].

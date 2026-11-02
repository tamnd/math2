---
tag: 6GWMGFGFJJ
kind: statement
role: theorem
name: Hahn–Banach separation theorem
msc: [46A22, 52A07]
uses: [02AS45T3H9, 4A82S5FVRT, B6GY2KJMWW, 0R6EWFKRCF, 0ZCK8DQYN1]
about: [02AS45T3H9, 4A82S5FVRT]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperplane_separation_theorem
  - url: https://en.wikipedia.org/wiki/Hahn%E2%80%93Banach_theorem
---

## Statement

Let $X$ be a topological vector space over $\R$, and let $A, B \subseteq X$ be nonempty disjoint [[convex sets|02AS45T3H9]].

1. If $A$ is open, then there are a continuous linear functional $f \colon X \to \R$ and a real number $t$ such that $f(a) < t \le f(b)$ for all $a \in A$ and $b \in B$.
2. If $X$ is a [[locally convex space|B6GY2KJMWW]], $A$ is [[compact|0R6EWFKRCF]] and $B$ is [[closed|0ZCK8DQYN1]], then the sets can be strictly separated.
   There are a continuous linear functional $f \colon X \to \R$ and real numbers $s < t$ such that $f(a) < s$ and $f(b) > t$ for all $a \in A$ and $b \in B$.

## Remarks

For part 1, the set $C = A - B + x_0$, with $x_0 \in B - A$ fixed, is an open convex neighbourhood of $0$ that misses $x_0$.
Its [[Minkowski functional|PAX9SHDHDW]] $p$ is sublinear, and the [[Hahn–Banach theorem|QB5AE3VYZZ]] extends the functional $\lambda x_0 \mapsto \lambda$ to a linear $f \le p$; then $f < 1 = f(x_0)$ on $C$, which gives the separation.
Part 2 reduces to part 1: compactness of $A$ gives a convex open neighbourhood $U$ of $0$ with $(A + U) \cap B = \emptyset$.
For a complex space, apply the theorem to the underlying real space and take the real part of a complex functional.
The hypotheses matter: in $\R^2$ the closed convex sets $A = \set{(x, y) : y \le 0}$ and $B = \set{(x, y) : x > 0,\ y \ge 1/x}$ are disjoint, but no line separates them strictly, so part 2 needs compactness of one set.

## Explanations

### L1 human

Two convex sets that do not meet can be put on the two sides of a flat wall.
In the plane the wall is a line and in space it is a plane.
In an infinite-dimensional space it is the set where a continuous linear functional takes one value.
If one set is compact and the other closed, there is even a gap between the sets and the wall.

### L2 human

This is the geometric form of the [[Hahn–Banach theorem|QB5AE3VYZZ]].
It shows that a closed convex set in a locally convex space is the intersection of the closed half-spaces that contain it.
Hence closed convex sets are closed for the [[weak topology|P6KHVSTPZV]], which is the key step in [[Mazur's lemma|7ZR88SCSRF]].
It is also the main tool in the proofs of the [[Krein–Milman theorem|RSRAY0Q68S]], the [[Goldstine theorem|K4S9G3AQBM]] and the [[bipolar theorem|FX5PWKCMBQ]].

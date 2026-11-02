---
tag: VMDTGTMN9P
kind: definition
name: Complex analytic variety
msc: [32B15, 32C25, 32C15]
defines: GB7M582M5Y
uses: [JSGWAN2RJV, 507C34W0ZT, 0ZCK8DQYN1]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]], for example an open subset of $\C^n$.
A subset $A \subseteq X$ is a *complex analytic variety* in $X$, or an analytic subset of $X$, if:

1. $A$ is [[closed|0ZCK8DQYN1]] in $X$, and
2. every point $a \in X$ has an open neighbourhood $U$ and finitely many [[holomorphic functions|507C34W0ZT]] $f_1, \dots, f_k$ on $U$ with
$$A \cap U = \set{z \in U : f_1(z) = \cdots = f_k(z) = 0}.$$

## Remarks

For points $a \notin A$ the second condition holds with $U = X \setminus A$ and $f_1 = 1$, so it only matters at points of $A$.
Example: in $\C^2$, $A = \set{z_1 z_2 = 0}$ is an analytic variety, with $U = \C^2$ and $f_1 = z_1 z_2$; it is the union of the two coordinate axes.
Non-example: the closed unit disc $\set{\abs{z} \le 1}$ in $\C$ is closed but not analytic.
Let $a$ be a point with $\abs{a} = 1$ and let $U$ be a connected neighbourhood of $a$.
A holomorphic function on $U$ that vanishes on the part of the disc in $U$ vanishes on an open set, hence on all of $U$.
So the common zero set would be $U$, not the part of the disc in $U$.
A set that satisfies condition 2 only at its own points is called locally analytic.
It need not be closed, for example the punctured line $\set{z_1 = 0} \setminus \set{0}$ in $\C^2$.
Some authors reserve "variety" for irreducible analytic sets; here no irreducibility is required.
The empty set and $X$ itself are analytic varieties, and finite unions and arbitrary intersections of analytic varieties are analytic varieties.

---
tag: WRZA1VYGB6
kind: definition
name: Gale diagram
msc: [52B35, 52B11]
defines: KFCXGKK288
uses: [0YMB1676R1, 0PHDYNR24D, 0FQSDC2EQ2, 300K6CB1KH]
sources:
  - url: https://en.wikipedia.org/wiki/Gale_diagram
---

## Definition

Let $d \ge 1$ and $n \ge d + 1$, and let $v_1, \dots, v_n$ be points of $\R^d$ whose [[affine span|0YMB1676R1]] is $\R^d$.
Let $A$ be the $(d+1) \times n$ matrix whose $i$-th column is $(v_i, 1) \in \R^{d+1}$.
Its [[null space|0PHDYNR24D]] $N = \set{\lambda \in \R^n : A \lambda = 0}$, the space of affine dependences of the points, has dimension $n - d - 1$.
Choose a basis of $N$ and let $B$ be the $n \times (n - d - 1)$ matrix with these basis vectors as columns.
The *Gale transform* of $v_1, \dots, v_n$ is the sequence $g_1, \dots, g_n \in \R^{n-d-1}$ of rows of $B$.

## Remarks

The Gale transform is determined up to an invertible linear map of $\R^{n-d-1}$, the change of basis of $N$.
Many authors call the configuration $g_1, \dots, g_n$ a *Gale diagram*, and some first rescale each nonzero $g_i$ by a positive factor; this does not affect the property below.

Key property: let $T \subseteq \set{1, \dots, n}$ be nonempty and $S$ its complement.
Consider an affine function $\ell$ on $\R^d$ with $\ell(v_i) = 0$ for $i \in S$ and $\ell(v_i) > 0$ for $i \in T$.
Such an $\ell$ exists if and only if $0$ lies in the relative interior of the [[convex hull|0FQSDC2EQ2]] of $\set{g_i : i \in T}$.
Indeed, the vectors $(\ell(v_1), \dots, \ell(v_n))$ are exactly the vectors $y$ with $\sum_i y_i g_i = 0$.
So when the $v_i$ are the vertices of a [[convex polytope|300K6CB1KH]] $P$, the sets $\set{v_i : i \in S}$ that are vertex sets of faces of $P$ are read off from the $g_i$.

Example: for the $4$ vertices $0, e_1, e_2, e_1 + e_2$ of a square in $\R^2$, $n - d - 1 = 1$, and $N$ is spanned by $(1, -1, -1, 1)$.
So the Gale transform is $1, -1, -1, 1$ in $\R$.
For $T = \set{1, 4}$, the hull of $g_1 = g_4 = 1$ is $\set{1}$, which misses $0$, so $\set{e_1, e_2}$ is not a face: it is a diagonal.
For $T = \set{1, 2}$, the hull of $1$ and $-1$ contains $0$ in its interior, so $\set{e_2, e_1 + e_2}$ is an edge.

Non-example: the points $0, e_1, 2e_1$ in $\R^2$ do not span $\R^2$ affinely, so the construction does not apply.

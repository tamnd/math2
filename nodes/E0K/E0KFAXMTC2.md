---
tag: E0KFAXMTC2
kind: statement
role: theorem
name: Existence and uniqueness of the adjoint
msc: ["15A04", "47A05"]
topics: [3YM9EK6VMB]
audience: ug1
about: [0R9NMSM1ZP]
uses: [01EK923SKP, 0NRYHJPQG2, 0RT96J4D3H, 04GYPXDXNH]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_adjoint
    locator: Definition for bounded operators between Hilbert spaces
  - book: isbn:9783031410253
    locator: Chapter 7
  - book: isbn:9780134860244
    locator: Section 6.3
---

## Statement

Every linear map between finite-dimensional inner product spaces has an adjoint, and only one.
Let $V$ and $W$ be finite-dimensional [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
Then there is exactly one map $S \colon W \to V$ such that
$$\ip{Tv}{w} = \ip{v}{S w} \qquad \text{for all } v \in V \text{ and } w \in W.$$
This map $S$ is linear, and it is the [[adjoint|0R9NMSM1ZP]] $T^*$ of $T$.
If $e_1, \dots, e_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$, then
$$T^* w = \sum_{j=1}^{n} \ip{w}{T e_j}\, e_j \qquad \text{for all } w \in W.$$

## Remarks

### Why each hypothesis is needed

Finite dimension of $V$ is needed.
Let $V$ be the space of all real polynomials with $\ip{p}{q} = \int_0^1 p q \, dx$, let $W = \mathbb{R}$ with $\ip{a}{b} = ab$, and let $T(p) = p(0)$.
An adjoint would give a polynomial $q = S(1)$ with $p(0) = \ip{Tp}{1} = \ip{p}{q}$ for every $p$.
Take $p = xq$: then $p(0) = 0$, so $\int_0^1 x q^2 \, dx = 0$, and this forces $q = 0$.
But then $p = 1$ gives $1 = \ip{1}{0} = 0$, which is false, so $T$ has no adjoint.

The inner product on $V$ must be positive definite.
With the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$ and $T(x) = x_2$ from $\mathbb{R}^2$ to $\mathbb{R}$, an adjoint would need a vector $u$ with $x_2 = \beta(x, u) = x_1 u_1$ for all $x$.
The vector $x = (0, 1)$ gives $1 = 0$, so no adjoint exists.

The map $T$ must be linear.
If some map $S$ satisfies the identity, then for all $w$
$$\ip{T(v + v') - Tv - Tv'}{w} = \ip{v + v'}{Sw} - \ip{v}{Sw} - \ip{v'}{Sw} = 0,$$
so $T(v + v') = Tv + Tv'$, and in the same way $T(cv) = cTv$.
So a map that is not linear has no adjoint.

### What it gives you

The [[definition of the adjoint|0ST8QF9T3T]] makes sense: "the map $T^*$" names one well-defined linear map.
Uniqueness also gives a method of proof.
To show that a linear map $S$ equals $T^*$, it is enough to check $\ip{Tv}{w} = \ip{v}{Sw}$ for all $v$ and $w$.
The [[algebraic properties of the adjoint|TPP76FP659]] are proved in this way.

The basis formula is a way to compute.
It is the Riesz formula for the linear form $v \mapsto \ip{Tv}{w}$, because the coefficient of $e_j$ is the value of that form at $e_j$, conjugated.
It needs an orthonormal basis: in another basis the numbers $\ip{w}{T e_j}$ are not the coordinates of $T^* w$.

### The converse

Is every linear map $S \colon W \to V$ the adjoint of some map $T \colon V \to W$?
Yes: $S$ is the adjoint of $S^*$, by the rule $(S^*)^* = S$ in the [[algebraic properties|TPP76FP659]].
So $T \mapsto T^*$ is a bijection between the linear maps $V \to W$ and the linear maps $W \to V$.

### Generalizations

For a bounded linear map between Hilbert spaces, the [[Riesz theorem for Hilbert spaces|TTC40N49M6]] gives the [[Hilbert space adjoint|6HSJBJ8TTQ]] by the same proof.
For two vector spaces with nondegenerate bilinear forms, the same argument gives a right adjoint and a left adjoint, and the two can differ when the forms are not symmetric.

## Explanations

### L1 human

The theorem says that each linear map has an adjoint, and only one.
For a matrix with the dot product, the adjoint is the transpose.
For example, the map that sends $(x_1, x_2)$ to $(x_2, 0)$ has the adjoint that sends $(y_1, y_2)$ to $(0, y_1)$.
No other map does the same job.

### L2 human

Here is the basis formula at work in $\mathbb{R}^2$ with the dot product.
Let $T(x_1, x_2) = (x_1 + 2x_2, 3x_2)$, with $e_1 = (1, 0)$ and $e_2 = (0, 1)$, so $T e_1 = (1, 0)$ and $T e_2 = (2, 3)$.
For $w = (w_1, w_2)$ the formula gives
$$T^* w = (w \cdot T e_1)\, e_1 + (w \cdot T e_2)\, e_2 = (w_1, 2w_1 + 3w_2).$$
Check with $v = w = (1, 1)$: $Tv = (3, 3)$, so $\ip{Tv}{w} = 6$, and $T^* w = (1, 5)$, so $\ip{v}{T^* w} = 6$.
In practice we often guess a formula for the adjoint and then check the defining identity, and uniqueness makes the check enough.
Watch out: the basis formula needs an orthonormal basis.

### L3 human

The proof identifies each finite-dimensional inner product space with its dual space by the Riesz map, which is antilinear over $\mathbb{C}$.
The adjoint is the dual map $T' \colon W' \to V'$, carried to a map $W \to V$ by the Riesz maps of $W$ and $V$.
In infinite dimension, a densely defined unbounded operator has an adjoint on a domain, and the closed and the self-adjoint operators of functional analysis come from this construction.

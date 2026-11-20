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

Let $V$ and $W$ be finite-dimensional [[inner product spaces|01EK923SKP]] over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$.
Let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
Then there is exactly one map $S \colon W \to V$ such that
$$\ip{Tv}{w} = \ip{v}{S w} \qquad \text{for all } v \in V \text{ and } w \in W.$$
This map $S$ is linear.
It is the [[adjoint|0R9NMSM1ZP]] $T^*$ of $T$.

## Remarks

### Why each hypothesis is needed

- Finite dimension of $V$ is needed. Let $V$ be the space of real polynomials with $\ip{p}{q} = \int_0^1 pq$, and let $W = \mathbb{R}$ with $\ip{a}{b} = ab$. The linear map $T(p) = p(0)$ has no adjoint. An adjoint would give $p(0) = \ip{Tp}{1} = \ip{p}{S(1)}$ for all $p$, and the [[Riesz theorem|04GYPXDXNH]] shows that no polynomial $S(1)$ does this.
- The inner product on $V$ must be positive definite. With the semidefinite form $\beta(x, y) = x_1 y_1$ on $\mathbb{R}^2$ and $T(x) = x_2$ into $\mathbb{R}$, no vector $u$ has $x_2 = \beta(x, u)$ for all $x$. So no adjoint exists.
- The map $T$ must be linear. If some map $S$ has the property, then $\ip{T(v + v') - Tv - Tv'}{w} = 0$ for all $w$, so $T$ is additive. In the same way $T(cv) = cT(v)$, so a map that is not linear has no adjoint.

### Consequences

- The [[definition of the adjoint|0ST8QF9T3T]] is correct: the phrase "the map $T^*$" names one well-defined linear map.
- Uniqueness gives a method of proof. To show that a linear map $S$ equals $T^*$, it is enough to check $\ip{Tv}{w} = \ip{v}{Sw}$ for all $v$ and $w$. The [[algebraic properties of the adjoint|TPP76FP659]] are proved in this way.
- If $e_1, \dots, e_n$ is an [[orthonormal basis|0FWJ0VW561]] of $V$, then $T^* w = \sum_{j=1}^{n} \ip{w}{T e_j} e_j$. This is the formula of the Riesz theorem for the form $v \mapsto \ip{Tv}{w}$.

### Converse

The converse question is whether each linear map $S \colon W \to V$ is the adjoint of some $T$.
This is true: $S$ is the adjoint of $S^*$, by the rule $(S^*)^* = S$ in [[the algebraic properties|TPP76FP659]].

### Generalizations

- For a bounded linear map between Hilbert spaces, the [[Riesz theorem for Hilbert spaces|TTC40N49M6]] gives the [[Hilbert space adjoint|6HSJBJ8TTQ]] by the same proof.
- For two vector spaces with nondegenerate bilinear forms, the same argument gives a right adjoint and a left adjoint, which can differ when the forms are not symmetric.

## Explanations

### L1 human

The theorem says that each linear map has an adjoint, and only one.
For a matrix with the dot product, the adjoint is the transpose.
For example, the map that sends $(x_1, x_2)$ to $(x_2, 0)$ has the adjoint that sends $(y_1, y_2)$ to $(0, y_1)$.
No other map does the same job.

### L2 human

Worked example: the formula $T^* w = \sum_j \ip{w}{T e_j} e_j$ in $\mathbb{R}^2$.

1. Let $T(x_1, x_2) = (x_1 + 2x_2, 3x_2)$ with the dot product, and $e_1 = (1, 0)$, $e_2 = (0, 1)$.
2. Then $T e_1 = (1, 0)$ and $T e_2 = (2, 3)$.
3. For $w = (w_1, w_2)$, the formula gives $T^* w = (w_1) e_1 + (2w_1 + 3w_2) e_2 = (w_1, 2w_1 + 3w_2)$.
4. Check with $v = (1, 1)$ and $w = (1, 1)$: $Tv = (3, 3)$, so $\ip{Tv}{w} = 6$.
5. Also $T^* w = (1, 5)$, so $\ip{v}{T^* w} = 6$. The two numbers agree.

The typical use of uniqueness: guess a formula for the adjoint, then check the defining identity.
A trap: the formula needs an orthonormal basis.
In another basis the coefficients $\ip{w}{T e_j}$ do not give the coordinates of $T^* w$.

### L3 human

The proof identifies each finite-dimensional inner product space with its dual space by the Riesz map, which is antilinear over $\mathbb{C}$.
The adjoint is the dual map $T' \colon W' \to V'$, transported to $W \to V$ by the Riesz isomorphisms of $W$ and $V$.
In infinite dimension, an unbounded densely defined operator has an adjoint defined on a domain, and closedness and self-adjointness of operators come from this construction.

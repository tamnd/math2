---
tag: NRPQP49N9F
kind: statement
role: theorem
name: Dvoretzky's theorem
msc: [46B07, 52A21, 46B09]
uses: [03J5RAKB30, 00YC1D652K, 0MFJJV97RJ, BF9XR5SVPV, RH1WTN38RQ]
about: [03J5RAKB30]
sources:
  - url: https://en.wikipedia.org/wiki/Dvoretzky%27s_theorem
same_as:
  wikidata: Q5317821
  wikipedia: Dvoretzky's theorem
---

## Statement

Let $k \ge 1$ be an integer and let $\varepsilon > 0$.
Then there is an integer $N = N(k, \varepsilon)$ with the following property.
Let $X$ be a real [[normed space|03J5RAKB30]] of dimension at least $N$.
Then $X$ has a $k$-dimensional [[linear subspace|00YC1D652K]] $E$ with a linear map $T \colon \R^k \to E$ such that
$$\abs{x} \le \norm{T x} \le (1 + \varepsilon) \abs{x} \quad \text{for all } x \in \R^k,$$
where $\abs{x}$ is the Euclidean norm of $x$.

## Remarks

The theorem was proved by Dvoretzky.
V. Milman gave a proof based on concentration of measure on the high-dimensional sphere.
His proof shows that one can take $k$ of order $c(\varepsilon) \log n$ in a space of dimension $n$.
The idea: a norm, seen as a Lipschitz function on the Euclidean sphere, is almost constant on most of the sphere.
A random $k$-dimensional subspace then sees only this almost constant part.

The bound $\log n$ cannot be improved in general.
For $\ell_\infty^n$, that is $\R^n$ with the max norm, the largest $k$ with a subspace at distance at most $2$ from Euclidean is of order $\log n$.
For $\ell_1^n$, in contrast, there are almost Euclidean subspaces of dimension proportional to $n$.

## Explanations

### L1 human

Every convex body that is symmetric about the origin and lives in very many dimensions has a slice through the center that is almost a round ball.
The slice can be large if the dimension is large.
So round balls, that is Euclidean geometry, appear inside every normed space of high dimension.

### L2 human

In the language of the local theory of Banach spaces, the theorem says that $\ell_2$ is finitely representable in every infinite-dimensional Banach space.
It is a starting point of asymptotic geometric analysis, together with the notions of [[type and cotype|BF9XR5SVPV]].
The distance used here is the Banach–Mazur distance of the [[Banach–Mazur compactum|RH1WTN38RQ]].

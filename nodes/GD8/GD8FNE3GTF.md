---
tag: GD8FNE3GTF
kind: definition
name: Real analytic manifold
msc: [32C05, 58A07]
defines: Z7H98E1NHP
uses: [QQQ9B1DK4P, J7P32JQTVE, 081WKEDK6C, F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_manifold
---

## Definition

Let $M$ be a [[topological manifold|QQQ9B1DK4P]] of dimension $n$.
A *real analytic atlas* on $M$ is an [[atlas|J7P32JQTVE]] $\set{(U_i, \varphi_i)}$ of charts $\varphi_i \colon U_i \to \R^n$ with the following property.
For all $i, j$ the transition map
$$\varphi_j \circ \varphi_i^{-1} \colon \varphi_i(U_i \cap U_j) \to \varphi_j(U_i \cap U_j)$$
is real [[analytic|081WKEDK6C]].
That is, each component of the transition map is given near each point by a convergent power series.
A *real analytic manifold* is a topological manifold $M$ together with a maximal real analytic atlas on $M$.

## Remarks

Example: the sphere $S^n \subseteq \R^{n+1}$ with the two stereographic projections is a real analytic manifold.
The transition map is $y \mapsto y / \abs{y}^2$ on $\R^n \setminus \set{0}$, whose components are quotients of polynomials by a nonvanishing polynomial, hence real analytic.

Non-example: on $\R$ take the identity chart and the chart $\psi$ with $\psi(x) = x$ for $x \le 0$ and $\psi(x) = x + e^{-1/x^2}$ for $x > 0$.
The map $\psi$ is a homeomorphism of $\R$ with positive derivative, and the transition map $\psi$ is smooth, so this atlas makes $\R$ a [[smooth manifold|F45VQ47GPV]].
But $\psi$ is not real analytic at $0$: all its derivatives at $0$ agree with those of $x \mapsto x$, while $\psi(x) \neq x$ for $x > 0$.
So the atlas is not real analytic.

A real analytic manifold is in particular a smooth manifold, since its maximal real analytic atlas lies in a unique maximal smooth atlas.

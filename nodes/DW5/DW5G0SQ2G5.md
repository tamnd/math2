---
tag: DW5G0SQ2G5
kind: definition
name: Dirichlet form
msc: [31C25, 60J46]
defines: MH20Q2N1AH
uses: [7V9TSDJFZR, HM2HHE3J51, SASP14MA1Z, 0SQZMXB6GP, M4CEZ5K9HP, 0NEGN5CRSC]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet_form
---

## Definition

Let $(X, \mathcal{A}, m)$ be a $\sigma$-finite [[measure|7V9TSDJFZR]] space.
Let $H = L^2(X, m)$ be the real [[Hilbert space|HM2HHE3J51]] of square-integrable functions (an [[Lp space|SASP14MA1Z]]), with inner product $(\cdot, \cdot)$.
Let $\mathcal{F}$ be a dense linear subspace of $H$ and let $\mathcal{E} \colon \mathcal{F} \times \mathcal{F} \to \R$ be a [[bilinear form|0SQZMXB6GP]].
The pair $(\mathcal{E}, \mathcal{F})$ is a *Dirichlet form* on $L^2(X, m)$ if:

1. $\mathcal{E}$ is symmetric: $\mathcal{E}(u, v) = \mathcal{E}(v, u)$ for all $u, v \in \mathcal{F}$.
2. $\mathcal{E}$ is nonnegative: $\mathcal{E}(u, u) \ge 0$ for all $u \in \mathcal{F}$.
3. $\mathcal{E}$ is closed: $\mathcal{F}$ is complete for the norm $\norm{u}_1 = \left(\mathcal{E}(u, u) + (u, u)\right)^{1/2}$.
4. $\mathcal{E}$ is Markovian: for every $u \in \mathcal{F}$, the function $v = \min(\max(u, 0), 1)$ lies in $\mathcal{F}$ and $\mathcal{E}(v, v) \le \mathcal{E}(u, u)$.

## Remarks

Example: on $L^2(\R^n)$ with Lebesgue measure, take $\mathcal{F}$ to be the [[Sobolev space|M4CEZ5K9HP]] $W^{1,2}(\R^n)$ and $\mathcal{E}(u, v) = \int_{\R^n} \nabla u \cdot \nabla v \, dx$.
It is symmetric and nonnegative, and $\norm{\cdot}_1$ is the Sobolev norm, which is complete.
The truncation $v = \min(\max(u, 0), 1)$ of $u \in W^{1,2}$ lies in $W^{1,2}$, with $\nabla v = \nabla u$ almost everywhere on $\set{0 < u < 1}$ and $\nabla v = 0$ almost everywhere elsewhere, so $\mathcal{E}(v, v) \le \mathcal{E}(u, u)$.

Non-example: on $L^2(\R)$ take $\mathcal{F} = W^{2,2}(\R)$ and $\mathcal{E}(u, v) = \int u'' v'' \, dx$.
Clauses 1 to 3 hold, but clause 4 fails.
If $u \in W^{2,2}(\R)$ is smooth and crosses the level $1$ with nonzero slope, its truncation has a corner there, so it is not in $W^{2,2}(\R)$.

A closed, symmetric, nonnegative, densely defined form corresponds to a nonnegative [[self-adjoint operator|0NEGN5CRSC]] $A$ with $\mathcal{E}(u, v) = (A^{1/2} u, A^{1/2} v)$ and $\mathcal{F}$ the domain of $A^{1/2}$.
Clause 4 holds if and only if the semigroup $T_t = e^{-tA}$ is Markovian: $0 \le f \le 1$ almost everywhere implies $0 \le T_t f \le 1$ almost everywhere, for every $t > 0$.
Let $X$ be a locally compact separable metric space and $m$ a Radon measure of full support.
The form is then *regular* if $\mathcal{F} \cap C_c(X)$ is dense in $\mathcal{F}$ for $\norm{\cdot}_1$ and dense in $C_c(X)$ for the uniform norm.

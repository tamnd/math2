---
tag: BAGCJR5EQF
kind: definition
name: Rayleigh–Ritz method
msc: [49R05, 65N25, 65F15]
defines: 5YSP8TWD4Q
uses: [HM2HHE3J51, 0NEGN5CRSC, 06WHP8SE98, 0BQAA2BK3Q, G11NE3AT6E]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Ritz_method
---

## Definition

Let $H$ be a real or complex [[Hilbert space|HM2HHE3J51]] with inner product $\ip{\cdot}{\cdot}$.
Let $A$ be a [[self-adjoint operator|0NEGN5CRSC]] in $H$ that is bounded below.
Let $Q$ be its closed quadratic form with form domain $D(Q)$, so that $Q(u, v) = \ip{Au}{v}$ for $u$ in the domain of $A$.
Let $m \ge 1$ and let $\varphi_1, \dots, \varphi_m \in D(Q)$ be linearly independent trial vectors.
Let $K$ and $M$ be the $m \times m$ matrices with entries $K_{ij} = Q(\varphi_j, \varphi_i)$ and $M_{ij} = \ip{\varphi_j}{\varphi_i}$.
The *Rayleigh–Ritz method* computes the solutions of the generalised eigenvalue problem
$$K c = \mu M c, \qquad c \in \C^m \setminus \set{0}.$$
Its eigenvalues $\mu_1 \le \cdots \le \mu_m$ are the *Ritz values*, and the vectors $\sum_j c_j \varphi_j$ for the eigenvectors $c$ are the *Ritz vectors*.

## Remarks

The Ritz values are the stationary values of the [[Rayleigh quotient|06WHP8SE98]] $Q(u, u) / \ip{u}{u}$ on the span $V$ of the trial vectors.
If the spectrum of $A$ below the essential spectrum consists of [[eigenvalues|0BQAA2BK3Q]] $\lambda_1 \le \lambda_2 \le \cdots$, the [[min-max theorem|G11NE3AT6E]] gives $\lambda_k \le \mu_k$ for $k = 1, \dots, m$.
For a Hermitian $n \times n$ matrix $A$ and a matrix $W$ with $m$ orthonormal columns, the Ritz values are the eigenvalues of $W^* A W$.

Example: $H = L^2(0, 1)$ and $A = -\frac{d^2}{dx^2}$ with Dirichlet conditions, so $D(Q) = H^1_0(0, 1)$, $Q(u, u) = \int_0^1 \abs{u'}^2 \, dx$ and $\lambda_1 = \pi^2$.
With $m = 1$ and $\varphi_1(x) = x (1 - x)$, which vanishes at $0$ and $1$, one gets $K = \int_0^1 (1 - 2x)^2 \, dx = \frac{1}{3}$ and $M = \int_0^1 x^2 (1 - x)^2 \, dx = \frac{1}{30}$.
So $\mu_1 = 10$, an upper bound for $\pi^2 \approx 9.8696$.

Non-example: the trial function $\varphi_1 = 1$ is not in $H^1_0(0, 1)$, because it does not vanish at the ends.
Its Rayleigh quotient is $0 < \pi^2$, so the upper bound fails when the trial vectors leave the form domain.

## Explanations

### L1 human

The method restricts the eigenvalue problem to a few trial vectors and solves the resulting small matrix problem, which gives upper bounds for the lowest eigenvalues.

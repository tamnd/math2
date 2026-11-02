---
tag: 97VNBS15CD
kind: statement
role: theorem
name: Schwarz alternating method
msc: [65N55, 65F10]
uses: [HM2HHE3J51, 0B8KZRT28M, M4CEZ5K9HP, 2RPE77ACER]
about: [AN054RHT1K]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarz_alternating_method
same_as:
  wikidata: Q7433186
  wikipedia: Schwarz alternating method
---

## Statement

Let $V$ be a real [[Hilbert space|HM2HHE3J51]] with inner product $a(\cdot, \cdot)$ and norm $\norm{v}_a = a(v, v)^{1/2}$.
Let $\ell$ be a bounded linear functional on $V$, and let $u \in V$ be the solution of $a(u, v) = \ell(v)$ for all $v \in V$.
Let $V_1, V_2$ be closed subspaces of $V$ with $V_1 + V_2 = V$.
The *alternating Schwarz method* starts from $u^0 \in V$ and repeats two half steps.

1. Find $w_1 \in V_1$ with $a(w_1, v) = \ell(v) - a(u^n, v)$ for all $v \in V_1$, and set $u^{n+1/2} = u^n + w_1$.
2. Find $w_2 \in V_2$ with $a(w_2, v) = \ell(v) - a(u^{n+1/2}, v)$ for all $v \in V_2$, and set $u^{n+1} = u^{n+1/2} + w_2$.

Then there is a constant $\rho < 1$, depending only on $V_1$ and $V_2$, such that
$$\norm{u^n - u}_a \le \rho^n \norm{u^0 - u}_a \quad \text{for all } n \ge 0.$$

## Remarks

Let $P_i$ be the $a$-[[orthogonal projection|0B8KZRT28M]] onto $V_i$.
The errors satisfy $u^{n+1} - u = (I - P_2)(I - P_1)(u^n - u)$, a product of the projections onto $V_1^\perp$ and $V_2^\perp$.
Since $V_1 + V_2 = V$ is closed, $V_1^\perp \cap V_2^\perp = \set{0}$ and the angle between $V_1^\perp$ and $V_2^\perp$ is positive, which gives $\rho = \norm{(I - P_2)(I - P_1)}_a < 1$.
If $V_1 + V_2$ is only dense in $V$, von Neumann's theorem on alternating projections still gives $u^n \to u$, but possibly without a geometric rate.

The original setting is the Dirichlet problem $-\Delta u = f$ in $\Omega$, $u = 0$ on $\partial \Omega$, where $\Omega = \Omega_1 \cup \Omega_2$ is a union of two overlapping domains.
Take $V = H^1_0(\Omega)$ (a [[Sobolev space|M4CEZ5K9HP]]), $a(u, v) = \int_\Omega \nabla u \cdot \nabla v \, dx$, and $V_i = H^1_0(\Omega_i)$ extended by zero.
Then each half step solves the Dirichlet problem on $\Omega_i$ with boundary values taken from the current iterate on $\partial \Omega_i \cap \Omega$.
A partition of unity subordinate to the overlap shows $V_1 + V_2 = V$ when the overlap has positive width.
The rate $\rho$ tends to $1$ as the overlap shrinks.

## Explanations

### L1 human

Hermann Schwarz wanted to solve a boundary value problem on a region made of two overlapping simple pieces, such as a disc and a rectangle.
He solved on the disc, used that answer as boundary data on the part of the rectangle's edge inside the disc, solved on the rectangle, and went back and forth.
The theorem says this back-and-forth converges to the solution on the whole region, and the error shrinks by a fixed factor each round.

### L2 human

The method is the prototype of [[domain decomposition methods|AN054RHT1K]]: a large problem is split into problems on subdomains that are cheaper to solve.
In the abstract form it is a block Gauss–Seidel iteration on the splitting $V = V_1 + V_2$, and the error operator is a product of orthogonal projections.
The [[additive Schwarz method|X68MFYW014]] is the Jacobi-type variant, which solves on all pieces at once and is used as a preconditioner.
The convergence rate depends on the overlap, which is why practical methods add a coarse space.

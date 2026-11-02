---
tag: 1VVKF0Y19B
kind: statement
role: theorem
name: Holmgren's uniqueness theorem
msc: [35A02, 35A20]
uses: [6DZETZ5T9G, CQJ2E2ARRF, 081WKEDK6C]
about: [6DZETZ5T9G]
sources:
  - url: https://en.wikipedia.org/wiki/Holmgren%27s_uniqueness_theorem
same_as:
  wikidata: Q5883744
  wikipedia: Holmgren's uniqueness theorem
---

## Statement

Let $\Omega \subseteq \R^n$ be open, and let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) \, \partial^\alpha$ be a [[linear differential operator|6DZETZ5T9G]] of order $m$ whose coefficients $a_\alpha$ are [[real-analytic|081WKEDK6C]] on $\Omega$.
Let $S \subseteq \Omega$ be a real-analytic hypersurface and let $x_0 \in S$ be a point at which $S$ is [[noncharacteristic|CQJ2E2ARRF]] for $P$.
Let $U \subseteq \Omega$ be an open neighbourhood of $x_0$, and let $u \in C^m(U)$ satisfy $P u = 0$ in $U$ and $\partial^\alpha u = 0$ on $S \cap U$ for all $\abs{\alpha} \le m - 1$.
Then $u = 0$ in some neighbourhood of $x_0$.

## Remarks

Equivalently, two $C^m$ solutions of $P u = f$ with the same Cauchy data on $S$ coincide near $x_0$; here $f$ need not be analytic.
The proof is by duality: one solves the adjoint equation $P^{*} v = p$ for polynomials $p$, with zero Cauchy data on a nearby analytic hypersurface, using the [[Cauchy–Kovalevskaya theorem|97HMV9BT2W]].
Integration by parts then shows that $\int u \, p = 0$ on a lens-shaped region for every polynomial $p$, and the Weierstrass approximation theorem gives $u = 0$ there.
Example: for the wave equation $\partial_t^2 u - \partial_x^2 u = 0$, the line $t = 0$ is noncharacteristic, so a $C^2$ solution with $u(0, x) = \partial_t u(0, x) = 0$ vanishes near the line.
The analyticity of the coefficients cannot simply be dropped: there are linear operators with smooth coefficients for which the Cauchy problem has nonzero solutions with zero data.
Hörmander extended the theorem to distribution solutions and to $C^1$ hypersurfaces.

## Explanations

### L1 human

The Cauchy–Kovalevskaya theorem gives uniqueness only among analytic solutions.
Holmgren's theorem says that for linear equations with analytic coefficients there is no other, non-analytic, solution with the same starting data.
So the starting data on a good surface determine the solution near the surface.

### L2 human

The theorem is a unique continuation result across noncharacteristic hypersurfaces.
It applies to the Laplace, heat and wave equations, since their coefficients are constant.
For the wave equation it is a step towards domain of dependence arguments.
For the Laplace equation it shows that the Cauchy problem has at most one solution, even though it is not [[well posed|W09B9NZ9B5]].
The noncharacteristic hypothesis matters: for the heat operator the line $t = 0$ is characteristic, and [[Tychonoff's example|RN4J24CD83]] gives a nonzero solution of the heat equation with zero initial values.

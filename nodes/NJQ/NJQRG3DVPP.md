---
tag: NJQRG3DVPP
kind: statement
role: theorem
name: Tonelli's existence theorem
msc: [49J10, 49J45]
uses: [JRQZ803Q5Y, M4CEZ5K9HP, X0Q69ZS09T, NGT5YCVAMR, H6GTJRG26G, TE379HBTY0]
about: [TE379HBTY0]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_method_in_the_calculus_of_variations
---

## Statement

Let $\Omega \subseteq \R^n$ be a bounded open set with Lipschitz boundary, and let $1 < p < \infty$.
Let $L \colon \overline{\Omega} \times \R \times \R^n \to \R$, written $L(x, u, \xi)$, be continuous.
Assume:

1. $L$ is a [[convex integrand|X0Q69ZS09T]]: $\xi \mapsto L(x, u, \xi)$ is convex for all $(x, u)$;
2. there are constants $a > 0$ and $b \in \R$ with $L(x, u, \xi) \ge a \abs{\xi}^p + b$ for all $(x, u, \xi)$.

Let $u_0$ be in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(\Omega)$ and let $J(u) = \int_\Omega L(x, u, \nabla u) \, dx$, an [[integral functional|JRQZ803Q5Y]].
If $J(u_0) < +\infty$, then $J$ attains its minimum on $u_0 + W^{1,p}_0(\Omega)$.

## Remarks

The proof is the [[direct method|TE379HBTY0]].
The growth bound and the Poincaré inequality make $J$ [[coercive|NGT5YCVAMR]] on $u_0 + W^{1,p}_0(\Omega)$, so a minimising sequence is bounded in $W^{1,p}(\Omega)$.
Since $1 < p < \infty$, a subsequence converges weakly in $W^{1,p}(\Omega)$, and strongly in $L^p(\Omega)$ by the Rellich–Kondrachov theorem.
Convexity in $\xi$ makes $J$ [[weakly lower semicontinuous|H6GTJRG26G]], so the weak limit is a minimiser.

Example: for $L = \frac{1}{2} \abs{\xi}^2 + \frac{1}{4} u^4$ and $p = 2$, the theorem gives a minimiser with boundary values $u_0$ whenever $J(u_0) < +\infty$; it is a weak solution of $-\Delta u + u^3 = 0$.

Each hypothesis matters.
For $L = (\xi^2 - 1)^2 + u^2$ with $n = 1$ and $u_0 = 0$, convexity fails and there is no minimiser.
For $L = \sqrt{1 + \abs{\xi}^2}$, which has growth $p = 1$, minimisers of the area of a graph need not exist in $W^{1,1}$ for some boundary data.

## Explanations

### L1 human

The theorem says that an energy that is convex in the slope and grows fast enough has a lowest state with given boundary values.
Fast growth keeps minimising sequences from running away.
Convexity prevents them from lowering the energy by oscillating.
Together they force a minimising sequence to settle on a true minimiser.

### L2 human

This is the model existence theorem of the calculus of variations, and it is the template for the direct method.
The minimiser is a priori only a Sobolev function; whether it is smooth is the separate question of regularity, raised in Hilbert's nineteenth problem.
For vector-valued $u$, convexity can be weakened to Morrey quasiconvexity, and in nonlinear elasticity to polyconvexity, as in Ball's existence theorem.
Without convexity one replaces the integrand by its convex envelope; this is relaxation, and it computes the limits of minimising sequences.

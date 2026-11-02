---
tag: 3ZZSXKM16Z
kind: statement
role: theorem
name: Kolmogorov–Arnold–Moser theorem
msc: [37J40, 70H08]
uses: [0EDKGA2FAK, 03NM7DZXXC, N0N7CMRCMH, M3T81YNSKC]
about: [N0N7CMRCMH]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov–Arnold–Moser_theorem
same_as:
  wikidata: Q587081
  wikipedia: Kolmogorov–Arnold–Moser theorem
---

## Statement

Let $n \ge 2$, let $D \subseteq \R^n$ be a bounded open set and let $\mathbb{T}^n = \R^n / 2\pi \Z^n$.
Use [[action-angle coordinates|M3T81YNSKC]] $(I, \theta)$ on $D \times \mathbb{T}^n$, with symplectic form $\sum_k dI_k \wedge d\theta_k$.
Consider the [[Hamiltonian system|0EDKGA2FAK]] with Hamiltonian
$$H_\varepsilon(I, \theta) = H_0(I) + \varepsilon H_1(I, \theta),$$
where $H_0$ and $H_1$ are real-analytic on a neighbourhood of $\overline{D} \times \mathbb{T}^n$.
Assume that $H_0$ is nondegenerate: $\det \left( \partial^2 H_0 / \partial I^2 \right) \ne 0$ on $\overline{D}$.
Then there is $\varepsilon_0 > 0$ such that for $0 \le \varepsilon < \varepsilon_0$:

1. the phase space contains a family of invariant $n$-[[tori|03NM7DZXXC]] of $H_\varepsilon$. Each is close to an invariant torus $\set{I = I_0}$ of $H_0$ with Diophantine frequency vector $\omega = \nabla H_0(I_0)$. This means that $\abs{\langle k, \omega \rangle} \ge \gamma \abs{k}^{-\tau}$ for all $k \in \Z^n \setminus \set{0}$, for some constants $\gamma > 0$ and $\tau > n - 1$;
2. on each of these tori the flow of $H_\varepsilon$ is conjugate to the linear flow $\theta \mapsto \theta + t \omega$;
3. the Lebesgue measure of the complement of the union of these tori in $D \times \mathbb{T}^n$ tends to $0$ as $\varepsilon \to 0$.

## Remarks

The proof is a Newton-type iteration.
At each step a canonical change of coordinates removes the angle dependence of the perturbation to a higher order.
Each step needs to divide by $\langle k, \omega \rangle$, the small divisors, and the Diophantine condition controls them.
The quadratic convergence of the Newton scheme beats the loss caused by the small divisors.

Kolmogorov announced the result in 1954, Arnold proved it for analytic Hamiltonians, and Moser proved a version for twist maps of finite smoothness.

Tori with resonant frequencies, where $\langle k, \omega \rangle = 0$ for some $k \ne 0$, are in general destroyed by the perturbation.
Some nondegeneracy condition on $H_0$ is needed, because the proof uses the map $I \mapsto \nabla H_0(I)$ to choose tori with Diophantine frequencies; other versions use the isoenergetic nondegeneracy condition instead.

## Explanations

### L1 human

An [[integrable system|N0N7CMRCMH]] has all its motions wound around invariant tori.
The theorem says that a small push does not destroy this order completely.
Most of the tori survive, slightly deformed, and the motions on them stay quasi-periodic forever.
Only the tori whose frequencies are close to rational relations break up.
This explains why, for example, a planetary system that is close to an integrable one can be stable for most initial conditions.

### L2 human

KAM theory answers a question of Poincaré on the persistence of quasi-periodic motion in nearly integrable systems.
Its key ingredients are the Diophantine condition on frequencies and a rapidly converging iteration.
For two degrees of freedom the surviving $2$-tori separate each $3$-dimensional energy level, which gives stability of the actions for all time.
In three or more degrees of freedom the tori do not separate the energy levels, and [[Arnold diffusion|ZVY046R4XB]] becomes possible; the [[Nekhoroshev estimates|PYEN6SFS9P]] bound its speed.
The same ideas apply to area-preserving twist maps such as the [[standard map|8TEV7CSX2H]].

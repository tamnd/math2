---
tag: PEDD2CP5PF
kind: statement
role: theorem
name: Noether's second theorem
msc: [70H33, 49S05, "58E30"]
uses: [JRQZ803Q5Y, PS0VV149ET, XHPDM5T2JG]
about: [PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/Noether%27s_second_theorem
same_as:
  wikidata: Q10369454
  wikipedia: Noether's second theorem
---

## Statement

Let $\Omega \subseteq \R^n$ be open, and consider maps $u \colon \Omega \to \R^m$.
Let $J(u) = \int_\Omega L(x, u, \partial u, \dots, \partial^k u) \, dx$ be an [[integral functional|JRQZ803Q5Y]] with smooth Lagrangian $L$.
Let $E_1(u), \dots, E_m(u)$ be its [[Euler–Lagrange expressions|PS0VV149ET]], so that the Euler–Lagrange equations read $E(u) = 0$.
Assume that $J$ has a symmetry depending on $r$ arbitrary smooth functions $g_1, \dots, g_r$ of $x$.
Its infinitesimal variations are
$$\delta u_\alpha = \sum_{j=1}^{r} \mathcal{D}_{\alpha j} \, g_j, \quad \alpha = 1, \dots, m,$$
where each $\mathcal{D}_{\alpha j}$ is a linear differential operator whose coefficients depend on $x$, $u$ and derivatives of $u$.
Assume that each such variation leaves $L$ invariant up to a total divergence.
Then the Euler–Lagrange expressions satisfy $r$ identities
$$\sum_{\alpha=1}^{m} \mathcal{D}_{\alpha j}^{*} \, E_\alpha(u) = 0, \quad j = 1, \dots, r,$$
for every smooth $u$, where $\mathcal{D}_{\alpha j}^{*}$ is the formal adjoint of $\mathcal{D}_{\alpha j}$.

## Remarks

Invariance up to a divergence gives $\sum_\alpha E_\alpha(u) \, \delta u_\alpha = \operatorname{div} S$ for some expression $S$ that is linear in the $g_j$ and their derivatives.
Integrating by parts moves the derivatives from $g_j$ onto $E_\alpha$, so $\sum_j g_j \sum_\alpha \mathcal{D}^*_{\alpha j} E_\alpha$ is a divergence too.
An expression of the form $\sum_j g_j F_j$ that is a divergence for all compactly supported $g_j$ must have $F_j = 0$.

Example: the length $J(x, y) = \int_a^b \sqrt{\dot x^2 + \dot y^2} \, dt$ of a regular plane curve, one with $(\dot x, \dot y) \ne 0$ everywhere, is invariant under reparametrisations $t \mapsto t + \varepsilon g(t)$.
The variations are $\delta x = \dot x \, g$ and $\delta y = \dot y \, g$, up to sign, so here $\mathcal{D}$ is multiplication by $\dot x$ and $\dot y$.
The Euler–Lagrange expressions are $E_x = -\frac{d}{dt} T_1$ and $E_y = -\frac{d}{dt} T_2$, with $T = (\dot x, \dot y) / \abs{(\dot x, \dot y)}$.
The identity is $\dot x \, E_x + \dot y \, E_y = 0$ for every regular curve; it holds because $T \cdot \dot T = 0$.

Unlike the first [[Noether's theorem|XHPDM5T2JG]], the result gives identities that hold for all $u$, not conservation laws along solutions.
So the Euler–Lagrange equations are not independent, and their solutions are not determined by initial data alone.

## Explanations

### L1 human

Some symmetries are not a single motion but a whole family that can vary from point to point, like a change of time scale that may differ at each moment.
Noether's second theorem says that such a large symmetry forces relations among the equations of motion themselves.
These relations hold for every function, not only for solutions.
They show that the equations do not fix the solution uniquely, because the symmetry can still move it.

### L2 human

This is the theorem behind gauge theories and general relativity.
In electromagnetism, gauge invariance gives the identity that the divergence of the Maxwell equations vanishes identically, which is linked to charge conservation.
In general relativity, invariance under diffeomorphisms gives the contracted Bianchi identities.
The identities explain why such equations are underdetermined and need gauge fixing before one can solve an initial value problem.

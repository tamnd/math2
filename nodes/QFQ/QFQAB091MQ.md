---
tag: QFQAB091MQ
kind: problem
name: Signorini problem
msc: [74M15, 49J40, 35J86]
uses: [6QS7X5GVMY, H80M01T0H8, M4CEZ5K9HP, GQ3K59MRJP]
about: [6QS7X5GVMY]
sources:
  - url: https://en.wikipedia.org/wiki/Signorini_problem
    locator: Formal statement of the problem
same_as:
  wikidata: Q7513012
  wikipedia: Signorini problem
history:
  posed_by: "Antonio Signorini"
  first_stated: "1959"
---

## Problem

Let $\Omega \subseteq \R^3$ be a bounded open set with Lipschitz boundary, the reference shape of a linearly elastic body.
Split the boundary into disjoint parts $\Gamma_D$, $\Gamma_N$ and $\Gamma_C$, with $\Gamma_D$ of positive surface measure, and let $n$ be the outward unit normal.
For a displacement $u \colon \Omega \to \R^3$ let $\varepsilon(u) = \tfrac12 (\nabla u + \nabla u^T)$ be the strain and $\sigma(u) = \mathcal{C} \varepsilon(u)$ the stress.
Here $\mathcal{C}$ is a bounded elasticity tensor with the usual symmetries that is uniformly positive definite on symmetric matrices.
Let $f$ be a body force and $g$ a surface force on $\Gamma_N$.
Write $u_n = u \cdot n$, $\sigma_n = (\sigma(u) n) \cdot n$ and $\sigma_T = \sigma(u) n - \sigma_n n$.
Find $u$ such that:

1. $-\operatorname{div} \sigma(u) = f$ in $\Omega$;
2. $u = 0$ on $\Gamma_D$;
3. $\sigma(u) n = g$ on $\Gamma_N$;
4. on $\Gamma_C$: $u_n \le 0$, $\sigma_n \le 0$, $\sigma_n u_n = 0$ and $\sigma_T = 0$.

Clause 4 describes frictionless contact with a rigid support.
The body cannot enter the support, the support can only push, and it pushes only where there is contact.

## Remarks

The difficulty is that it is not known in advance where on $\Gamma_C$ the body touches the support, so the boundary condition there is ambiguous.
The weak form is a [[variational inequality|6QS7X5GVMY]].
Let $V = \set{v \in H^1(\Omega; \R^3) : v = 0 \text{ on } \Gamma_D}$, using the [[Sobolev space|M4CEZ5K9HP]] $H^1$, and $K = \set{v \in V : v \cdot n \le 0 \text{ on } \Gamma_C}$.
Let $a(u, v) = \int_\Omega \sigma(u) : \varepsilon(v) \, dx$ and $\ell(v) = \int_\Omega f \cdot v \, dx + \int_{\Gamma_N} g \cdot v \, dS$.
Find $u \in K$ with $a(u, v - u) \ge \ell(v - u)$ for all $v \in K$.
The set $K$ is closed and convex, and Korn's inequality makes $a$ coercive on $V$, so the [[Lions–Stampacchia theorem|H80M01T0H8]] gives exactly one weak solution.
Without the contact part, the problem is the mixed boundary value problem of linear elasticity, governed by the [[Lamé equations|GQ3K59MRJP]] in the isotropic case.

Status: solved.
Signorini posed the problem in a course in 1959.
Gaetano Fichera proved existence and uniqueness of the weak solution in the early 1960s, and this work started the theory of variational inequalities.

## Explanations

### L1 human

Put an elastic block on a rigid table and push or pull it.
Some parts of its bottom face stay on the table, others lift off, and nobody tells you which.
The Signorini problem asks for the deformation of the block together with the unknown contact zone.
The table may push the block but cannot pull it, and the block may not sink into the table.
These one-sided conditions turn the usual equations of elasticity into a variational inequality.

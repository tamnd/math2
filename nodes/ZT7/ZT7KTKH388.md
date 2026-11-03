---
tag: ZT7KTKH388
kind: definition
name: Seiberg–Witten theory
msc: [81T60, 81T13, 14H52]
defines: BKKX6C8HR9
uses: [VZ9ZJNWN73, M71M5DQY86, 427N6S6QQW, 5K0N8QMV6Q]
sources:
  - url: https://en.wikipedia.org/wiki/Seiberg–Witten_theory
---

## Definition

Consider four-dimensional $N = 2$ [[supersymmetric|S847N922FY]] [[Yang–Mills theory|A0J2688KZF]] with gauge group $SU(2)$ and dynamical scale $\Lambda > 0$.
Its space of vacua contains the Coulomb branch, a copy of the complex plane.
Its coordinate $u$ is the vacuum expectation value of $\operatorname{tr}\phi^2$ for the adjoint scalar $\phi$.
*Seiberg–Witten theory* is the following description of the low-energy effective theory on the Coulomb branch.

1. The effective theory is a $U(1)$ gauge theory determined by a holomorphic function $\mathcal{F}$, the prepotential, of a local coordinate $a$ on the Coulomb branch.
   Set $a_D = \partial\mathcal{F}/\partial a$ and $\tau = da_D / da$; the imaginary part of $\tau$ is positive and is proportional to the inverse squared effective coupling.
2. To each $u$ is attached an [[elliptic curve|427N6S6QQW]], the Seiberg–Witten curve, which in one standard normalization is $E_u \colon y^2 = (x^2 - u)^2 - \Lambda^4$.
   It is smooth exactly when $u \ne \pm\Lambda^2$.
3. There is a meromorphic differential $\lambda_u$ on $E_u$, the Seiberg–Witten differential, whose derivative in $u$ is a holomorphic differential up to an exact form.
   For a basis $\alpha, \beta$ of the first homology of $E_u$, one has $a = \oint_\alpha \lambda_u$ and $a_D = \oint_\beta \lambda_u$.
   So $\tau$ is the period ratio of the elliptic curve.
4. The mass of a state with electric charge $n_e$ and magnetic charge $n_m$ saturating the BPS bound is $\sqrt{2} \abs{n_e a + n_m a_D}$.

## Remarks

At the two singular points $u = \pm\Lambda^2$, a cycle of $E_u$ shrinks, the corresponding period vanishes, and a monopole or a dyon becomes massless.
Going around a singular point acts on $(a_D, a)$ by an element of $SL(2, \Z)$, which mixes electric and magnetic charges; this is electric-magnetic duality.
Far from the origin, $u \to \infty$, the theory is weakly coupled and $a \approx \sqrt{2u}$ up to normalization, in agreement with [[asymptotic freedom|RRN63RT562]].

Example: as $u \to \pm\Lambda^2$, the curve degenerates to a rational curve with a node, and $\tau$ tends to a cusp of the upper half-plane.
This reflects the fact that the low-energy theory there is a weakly coupled dual photon with a light monopole.

Non-example: $N = 1$ supersymmetric Yang–Mills theory has no Coulomb branch of this kind, and its low-energy theory is not described by a family of elliptic curves.

Normalizations of $u$, $\Lambda$, $\lambda_u$ and of the curve differ between papers; for instance the curve is also written as $y^2 = (x^2 - \Lambda^4)(x - u)$.
The construction extends to other gauge groups and to theories with matter, with curves of higher genus.

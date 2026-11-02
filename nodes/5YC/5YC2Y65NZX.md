---
tag: 5YC2Y65NZX
kind: statement
role: theorem
name: Krylov–Safonov estimate
msc: [35J15, 35B65, 35B45]
uses: [B4TTNHSTRX, M4CEZ5K9HP, 012PBA0FMD, YNH832D50W]
about: [B4TTNHSTRX, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_inequality
---

## Statement

Let $\Omega \subseteq \R^n$ be open and let $0 < \lambda \le \Lambda$.
Let $a_{ij} = a_{ji} \colon \Omega \to \R$ be measurable functions with
$$\lambda \abs{\xi}^2 \le \sum_{i,j=1}^n a_{ij}(x) \xi_i \xi_j \le \Lambda \abs{\xi}^2 \quad \text{for all } x \in \Omega \text{ and } \xi \in \R^n.$$
Let $u \in W^{2,n}_{\mathrm{loc}}(\Omega)$, a local [[Sobolev space|M4CEZ5K9HP]], satisfy $\sum_{i,j} a_{ij} \partial_i \partial_j u = 0$ almost everywhere in $\Omega$.
There are constants $C > 0$ and $\alpha \in (0,1)$, depending only on $n$, $\lambda$ and $\Lambda$, such that for every ball $B_{2r}(x_0)$ with closure in $\Omega$:

1. (Harnack inequality) If $u \ge 0$ in $B_{2r}(x_0)$, then $\sup_{B_r(x_0)} u \le C \inf_{B_r(x_0)} u$.
2. (Hölder estimate) $\abs{u(x) - u(y)} \le C \big(\abs{x-y}/r\big)^{\alpha} \sup_{B_{2r}(x_0)} \abs{u}$ for all $x, y \in B_r(x_0)$.

## Remarks

The equation is an [[elliptic equation|B4TTNHSTRX]] in non-divergence form and the coefficients are only measurable, so the energy methods of De Giorgi, Nash and Moser do not apply.
The proof uses the Aleksandrov–Bakelman–Pucci maximum principle to show that a supersolution which is large on a fixed fraction of a ball is bounded below on a smaller ball.
A covering argument with dyadic cubes in the style of Calderón and Zygmund then turns this into a decay of the measure of level sets, which gives the Harnack inequality.
The [[Hölder continuity|012PBA0FMD]] estimate follows from the Harnack inequality applied to $\sup u - u$ and $u - \inf u$ on shrinking balls.
For $a_{ij} = \delta_{ij}$ the first part is the classical [[Harnack inequality|YNH832D50W]] for harmonic functions.

## Explanations

### L1 human

A non-negative solution of an elliptic equation cannot be huge at one point and tiny at a nearby point: its largest and smallest values on a ball are comparable.
This stays true even when the coefficients of the equation are very rough.
From this one gets that solutions are Hölder continuous.

### L2 human

This is the non-divergence analogue of the De Giorgi–Nash–Moser theorem.
It is the starting point of the regularity theory of fully nonlinear elliptic equations $F(D^2 u) = 0$: differences of solutions satisfy linear equations with measurable coefficients, so they are Hölder continuous.
With concavity of $F$ this leads to the Evans–Krylov theorem on $C^{2,\alpha}$ regularity.
Caffarelli extended the theory to viscosity solutions.

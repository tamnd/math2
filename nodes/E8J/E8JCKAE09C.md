---
tag: E8JCKAE09C
kind: statement
role: theorem
name: Euler's critical load
msc: [74G60, 74K10, 74G05]
uses: [4GAM4KXSM8, 13FGKM7NQ0, T8ENJX1905, 1QCSARFXQ0]
about: [4GAM4KXSM8]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_critical_load
same_as:
  wikidata: Q3658620
  wikipedia: Euler's critical load
---

## Statement

Let a column of length $L > 0$ be initially straight and made of a homogeneous linear elastic material with [[Young's modulus|T8ENJX1905]] $E > 0$.
Let it have constant [[second moment of area|1QCSARFXQ0]] $I > 0$.
Let both ends be pinned, and let a compressive force $P$ act along the axis through the centroids of the end sections.
Model the lateral deflection $w(x)$ by the linearized [[Euler–Bernoulli|13FGKM7NQ0]] equation
$$EI \, w''(x) + P \, w(x) = 0, \qquad w(0) = w(L) = 0.$$
Then this problem has a nonzero solution exactly when $P = n^2 \pi^2 E I / L^2$ for some integer $n \ge 1$, with solution $w(x) = C \sin(n \pi x / L)$.
In particular the smallest load at which the column can [[buckle|4GAM4KXSM8]] is
$$P_{cr} = \frac{\pi^2 E I}{L^2}.$$

## Remarks

The proof is a short computation.
For $P > 0$ write $k^2 = P/(EI)$; the general solution is $w = A \cos kx + B \sin kx$.
The condition $w(0) = 0$ gives $A = 0$, and $w(L) = 0$ with $B \ne 0$ forces $\sin kL = 0$, so $kL = n\pi$.
For $P \le 0$ the only solution is $w = 0$.

For other end conditions the same analysis gives $P_{cr} = \pi^2 E I / (K L)^2$ with an effective length factor $K$.
One has $K = 1/2$ for both ends clamped, $K = 2$ for one end clamped and the other free, and $K \approx 0.699$ for one end clamped and the other pinned.
Dividing by the cross-section area $A$ and writing $r = \sqrt{I/A}$ for the radius of gyration gives the critical stress $\sigma_{cr} = \pi^2 E / (KL/r)^2$.

The hypotheses matter.
The formula assumes the stress stays below the elastic limit.
For short columns $\sigma_{cr}$ would exceed the yield stress and the column fails by yielding first, so [[Johnson's parabolic formula|624BQC6T8E]] is used there.
It also assumes a perfectly straight column with a centred load; real columns have imperfections and are treated by the [[Perry–Robertson formula|A1FNYW0HJ9]].

## Explanations

### L1 human

A long thin column under a push from both ends stays straight until the push reaches a certain size, and then it bows out sideways.
Euler's formula gives that size.
It grows with the stiffness of the material and of the cross-section, and it falls with the square of the length.
So doubling the length of a column cuts its buckling load to a quarter.

### L2 human

The formula comes from a linear eigenvalue problem: the critical loads are the eigenvalues of $-EI\, d^2/dx^2$ with Dirichlet conditions, and the buckling modes are its eigenfunctions.
The linear theory predicts the load at which a bent shape first appears but not the size of the deflection.
The nonlinear [[elastica|CBT8F8S8JT]] shows that the bent branch rises slowly above $P_{cr}$.
The same eigenvalue method gives critical loads for plates and shells, and it is the base of [[Lagrange's problem of the strongest column|DWXSXSN2S2]].

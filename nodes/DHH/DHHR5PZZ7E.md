---
tag: DHHR5PZZ7E
kind: statement
role: theorem
name: Existence of Leray weak solutions
msc: [35Q30, 76D05, 35D30]
uses: [18KXZHVF4M, SJZX81A783, M4CEZ5K9HP]
about: [18KXZHVF4M, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/Navier–Stokes_existence_and_smoothness
---

## Statement

Let $\nu > 0$ and let $u_0 \in L^2(\R^3; \R^3)$ satisfy $\nabla \cdot u_0 = 0$ in the sense of distributions.
Then there exists a vector field $u \in L^\infty\big(0, \infty; L^2(\R^3; \R^3)\big)$ with $\nabla u \in L^2\big(\R^3 \times (0, \infty)\big)$ such that:

1. $u$ is a [[weak solution|SJZX81A783]] of the [[Navier–Stokes equations|18KXZHVF4M]] with no external force and initial value $u_0$.
That is, $\nabla \cdot u(\cdot, t) = 0$ for almost every $t$.
Also, let $\varphi \colon \R^3 \times [0, \infty) \to \R^3$ be any smooth compactly supported test field with $\nabla \cdot \varphi = 0$.
Then
$$\int_0^\infty \!\! \int_{\R^3} \Big( u \cdot \partial_t \varphi + \sum_{i,j=1}^3 u_i u_j \, \partial_j \varphi_i - \nu \nabla u : \nabla \varphi \Big) dx \, dt + \int_{\R^3} u_0 \cdot \varphi(x, 0) \, dx = 0.$$
2. $u$ satisfies the energy inequality: for every $t > 0$,
$$\norm{u(\cdot, t)}_{L^2}^2 + 2 \nu \int_0^t \norm{\nabla u(\cdot, s)}_{L^2}^2 \, ds \le \norm{u_0}_{L^2}^2.$$

Here $\nabla u : \nabla \varphi = \sum_{i,j} \partial_j u_i \, \partial_j \varphi_i$.
A solution with these properties is called a *Leray weak solution*, or a Leray–Hopf weak solution.

## Remarks

Jean Leray proved this theorem in 1934, and Eberhard Hopf later proved the analogue on bounded domains.
The proof regularises the nonlinear term, solves the regularised problem, and uses the energy identity to bound the approximate solutions uniformly in the [[Sobolev space|M4CEZ5K9HP]] norm.
A compactness argument then gives a subsequence whose limit solves the equations in the weak sense, and the energy inequality survives the limit by lower semicontinuity of the norm.
The pressure does not appear, because $\int \nabla p \cdot \varphi \, dx = 0$ for divergence-free $\varphi$.
In two space dimensions the Leray weak solution is unique and smooth for positive times.
In three dimensions its uniqueness and smoothness are open, and they are the heart of the Navier–Stokes existence and smoothness problem.

## Explanations

### L1 human

For the equations of fluid flow in three dimensions, nobody knows how to build smooth solutions that last forever.
Leray found a weaker kind of solution that does always exist: it may be rough, but it obeys the equations on average against smooth test fields.
It also never gains kinetic energy, as a real viscous fluid should not.

### L2 human

The theorem is the starting point of the mathematical theory of the Navier–Stokes equations.
The energy inequality gives the only a priori bound that is known for large data, and the class of solutions it defines is the natural one for studying regularity.
A weak solution that is smooth agrees with the classical solution, and a classical solution is unique among Leray weak solutions while it exists.
Results such as the partial regularity theorem of Caffarelli, Kohn and Nirenberg concern this class of solutions.
Buckmaster and Vicol showed that weak solutions without the energy inequality and with less regularity are not unique.

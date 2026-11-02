---
tag: 7BY5D2THKW
kind: statement
role: theorem
name: Harnack inequality for parabolic equations
msc: [35K10, 35B65, 35B45]
uses: [1CCTH8X2FT, SJZX81A783, VP2HN86VAG, YNH832D50W]
about: [1CCTH8X2FT]
sources:
  - url: https://en.wikipedia.org/wiki/Harnack%27s_inequality
---

## Statement

Let $U \subseteq \R^n$ be open, let $T > 0$, and let $0 < \lambda \le \Lambda$.
Let $A = (a_{ij})$ be a measurable function on $U \times (0, T]$ with values in the symmetric $n \times n$ matrices such that $\lambda \abs{\eta}^2 \le \sum_{i,j} a_{ij}(x, t)\, \eta_i \eta_j \le \Lambda \abs{\eta}^2$ for all $\eta \in \R^n$ and all $(x, t)$.
Let $u \ge 0$ be a [[weak solution|SJZX81A783]] of the [[parabolic equation|1CCTH8X2FT]]
$$\partial_t u = \sum_{i,j=1}^{n} \partial_{x_i}\big(a_{ij}\, \partial_{x_j} u\big) \quad \text{in } U \times (0, T].$$
Let $V$ be a connected open set with compact closure $\overline{V} \subset U$, and let $0 < t_1 < t_2 \le T$.
Then there is a constant $C$, depending only on $n$, $\lambda$, $\Lambda$, $U$, $V$, $t_1$ and $t_2$, such that
$$\sup_{x \in V} u(x, t_1) \le C \inf_{x \in V} u(x, t_2).$$

## Remarks

This is Moser's parabolic Harnack inequality of 1964; the solution is Hölder continuous by the De Giorgi–Nash–Moser theory, so the pointwise values make sense.
Moser's proof bounds $\sup u$ and $\inf u$ on small cylinders by integral means of powers of $u$, using iterated energy estimates.
An estimate for $\log u$ then links the two bounds.
A chain of overlapping cylinders then gives the statement on $V$, which is why $V$ must be connected.
The time lag $t_1 < t_2$ is necessary.
For the [[heat equation|VP2HN86VAG]] $u_t = \Delta u$ on $\R^n$, the solutions $u_y(x, t) = (4\pi t)^{-n/2} e^{-\abs{x - y}^2/(4t)}$ with $y \in \R^n$ satisfy $u_y(x_1, t)/u_y(x_2, t) = e^{(\abs{x_2 - y}^2 - \abs{x_1 - y}^2)/(4t)}$, which is unbounded over $y$ for fixed distinct $x_1, x_2$.
So no bound $\sup_V u(\cdot, t) \le C \inf_V u(\cdot, t)$ at a single time can hold for all nonnegative solutions.
The hypothesis $u \ge 0$ is also necessary, as for [[Harnack's inequality|YNH832D50W]] for harmonic functions.

## Explanations

### L1 human

A nonnegative temperature distribution cannot be very hot at one place now and almost zero at a nearby place a little later.
Heat that is present now spreads, so it raises the temperature nearby at later times.
The inequality makes this precise: the largest value at an earlier time is controlled by the smallest value at a later time.
Looking at the same time is not enough, because a very concentrated source far away can make two nearby points have very different temperatures.

### L2 human

The parabolic Harnack inequality is the time-dependent analogue of [[Harnack's inequality|YNH832D50W]] for nonnegative harmonic functions.
It holds for equations with merely measurable coefficients, which makes it a central tool in the regularity theory of nonlinear parabolic equations.
From it one derives Hölder continuity of solutions and a strong maximum principle.
For the heat equation on Riemannian manifolds with nonnegative Ricci curvature, Li and Yau proved a sharp differential form, which integrates to a Harnack inequality with explicit constants.

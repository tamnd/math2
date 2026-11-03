---
tag: V4WDBZ3D2K
kind: statement
role: theorem
name: Popov criterion
msc: [93D10, 93C10, 93C80]
uses: [Z67CH2W4W6, 86JKV3TRFD, 9A3TBBHRFA, A9WFM77Z4P, C4HN3EAQWM, 4NJC7AGT5N, 0BQAA2BK3Q]
about: [Z67CH2W4W6]
sources:
  - url: https://en.wikipedia.org/wiki/Popov_criterion
same_as:
  wikidata: Q4241326
  wikipedia: Popov criterion
---

## Statement

Let $A$ be a real $n \times n$ [[Hurwitz-stable|9A3TBBHRFA]] matrix, $b \in \R^{n \times 1}$ and $c \in \R^{1 \times n}$, with $(A, b)$ [[controllable|A9WFM77Z4P]] and $(A, c)$ [[observable|C4HN3EAQWM]], and let $G(s) = c(sI - A)^{-1} b$ be the [[transfer function|86JKV3TRFD]].
Let $k > 0$.
Consider the Lur'e system
$$x' = A x + b u, \qquad y = c x, \qquad u = -\psi(y),$$
where $\psi \colon \R \to \R$ is locally Lipschitz, does not depend on time, and lies in the sector $[0, k]$: $0 \le y\, \psi(y) \le k y^2$ for all $y$.
Suppose that there is $\gamma \ge 0$ such that $-1/\gamma$ is not an [[eigenvalue|0BQAA2BK3Q]] of $A$ (no condition when $\gamma = 0$) and
$$\frac{1}{k} + \operatorname{Re} G(i\omega) - \gamma\, \omega \operatorname{Im} G(i\omega) > 0 \quad \text{for all } \omega \in \R.$$
Then the system is absolutely stable for the sector $[0, k]$: for every such $\psi$, the origin is globally asymptotically stable.

## Remarks

The left side equals $\frac{1}{k} + \operatorname{Re}\bigl[(1 + i\gamma\omega) G(i\omega)\bigr]$.
The proof uses the Lur'e–Postnikov Lyapunov function $V(x) = x^T P x + \eta \int_0^{cx} \psi(\sigma) \, d\sigma$ with a constant $\eta \ge 0$ proportional to $\gamma$, whose existence with $P$ positive definite follows from the frequency condition by the [[Kalman–Yakubovich–Popov lemma|4NJC7AGT5N]].
The integral term is why $\psi$ must not depend on time.
For $\gamma = 0$ the condition is that of case 2 of the circle criterion.

Graphically, plot the Popov curve $\omega \mapsto (\operatorname{Re} G(i\omega), \omega \operatorname{Im} G(i\omega))$; the condition says that this curve lies strictly to the right of a straight line through $(-1/k, 0)$ with slope $1/\gamma$.

Example: for $G(s) = 1/((s + 1)(s + 2))$, one finds $\operatorname{Re} G(i\omega) = (2 - \omega^2)/D$ and $\omega \operatorname{Im} G(i\omega) = -3\omega^2/D$ with $D = (2 - \omega^2)^2 + 9\omega^2 > 0$.
With $\gamma = 2$, which is allowed since $-1/2$ is not an eigenvalue, the condition reads $\frac{1}{k} + (2 + 5\omega^2)/D > 0$, which holds for every $k > 0$.
So this loop is absolutely stable for every sector $[0, k]$.

## Explanations

### L1 human

The Popov criterion is a test on the frequency response of the linear part of a loop with one nonlinearity that does not change with time.
Draw a modified Nyquist picture of the linear part.
If a certain tilted line has the whole curve on one side, then the loop is stable for every nonlinearity in the sector.
The freedom to tilt the line makes the test weaker in its demands than the circle criterion.

### L2 human

The criterion is a sufficient answer to the absolute stability problem of Lur'e for time-invariant nonlinearities in a sector $[0, k]$.
The multiplier $1 + \gamma s$ in the frequency condition is what the time invariance buys: it comes from the derivative of the integral term in the Lyapunov function.
It is a standard tool to prove that loops with saturations or dead zones are stable, and it is checked by finding one line on a plot.

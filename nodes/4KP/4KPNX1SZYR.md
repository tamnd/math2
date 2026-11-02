---
tag: 4KPNX1SZYR
kind: statement
role: lemma
name: Barbalat's lemma
msc: [34D05, 34D20]
uses: [0M4JJT780X, 01REYCJ371]
about: [0F2SYCKDT2]
sources:
  - url: https://en.wikipedia.org/wiki/Lyapunov_stability
---

## Statement

Let $f \colon [0, \infty) \to \R$ be differentiable.
Assume that the limit $\lim_{t \to \infty} f(t)$ exists and is finite.
Assume that $f'$ is [[uniformly continuous|0M4JJT780X]] on $[0, \infty)$.
Then $\lim_{t \to \infty} f'(t) = 0$.

## Remarks

Suppose $f'(t) \not\to 0$.
Then there are $\varepsilon > 0$ and times $t_n \to \infty$ with $\abs{f'(t_n)} \ge \varepsilon$.
Uniform continuity gives $\delta > 0$, independent of $n$, with $\abs{f'(t)} \ge \varepsilon / 2$ and constant sign on $[t_n, t_n + \delta]$.
Then $\abs{f(t_n + \delta) - f(t_n)} \ge \varepsilon \delta / 2$ for all $n$, which contradicts the Cauchy criterion for the limit of $f$.

The hypothesis on $f'$ is necessary.
For $f(t) = \sin(t^2) / (t + 1)$, the limit of $f$ is $0$, but $f'(t) = 2t \cos(t^2) / (t + 1) - \sin(t^2) / (t + 1)^2$ does not tend to $0$.
Here $f'$ is not uniformly continuous.

An equivalent form: if $g \colon [0, \infty) \to \R$ is uniformly continuous and $\int_0^\infty g(t) \, dt$ converges, then $g(t) \to 0$.
In stability theory, it is applied to $f(t) = V(t, x(t))$ for a [[Lyapunov function|01REYCJ371]] $V$ along a solution $x$.
If $V$ is bounded below, $\dot V \le 0$ and $\dot V$ is uniformly continuous in $t$, then $\dot V(t, x(t)) \to 0$.

## Explanations

### L1 human

If a quantity settles down to a limit and its rate of change cannot jump suddenly, then the rate of change must die out.
Without the second condition, the quantity could settle while still making ever faster tiny wiggles.

### L2 human

For time-varying systems, LaSalle's invariance principle does not apply directly.
Barbalat's lemma replaces it: from a Lyapunov function with $\dot V \le 0$ one gets $\dot V \to 0$ along solutions, which often forces some components of the state to tend to $0$.
This is a standard step in adaptive control.
A common sufficient condition for uniform continuity of $\dot V$ is that $\ddot V$ is bounded.

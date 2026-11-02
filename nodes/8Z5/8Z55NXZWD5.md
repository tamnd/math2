---
tag: 8Z55NXZWD5
kind: problem
name: Bolza problem
msc: [49K15, 49J15]
uses: [T3V6ZNAMDN, ZPDTVZQN5K, 8M31QKB0GW, 1EQM0DJ4NC, 1J8TYT7C49, XEX7QZV1BS, 7RPV2T29CF]
about: [T3V6ZNAMDN]
sources:
  - url: https://en.wikipedia.org/wiki/Optimal_control
history:
  posed_by: "Oskar Bolza"
  first_stated: "1913"
---

## Problem

Let $U \subseteq \R^m$ be a nonempty set, and let $t_0 < t_1$ be fixed times.
Let $f \colon [t_0, t_1] \times \R^n \times U \to \R^n$ and $L \colon [t_0, t_1] \times \R^n \times U \to \R$ be continuous.
Let $\varphi \colon \R^n \times \R^n \to \R$ be continuous, and let $S \subseteq \R^n \times \R^n$ be a closed set of allowed endpoint pairs.
An [[admissible control|8M31QKB0GW]] is a measurable map $u \colon [t_0, t_1] \to U$ whose trajectory $x$ of the [[control system|ZPDTVZQN5K]] $x'(t) = f(t, x(t), u(t))$ is absolutely continuous on $[t_0, t_1]$ and satisfies $(x(t_0), x(t_1)) \in S$.
The *Bolza problem* asks to minimize the [[functional|1EQM0DJ4NC]]
$$J(u) = \varphi(x(t_0), x(t_1)) + \int_{t_0}^{t_1} L(t, x(t), u(t)) \, dt$$
over all admissible controls $u$.

## Remarks

The cost has two parts: an endpoint term $\varphi$ and a running term given by the integral of $L$.
The case $L = 0$ is the Mayer problem, and the case $\varphi = 0$ is the Lagrange problem; see [[Mayer and Lagrange problems|1J8TYT7C49]].
The three forms are equivalent: adding the state $y' = L(t, x, u)$ with $y(t_0) = 0$ turns the Bolza cost into the endpoint cost $\varphi(x(t_0), x(t_1)) + y(t_1)$.
In the classical calculus of variations the control is the velocity, $f(t, x, u) = u$, and the problem is to minimize $\varphi(x(t_0), x(t_1)) + \int_{t_0}^{t_1} L(t, x, x') \, dt$ with possible side conditions.
Necessary conditions for a minimizer are given by [[Pontryagin's maximum principle|7RPV2T29CF]], with transversality conditions coming from $\varphi$ and $S$.
Existence of a minimizer needs extra hypotheses, such as compactness of $U$ and convexity of the set of velocities and costs; see [[Filippov's existence theorem|XEX7QZV1BS]].

## Explanations

### L1 human

A Bolza problem asks for the best way to steer a system when one pays both along the way and at the end.
The running cost might be fuel spent, and the end cost might be a penalty for missing a target.
Many optimal control problems in engineering and economics take this form.

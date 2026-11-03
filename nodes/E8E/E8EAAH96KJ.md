---
tag: E8EAAH96KJ
kind: definition
name: Passivity
msc: [93D30, 93C10, 93D25]
defines: HW9JJGS944
uses: [0X3WGX95FE, 0NT64JV96A, 0F2SYCKDT2]
sources:
  - url: https://en.wikipedia.org/wiki/Passivity_(engineering)
---

## Definition

Let $m, n \ge 1$ and consider a system with inputs and outputs given by the [[ordinary differential equation|0NT64JV96A]]
$$x' = f(x, u), \qquad y = h(x, u),$$
with state $x(t) \in \R^n$, input $u(t) \in \R^m$ and output $y(t) \in \R^m$.
The system is *passive* if there is a [[continuous function|0X3WGX95FE]] $V \colon \R^n \to [0, \infty)$, called a storage function, with the following property.
For every input $u$, every solution $x$ on an interval containing $t_0 \le t_1$, and the corresponding output $y$,
$$V(x(t_1)) - V(x(t_0)) \le \int_{t_0}^{t_1} u(t)^T y(t) \, dt.$$
It is *lossless* if equality always holds.
A memoryless system $y = h(t, u)$ is passive if $u^T h(t, u) \ge 0$ for all $t$ and $u$.

## Remarks

If $V$ is continuously differentiable, the condition is equivalent to $\nabla V(x) \cdot f(x, u) \le u^T h(x, u)$ for all $x$ and $u$.
The quantity $u^T y$ is the power supplied to the system, and $V$ is the energy stored in it.
If $V$ is positive definite and the system is passive, then with $u = 0$ the function $V$ does not increase along solutions, so the origin of $x' = f(x, 0)$ is [[Lyapunov stable|0F2SYCKDT2]].

Example: the integrator $x' = u$, $y = x$ with $V(x) = x^2/2$.
Then $\frac{d}{dt} V(x(t)) = x u = u y$, so the system is passive and even lossless.

Non-example: the memoryless system $y = -u$.
It has $u y = -u^2 < 0$ for $u \ne 0$, so it delivers energy instead of absorbing it, and it is not passive.

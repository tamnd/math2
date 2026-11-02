---
tag: V6E2R7JNN8
kind: definition
name: Exponential stability
msc: [34D20, 93D20]
defines: VY180V8QY2
uses: [0G4X36AE0X, 02903SSA48, 0VW90BBSJ4]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_stability
---

## Definition

Let $U \subseteq \R^n$ be open, let $f \colon U \to \R^n$ be [[continuously differentiable|0VW90BBSJ4]], and let $\varphi$ be the [[flow|02903SSA48]] of $x' = f(x)$.
An [[equilibrium point|0G4X36AE0X]] $x^*$ is *exponentially stable* if there are constants $\delta > 0$, $C \ge 1$ and $\alpha > 0$ such that for every $x_0 \in U$ with $\norm{x_0 - x^*} < \delta$:

1. the solution $\varphi_t(x_0)$ exists for all $t \ge 0$;
2. $\norm{\varphi_t(x_0) - x^*} \le C e^{-\alpha t} \norm{x_0 - x^*}$ for all $t \ge 0$.

## Remarks

An exponentially stable equilibrium is asymptotically stable.
If $f$ is of class $C^2$, then $x^*$ is exponentially stable if and only if every eigenvalue of $Df(x^*)$ has negative real part.

Example: $x' = -x$ on $\R$ with $x^* = 0$.
The solution is $x_0 e^{-t}$, so clause 2 holds with $C = 1$ and $\alpha = 1$, for any $\delta$.

Non-example: $x' = -x^3$ on $\R$ with $x^* = 0$.
The solution is $x(t) = x_0 / \sqrt{1 + 2 x_0^2 t}$, since $\frac{d}{dt} x^{-2} = 2$.
It tends to $0$, but $x(t) e^{\alpha t} \to \infty$ for each $\alpha > 0$ and $x_0 \ne 0$, so clause 2 fails.

For a time-dependent system $x' = f(t, x)$ with $f(t, 0) = 0$, the origin is uniformly exponentially stable if $\norm{x(t)} \le C e^{-\alpha (t - t_0)} \norm{x(t_0)}$ for all $t \ge t_0$, all initial times $t_0$ and all $\norm{x(t_0)} < \delta$.

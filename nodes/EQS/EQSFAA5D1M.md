---
tag: EQSFAA5D1M
kind: definition
name: Integral functional with a Lagrangian density
msc: [49J10, 49K10, 49K05]
defines: JRQZ803Q5Y
uses: [1EQM0DJ4NC, 02BH3MCBQB, 0VW90BBSJ4, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_variations
---

## Definition

Let $n, m \ge 1$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]], and let $\overline{\Omega}$ be its closure.
Let $L \colon \overline{\Omega} \times \R^m \times \R^{m \times n} \to \R$, written $L(x, z, p)$, be a continuous function, called the *Lagrangian density*.
For a [[continuously differentiable|0VW90BBSJ4]] map $u \in C^1(\overline{\Omega}; \R^m)$ with Jacobian matrix $Du$, set
$$J(u) = \int_\Omega L\big(x, u(x), Du(x)\big) \, dx.$$
The [[functional|1EQM0DJ4NC]] $J \colon C^1(\overline{\Omega}; \R^m) \to \R$ is the *integral functional* with Lagrangian density $L$.
The integrand is continuous and bounded on $\Omega$, so the [[Lebesgue integral|DWJF7ABPR1]] is finite.

## Remarks

In one variable, with $n = m = 1$ and $\Omega = (a, b)$, the functional reads $J(y) = \int_a^b L(x, y(x), y'(x)) \, dx$.
Example: $L(x, z, p) = \frac{1}{2} \abs{p}^2$ with $m = 1$ gives the Dirichlet energy $J(u) = \frac{1}{2} \int_\Omega \abs{\nabla u}^2 \, dx$.
It is an integral functional because this $L$ is continuous on all of $\overline{\Omega} \times \R \times \R^n$.
Non-example: on $\Omega = (0, 1)$, the expression $L(x, z, p) = 1/x$ is not defined at $x = 0$ and has no continuous extension to $[0, 1] \times \R \times \R$, and indeed $\int_0^1 dx / x = \infty$ for every $y$.
The same name is used for Lagrangians with higher derivatives, as in the [[Euler–Poisson equation|XBNAJ1RRET]], and for $u$ in [[Sobolev spaces|M4CEZ5K9HP]] under growth conditions on $L$.

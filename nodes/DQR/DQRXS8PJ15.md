---
tag: DQRXS8PJ15
kind: definition
name: Heaviside operational calculus
msc: [44A45]
defines: QQ98C2AXZP
uses: [BB15T3J891, 09C4JP7Y0M, 0QQRP17Z7S, 8050R3Z6HA]
sources:
  - url: https://en.wikipedia.org/wiki/Operational_calculus
---

## Definition

Let $H$ be the [[Heaviside step function|09C4JP7Y0M]], and consider functions of $t$ that vanish for $t < 0$.
The *Heaviside operational calculus* is the formal method that works with the following conventions.

1. The [[differentiation operator|BB15T3J891]] $d/dt$ is written $p$, and $p^{-1}$ means integration from $0$: $(p^{-1} f)(t) = \int_0^t f(\tau) \, d\tau$.
2. For each integer $n \ge 0$, $p^{-n} H = \frac{t^n}{n!} H$.
3. Consider a system governed by a [[linear differential equation|0QQRP17Z7S]] with constant coefficients, at rest before $t = 0$. Replace $d/dt$ by $p$ and solve the equation algebraically for $x$. The response $x$ to the input $H$ is then written $x = \varphi(p) H$ with a rational function $\varphi$.
4. $\varphi(p) H$ is evaluated by expanding $\varphi(p)$ in powers of $p^{-1}$ and applying rule 2 term by term, or by the expansion theorem.

## Remarks

In modern terms, $\varphi(p) H$ is the function whose Laplace transform is $\varphi(s)/s$, and rule 2 says that $\mathcal{L}(t^n/n!) = 1/s^{n+1}$.
For rational $\varphi$ that is bounded at infinity, the series in rule 4 converges for all $t$ and the method is correct.
Heaviside also applied the rules to non-rational expressions such as $\sqrt{p}$, where they need a separate justification.

Example: $x' - a x = a H$, with $x = 0$ for $t < 0$.
Rule 3 gives $(p - a) x = a H$, so $x = \frac{a}{p - a} H = \frac{a/p}{1 - a/p} H = \sum_{n \ge 1} a^n p^{-n} H = \sum_{n \ge 1} \frac{a^n t^n}{n!} = e^{at} - 1$ for $t \ge 0$.
Check: $x' - ax = a e^{at} - a e^{at} + a = a$ and $x(0) = 0$.

Non-example: the rules do not apply to an equation with variable coefficients such as $x' - t x = H$.
There $p$ does not commute with multiplication by $t$, so the equation cannot be solved for $x$ as $\varphi(p) H$.

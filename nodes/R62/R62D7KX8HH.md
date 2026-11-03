---
tag: R62D7KX8HH
kind: definition
name: Ramsey–Cass–Koopmans model
msc: [91B62, 49K15]
defines: D03R7HF5KZ
uses: [223GCENAVJ, EZ8NBZ8D0E, GZZS4MTDG9, 0GCM7B6PBK, 7RPV2T29CF]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey%E2%80%93Cass%E2%80%93Koopmans_model
---

## Definition

Let $f$ be an intensive production function as in the [[Solow–Swan model|223GCENAVJ]].
So $f(0) = 0$, $f$ is strictly increasing and strictly [[concave|0GCM7B6PBK]], and $f$ satisfies the Inada conditions.
Let $n \ge 0$ be the growth rate of the population, $\delta \ge 0$ the depreciation rate, and $\rho > n$ the rate of time preference.
Let $u \colon (0, \infty) \to \R$ be a twice differentiable [[utility function|GZZS4MTDG9]] with $u' > 0$, $u'' < 0$ and $u'(c) \to \infty$ as $c \to 0$.

The *Ramsey–Cass–Koopmans model* is the [[optimal control|EZ8NBZ8D0E]] problem: given $k_0 > 0$, choose a consumption path $c(t) > 0$ to maximise
$$\int_0^\infty e^{-(\rho - n) t} \, u(c(t)) \, dt$$
subject to
$$\dot k(t) = f(k(t)) - c(t) - (n + \delta) k(t), \qquad k(0) = k_0, \qquad k(t) \ge 0.$$
Here $c$ and $k$ are consumption and capital per person.

## Remarks

By [[Pontryagin's maximum principle|7RPV2T29CF]], an interior optimal path satisfies the Euler equation
$$\frac{\dot c}{c} = \frac{f'(k) - \delta - \rho}{\sigma(c)}, \qquad \sigma(c) = -\frac{c\, u''(c)}{u'(c)},$$
together with the capital equation and a transversality condition at infinity.
The steady state $(k^*, c^*)$ is given by $f'(k^*) = \rho + \delta$ and $c^* = f(k^*) - (n + \delta) k^*$.
This is the modified golden rule.

Example: let $f(k) = k^\alpha$ with $0 < \alpha < 1$ and $u(c) = \ln c$, so $\sigma = 1$.
Then $\alpha (k^*)^{\alpha - 1} = \rho + \delta$, so $k^* = \left( \alpha/(\rho + \delta) \right)^{1/(1 - \alpha)}$.

Non-example: if $\rho \le n$, the clause $\rho > n$ fails.
Then a constant consumption path with $u(c) > 0$ gives an infinite integral, and the maximisation problem is not well posed.

The steady state is a saddle point of the system in $(k, c)$, and the optimal path is the stable arm that leads to it.
The model is named after Frank Ramsey, David Cass and Tjalling Koopmans.

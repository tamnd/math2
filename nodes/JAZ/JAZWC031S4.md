---
tag: JAZWC031S4
kind: definition
name: Hamilton's principal function
msc: [70H20, 49L12]
defines: YM2P1ENF0B
uses: [T0WAGV4KP4, BEM454AYTT, MPM0RHWCN6, 5TRXQKP7DY]
sources:
  - url: https://en.wikipedia.org/wiki/Hamilton%E2%80%93Jacobi_equation
---

## Definition

Let $L(q, \dot q, t)$ be a Lagrangian of class $C^2$ on $U \times \R^n \times I$, with $U \subseteq \R^n$ and $I \subseteq \R$ open.
Fix $q_0 \in U$ and $t_0 \in I$, and let $W \subseteq U \times I$ be an open set of points $(q, t)$ with $t > t_0$.
Assume that for each $(q, t) \in W$ there is a unique solution $\gamma_{q, t} \colon [t_0, t] \to U$ of the [[Lagrange equations|BEM454AYTT]] of $L$ with $\gamma_{q, t}(t_0) = q_0$ and $\gamma_{q, t}(t) = q$.
Assume also that $\gamma_{q, t}(s)$ is of class $C^2$ in $(q, t, s)$.
*Hamilton's principal function* is the function $S \colon W \to \R$ given by the [[action|T0WAGV4KP4]]
$$S(q, t) = \int_{t_0}^{t} L\big(\gamma_{q, t}(s), \dot \gamma_{q, t}(s), s\big) \, ds.$$

## Remarks

Assume that $L$ is hyperregular, with [[Hamiltonian|MPM0RHWCN6]] $H$.
Let $p$ be the momentum of $\gamma_{q, t}$ at time $t$.
The first variation of the action with free endpoint gives $\nabla_q S(q, t) = p$ and $\partial_t S(q, t) = -H(q, p, t)$.
Hence $S$ solves the [[Hamilton–Jacobi equation|5TRXQKP7DY]] $\partial_t S + H(q, \nabla_q S, t) = 0$.

Example: for $L = \frac{1}{2} m \dot q^2$ with $n = 1$, the path is $\gamma(s) = q_0 + (q - q_0)(s - t_0)/(t - t_0)$, and
$$S(q, t) = \frac{m (q - q_0)^2}{2 (t - t_0)}.$$
Check: $\partial_t S = -\frac{m (q - q_0)^2}{2 (t - t_0)^2}$ and $\frac{1}{2m} (\partial_q S)^2 = \frac{m (q - q_0)^2}{2 (t - t_0)^2}$, so $\partial_t S + \frac{1}{2m} (\partial_q S)^2 = 0$.

Non-example: for the oscillator $L = \frac{1}{2} \dot q^2 - \frac{1}{2} q^2$, every solution starting at $q_0$ at $t_0$ is at $-q_0$ at time $t_0 + \pi$.
So for $t = t_0 + \pi$ there is no solution ending at $q \ne -q_0$ and infinitely many ending at $-q_0$, and $S$ is not defined near such points.

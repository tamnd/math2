---
tag: TVGNQ7PH4Y
kind: definition
name: Group velocity
msc: [78A40, 35L05]
defines: C05DPKD4S0
uses: [R5P8M6SBG7, FMDA4DKT0M, 0ABK9V9Y64]
sources:
  - url: https://en.wikipedia.org/wiki/Group_velocity
---

## Definition

Consider a linear wave equation in $\R^d$ with a branch $\omega = W(k)$ of its [[dispersion relation|R5P8M6SBG7]].
Assume that $W$ is real-valued and differentiable on an open set $U \subseteq \R^d$ of wave vectors.
The *group velocity* at the wave vector $k \in U$ is the [[gradient|0ABK9V9Y64]]
$$v_g(k) = \nabla_k W(k).$$
In one dimension it is $v_g = d\omega / dk$.

## Remarks

A wave packet $u(x, t) = \int a(k) e^{i(k \cdot x - W(k) t)} dk$ with an amplitude $a$ concentrated near $k_0$ moves, to first order, with velocity $v_g(k_0)$: expanding $W(k) \approx W(k_0) + v_g(k_0) \cdot (k - k_0)$ gives $u(x, t) \approx e^{i(k_0 \cdot x - W(k_0) t)} \, f(x - v_g(k_0) t)$ for a fixed envelope $f$.
In one dimension, $v_g = v_p + k \, dv_p / dk$, where $v_p = \omega / k$ is the [[phase velocity|FMDA4DKT0M]]; the two agree exactly when the equation is non-dispersive.

Example: light in a cold plasma has $\omega = \sqrt{\omega_p^2 + c^2 k^2}$ with plasma frequency $\omega_p > 0$.
Then $v_g = c^2 k / \omega < c$ and $v_p = \omega / k > c$, and $v_g v_p = c^2$.

Non-example: the ratio $\omega / k$ is not the group velocity in a dispersive medium.
For deep water waves, $\omega = \sqrt{g k}$ with gravitational acceleration $g$, so $v_g = \frac{1}{2} \sqrt{g / k}$, while $\omega / k = \sqrt{g / k}$.

## Explanations

### L1 human

The group velocity is the derivative of frequency with respect to wave number.
It tells how fast a short burst of waves moves as a whole.

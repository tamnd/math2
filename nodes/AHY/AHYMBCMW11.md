---
tag: AHYMBCMW11
kind: definition
name: Huber loss
msc: [62F35, 62G35]
defines: RATW595XR9
uses: [3BTG6VVCGZ, 4503R8BVF8, 0VV0HSW1ZS]
sources:
  - url: https://en.wikipedia.org/wiki/Huber_loss
---

## Definition

Let $\delta > 0$.
The *Huber loss* with threshold $\delta$ is the function $L_\delta \colon \R \to \R$ given by
$$L_\delta(a) = \begin{cases} \dfrac{a^2}{2} & \text{if } \abs{a} \le \delta, \\[1ex] \delta\Big(\abs{a} - \dfrac{\delta}{2}\Big) & \text{if } \abs{a} > \delta. \end{cases}$$

## Remarks

The two pieces agree at $\abs{a} = \delta$, where both equal $\delta^2/2$, and so do their derivatives.
So $L_\delta$ is [[convex|0VV0HSW1ZS]] and continuously differentiable, with derivative $\psi_\delta(a) = \max(-\delta, \min(\delta, a))$, the residual clipped to $[-\delta, \delta]$.
Huber's [[M-estimator|4503R8BVF8]] of location minimises $\sum_{i=1}^{n} L_\delta(x_i - \mu)$ over $\mu \in \R$, or equivalently solves $\sum_i \psi_\delta(x_i - \mu) = 0$.
As $\delta \to \infty$ it tends to the mean, and as $\delta \to 0$ it tends to the median.

Example: with $\delta = 1$, $L_1(0.5) = 0.125$, as for squared loss, and $L_1(3) = 3 - 0.5 = 2.5$, much less than $3^2/2 = 4.5$.

Non-example: the function $a \mapsto \abs{a}$ grows linearly but is not differentiable at $0$.
It is not quadratic on any interval around $0$, so it is not a Huber loss for any $\delta$.

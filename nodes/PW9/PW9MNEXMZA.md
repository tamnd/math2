---
tag: PW9MNEXMZA
kind: definition
name: Mohr's circle
msc: [74A10]
defines: DED41X44XM
uses: [KG2XWEMJ30, M6ZWV4Y29A]
sources:
  - url: https://en.wikipedia.org/wiki/Mohr%27s_circle
---

## Definition

Consider a plane state of stress, given by the symmetric matrix $\begin{pmatrix} \sigma_x & \tau_{xy} \\ \tau_{xy} & \sigma_y \end{pmatrix}$ of a [[Cauchy stress tensor|KG2XWEMJ30]] in the plane.
For the unit normal $n = (\cos\theta, \sin\theta)$ and the unit tangent $m = (-\sin\theta, \cos\theta)$, let the normal and shear stresses on the line with normal $n$ be
$$\sigma_n = n \cdot \sigma n = \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2} \cos 2\theta + \tau_{xy} \sin 2\theta,$$
$$\tau_n = m \cdot \sigma n = -\frac{\sigma_x - \sigma_y}{2} \sin 2\theta + \tau_{xy} \cos 2\theta.$$
*Mohr's circle* is the circle in the $(\sigma_n, \tau_n)$-plane with centre $(c, 0)$ and radius $R$, where
$$c = \frac{\sigma_x + \sigma_y}{2}, \qquad R = \sqrt{\left( \frac{\sigma_x - \sigma_y}{2} \right)^2 + \tau_{xy}^2}.$$
As $\theta$ varies, the point $(\sigma_n, \tau_n)$ runs over the whole circle.

## Remarks

The identity $(\sigma_n - c)^2 + \tau_n^2 = R^2$ follows from $\cos^2 2\theta + \sin^2 2\theta = 1$.
The circle meets the axis $\tau_n = 0$ at $c \pm R$, the two [[principal stresses|M6ZWV4Y29A]] of the plane state, and the maximum shear stress is $R$.
For $\sigma_x = 3$, $\sigma_y = -1$, $\tau_{xy} = 0$, one has $c = 1$ and $R = 2$, so the principal stresses are $3$ and $-1$, and the maximum shear stress $2$ occurs at $\theta = 45$ degrees.
A point such as $(\sigma_n, \tau_n) = (1, 3)$ is not on this circle, so no orientation produces it.
The sign convention for $\tau_n$ varies between texts, which flips the circle about the horizontal axis.
In three dimensions the admissible points $(n \cdot \sigma n, \abs{\sigma n - (n \cdot \sigma n) n})$ lie in the region between three circles built on the pairs of principal stresses.

## Explanations

### L1 human

Mohr's circle turns the formulas for rotating stresses into a circle drawn on paper.
Reading off the circle gives the principal stresses and the largest shear stress.

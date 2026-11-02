---
tag: KWQYX7B6P5
kind: definition
name: Angle of parallelism
msc: [51M10, 51M09]
defines: 323GN6K117
uses: [GN4N94GQ0Z, 0GJAJC6TNZ, 1WN9B18H86]
sources:
  - url: https://en.wikipedia.org/wiki/Angle_of_parallelism
---

## Definition

Let $\mathbb{H}^2$ be the [[hyperbolic plane|GN4N94GQ0Z]] of constant curvature $-1$.
Let $\ell$ be a line and $P$ a point not on $\ell$.
Let $Q$ be the foot of the perpendicular from $P$ to $\ell$, and let $a = d(P, Q) > 0$.
A ray from $P$ meets $\ell$ when its [[angle|0GJAJC6TNZ]] with the ray $PQ$ is small.
Fix a side of the line $PQ$, and for $\theta \in [0, \pi/2]$ let $r_\theta$ be the ray from $P$ on that side at angle $\theta$ with $PQ$.
The *angle of parallelism* $\Pi(a)$ is the supremum of the angles $\theta$ such that $r_\theta$ meets $\ell$.
The ray at angle exactly $\Pi(a)$ does not meet $\ell$; it is a *limiting parallel* to $\ell$ through $P$.

## Remarks

The value does not depend on the side of $PQ$, nor on $\ell$ and $P$, only on $a$, and Lobachevsky's formula gives
$$\tan \frac{\Pi(a)}{2} = e^{-a}, \qquad \text{equivalently} \qquad \cos \Pi(a) = \tanh a, \quad \sin \Pi(a) = \frac{1}{\cosh a}.$$
Example: in the [[Beltrami–Klein model|1WN9B18H86]], take $P$ the centre and $\ell$ the chord $x = r$ with $0 < r < 1$.
Lines through the centre are diameters, so the foot is $Q = (r, 0)$ and $a = \operatorname{artanh} r$.
The limiting parallels are the chords from $P$ to the endpoints $(r, \pm\sqrt{1 - r^2})$, which make angle $\theta$ with $\cos \theta = r$ at the centre; angles at the centre are Euclidean in this model.
So $\cos \Pi(a) = r = \tanh a$, as the formula says.
Non-example: in the Euclidean plane every ray from $P$ at angle less than $\pi/2$ with $PQ$ meets $\ell$, and the ray at angle $\pi/2$ is the unique parallel.
There the supremum is $\pi/2$ for every $a$, so the angle carries no information about distance.
In curvature $-k^2$, the formula holds with $a$ replaced by $ka$.

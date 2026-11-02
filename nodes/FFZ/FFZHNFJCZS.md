---
tag: FFZHNFJCZS
kind: conjecture
name: Mahler conjecture
msc: [52A40, 52A20]
uses: [437FSG3419, 2Z2QVWZ262, 0S52TNNTH9]
about: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Mahler_volume
history:
  posed_by: Kurt Mahler
  first_stated: "1939"
---

## Statement

Let $n \ge 1$ and let $K \subseteq \R^n$ be a compact [[convex body|437FSG3419]] with nonempty interior and $K = -K$.
Let $K^\circ = \set{y \in \R^n : x \cdot y \le 1 \text{ for all } x \in K}$ be its polar body, with $x \cdot y$ the [[dot product|0S52TNNTH9]], and let $\operatorname{vol}$ be [[Lebesgue measure|2Z2QVWZ262]].
The conjecture states that
$$\operatorname{vol}(K) \operatorname{vol}(K^\circ) \ge \frac{4^n}{n!},$$
which is the value for the cube $[-1, 1]^n$.

## Remarks

For the cube, $\operatorname{vol}([-1,1]^n) = 2^n$ and its polar is the cross-polytope of volume $2^n / n!$, which gives $4^n / n!$.
The conjecture is proved for $n = 2$, by Mahler, and for $n = 3$, by Iriyama and Shibata.
It is known for some classes of bodies, such as unconditional bodies and zonoids.
In general the Bourgain–Milman inequality gives $\operatorname{vol}(K) \operatorname{vol}(K^\circ) \ge c^n \frac{4^n}{n!}$ for an absolute constant $c > 0$, and Kuperberg gave an explicit such constant.
The upper bound is the [[Blaschke–Santaló inequality|MNJ030R4CA]].
There is also a version for convex bodies that are not symmetric, in which the simplex is the conjectured minimizer.

## Explanations

### L1 human

Multiply the volume of a symmetric convex shape by the volume of its polar shape.
The result does not change when the shape is stretched.
The largest possible product is reached by balls.
Mahler conjectured that the smallest possible product is reached by the cube, and this is still open in dimension four and higher.

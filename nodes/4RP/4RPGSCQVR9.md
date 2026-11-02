---
tag: 4RPGSCQVR9
kind: definition
name: Minkowski content
msc: [28A75, 28A80]
defines: HS2NTCMZ4T
uses: [2Z2QVWZ262, 0T3RZQXDYD, 0VKD1TP7F3, Q1TGZK8RN6]
sources:
  - url: https://en.wikipedia.org/wiki/Minkowski_content
---

## Definition

Let $A \subseteq \R^n$, and let $\mathcal{L}^n$ be [[Lebesgue measure|2Z2QVWZ262]] on $\R^n$.
For $r > 0$, let $A_r = \set{x \in \R^n : \abs{x - a} < r \text{ for some } a \in A}$.
Let $0 \le m \le n$ be an integer, and let $\alpha(k)$ be the volume of the unit ball of $\R^k$, with $\alpha(0) = 1$.
The *upper* and *lower $m$-dimensional Minkowski contents* of $A$ are
$$\mathcal{M}^{*m}(A) = \limsup_{r \to 0^+} \frac{\mathcal{L}^n(A_r)}{\alpha(n - m) \, r^{n - m}}, \qquad \mathcal{M}^m_*(A) = \liminf_{r \to 0^+} \frac{\mathcal{L}^n(A_r)}{\alpha(n - m) \, r^{n - m}}.$$
If they are equal, their common value $\mathcal{M}^m(A)$ is the *$m$-dimensional Minkowski content* of $A$.

## Remarks

The [[limit superior|0T3RZQXDYD]] and limit inferior always exist in $[0, \infty]$.
The same formulas with a real exponent $s$ in place of $m$ are also used, with a suitable constant.

Example: let $A \subseteq \R^2$ be a segment of length $L$ and $m = 1$.
Then $A_r$ is a rectangle of area $2 r L$ with two half-discs of radius $r$, so $\mathcal{L}^2(A_r) = 2 r L + \pi r^2$.
Since $\alpha(1) = 2$, the ratio is $L + \pi r / 2 \to L$, so $\mathcal{M}^1(A) = L$.

Minkowski content does not ignore countable sets.
For $A = \Q \cap [0, 1]$ in $\R$ with $m = 1$, one has $A_r = (-r, 1 + r)$, so $\mathcal{M}^1(A) = 1$, although $A$ has Lebesgue measure $0$.
Thus Minkowski content is not countably additive.

For a closed set $A \subseteq \R^n$ that is the image of a bounded subset of $\R^m$ under a Lipschitz map, $\mathcal{M}^m(A)$ exists and equals its normalized $m$-dimensional [[Hausdorff measure|Q1TGZK8RN6]].

## Explanations

### L1 human

Thicken the set a little, measure the volume of the thickening, and divide by the volume one would expect from an $m$-dimensional set.
The limit of this ratio is the $m$-dimensional size of the set.

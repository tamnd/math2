---
tag: Y2DKZH3CCT
kind: statement
role: theorem
name: Singer's theorem
msc: ["37E05", "37C25"]
uses: [6ZPKWE0VAZ, 0YTCMFB4HC, T75CZ5H47N, 0AA97XA70K, QN9X9BNKTX]
about: [6ZPKWE0VAZ]
sources:
  - url: https://en.wikipedia.org/wiki/Schwarzian_derivative
---

## Statement

Let $I \subset \R$ be a compact interval and let $f \colon I \to I$ be a map of class $C^3$ with finitely many [[critical points|0YTCMFB4HC]].
Assume that $f$ has negative [[Schwarzian derivative|6ZPKWE0VAZ]]:
$$Sf(x) = \frac{f'''(x)}{f'(x)} - \frac{3}{2} \left( \frac{f''(x)}{f'(x)} \right)^2 < 0 \quad \text{for every } x \in I \text{ with } f'(x) \neq 0.$$
Let $\mathcal{O}$ be an attracting [[periodic orbit|0AA97XA70K]] of $f$, that is, the orbit of a point $p$ with $f^n(p) = p$ and $\abs{(f^n)'(p)} < 1$.
The immediate basin of $\mathcal{O}$ is the union of the connected components of its basin of attraction that contain a point of $\mathcal{O}$.
Then the immediate basin of $\mathcal{O}$ contains a critical point of $f$ or a boundary point of $I$.
In particular, the number of attracting periodic orbits of $f$ is at most the number of critical points of $f$ plus $2$.

## Remarks

The key fact is that the Schwarzian derivative of a composition satisfies $S(g \circ f) = (Sg \circ f) \, (f')^2 + Sf$, so negative Schwarzian passes to all iterates $f^n$.
Then $\abs{(f^n)'}$ has no positive local minimum on an interval where $f^n$ is monotone (the minimum principle).
Suppose the component $J$ of the immediate basin that contains $p$ had no critical point and no boundary point.
Then $f^n$ would map $J$ diffeomorphically onto itself, and the minimum principle applied there gives a contradiction.

Example: for the [[logistic map|QN9X9BNKTX]] $f_r(x) = r x (1 - x)$ with $1 < r \le 4$, one computes $S f_r = -\frac{3}{2} \left( \frac{-2}{1 - 2x} \right)^2 < 0$.
Its only critical point is $1/2$, and the boundary points are not in the basin of an interior attracting orbit, since $0$ is a repelling fixed point and $f_r(1) = 0$.
So $f_r$ has at most one attracting periodic orbit in $(0, 1)$, and if it has one, the orbit of $1/2$ converges to it.
This is why, in numerical experiments, one iterates the critical point to find the attracting orbit.

The hypothesis on the Schwarzian derivative is necessary.
For $N \ge 3$ and $0 < a < 1$, the map $f(x) = x + \frac{a}{2\pi N} \sin(2 \pi N x)$ is an increasing diffeomorphism of $[0, 1]$ with no critical points, and it has the $N$ attracting fixed points $\frac{2j + 1}{2N}$, $0 \le j < N$, where $f' = 1 - a$.
This is more than $0 + 2$, so the Schwarzian derivative of this map cannot be negative everywhere.

## Explanations

### L1 human

For many smooth maps of an interval, every stable cycle must attract one of the turning points of the map.
So a map with only one turning point, like the logistic map, can have at most one stable cycle inside the interval, and following the turning point reveals it.
The condition that makes this work is a sign condition on a particular combination of derivatives, the Schwarzian derivative.

### L2 human

David Singer proved the theorem in 1978.
Negative Schwarzian derivative is the standard hypothesis in one-dimensional dynamics: it holds for all real quadratic maps and is preserved under composition.
Combined with kneading theory, it gives a fine picture of the logistic family, where at each parameter there is at most one attracting cycle.
It is also used in the study of neutral cycles, which with negative Schwarzian are attracting from at least one side.

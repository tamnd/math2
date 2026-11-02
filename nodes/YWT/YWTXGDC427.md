---
tag: YWTXGDC427
kind: definition
name: Chebyshev nodes
msc: [65D05, 41A05, 33C45]
defines: HYK8J56PSH
uses: [M6EAR1JHPP, 0TK8Y3J5RW]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev_nodes
---

## Definition

Let $n \ge 1$ be an integer.
The *Chebyshev nodes* of order $n$ in $[-1, 1]$ are the $n$ numbers
$$x_k = \cos\left(\frac{(2k - 1)\pi}{2n}\right), \qquad k = 1, \dots, n.$$
They are the zeros of the [[Chebyshev polynomial|M6EAR1JHPP]] $T_n$ of the first kind.
For an [[interval|0TK8Y3J5RW]] $[a, b]$ with $a < b$, the Chebyshev nodes of order $n$ in $[a, b]$ are the numbers $\frac{a + b}{2} + \frac{b - a}{2} x_k$, $k = 1, \dots, n$.

## Remarks

Example: for $n = 3$ the nodes are $\cos(\pi/6), \cos(\pi/2), \cos(5\pi/6)$, that is $\sqrt{3}/2$, $0$ and $-\sqrt{3}/2$.
Check: $T_3(x) = 4x^3 - 3x = x(4x^2 - 3)$ vanishes exactly there.

Non-example: the equally spaced points $-1, 0, 1$ are not the Chebyshev nodes of order $3$, since $T_3(1) = 1 \ne 0$.

The node polynomial is $\prod_{k=1}^{n} (x - x_k) = 2^{1-n} T_n(x)$, whose maximum on $[-1, 1]$ is $2^{1-n}$, the least possible for a monic polynomial of degree $n$.
Hence, if $f$ has $n$ continuous derivatives and $p$ interpolates $f$ at these nodes, then $\max_{[-1, 1]} \abs{f - p} \le \frac{\max \abs{f^{(n)}}}{2^{n-1} n!}$.
The points $\cos(k\pi/n)$, $k = 0, \dots, n$, where $T_n = \pm 1$, are the Chebyshev extreme points, also called Chebyshev–Lobatto points.
